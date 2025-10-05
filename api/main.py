
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import logging
import os
from contextlib import asynccontextmanager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model when server starts
MODEL = None
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def load_model():
    global MODEL
    try:
        # Check if converted model exists first, then fallback to original models
        model_paths = [
            "/Users/harish/potato-disease-classification/converted_model.keras",
            "../converted_model.keras",
            "/Users/harish/potato-disease-classification/potatoes.h5",
            "../potatoes.h5",
            "../saved_models/1",
            "/Users/harish/potato-disease-classification/saved_models/1",
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "saved_models", "1")
        ]
        
        model_path = None
        for path in model_paths:
            if os.path.exists(path):
                model_path = path
                break
                
        if not model_path:
            logger.error(f"Model not found in any of: {model_paths}")
            return False
            
        logger.info(f"Loading model from {model_path}")
        import tensorflow as tf
        
        # Set memory growth to avoid GPU memory issues
        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
            except RuntimeError as e:
                logger.warning(f"GPU setup warning: {e}")
        
        # Load the model - Keras 3 format should load directly
        MODEL = tf.keras.models.load_model(model_path)
        logger.info(f"Model loaded successfully! Input shape: {MODEL.input_shape}")
        logger.info(f"Model output shape: {MODEL.output_shape}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        logger.info("API will run with mock predictions")
        return False

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    load_model()
    yield
    # Shutdown
    pass

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

@app.get("/model-status")
async def model_status():
    return {
        "model_loaded": MODEL is not None,
        "classes": CLASS_NAMES
    }

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    try:
        image = read_file_as_image(await file.read())
        
        if MODEL is not None:
            # Resize image to expected input size (256x256 based on model)
            img = Image.fromarray(image)
            img = img.resize((256, 256))
            img_array = np.array(img)
            
            # Normalize pixel values to [0,1]
            img_array = img_array.astype('float32') / 255.0
            
            # Add batch dimension
            img_batch = np.expand_dims(img_array, 0)
            
            # Make prediction with the converted Keras model
            predictions = MODEL.predict(img_batch, verbose=0)
            predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
            confidence = float(np.max(predictions[0]))
            
            logger.info(f"Real prediction: {predicted_class} with confidence: {confidence:.3f}")
        else:
            # Fallback to mock prediction
            import random
            predicted_class = random.choice(CLASS_NAMES)
            confidence = round(random.uniform(0.7, 0.95), 2)
            logger.info(f"Mock prediction: {predicted_class} with confidence: {confidence}")
        
        return {
            'class': predicted_class,
            'confidence': confidence,
            'model_used': MODEL is not None
        }
        
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {
            'error': str(e),
            'class': 'Unknown',
            'confidence': 0.0,
            'model_used': False
        }

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

