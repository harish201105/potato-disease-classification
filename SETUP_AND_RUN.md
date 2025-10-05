# 🥔 Potato Disease Classification - Setup & Run Guide

This guide provides complete instructions to set up and run your potato disease classification system with TensorFlow backend and React frontend.

## 🚀 **Complete Setup and Run Instructions**

### 1. **Backend API Setup & Run**

#### **First Time Setup:**
```bash
# Navigate to the API directory
cd /Users/harish/potato-disease-classification/api

# Create a virtual environment (recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### **Run the Backend API:**
```bash
# Make sure you're in the api directory and venv is activated
cd /Users/harish/potato-disease-classification/api
source venv/bin/activate

# Option 1: Run with Python directly
python main.py

# Option 2: Run with uvicorn (alternative)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**✅ Backend will be running at:** `http://127.0.0.1:8000`

### 2. **Frontend Setup & Run**

#### **First Time Setup:**
```bash
# Navigate to the frontend directory
cd /Users/harish/potato-disease-classification/frontend

# Install Node.js dependencies
npm install
```

#### **Run the Frontend:**
```bash
# Make sure you're in the frontend directory
cd /Users/harish/potato-disease-classification/frontend

# Start the React development server
NODE_OPTIONS="--openssl-legacy-provider" npm start
```

**✅ Frontend will be running at:** `http://localhost:3000`

## 🔄 **Daily Development Workflow**

### **Terminal 1 - Backend API:**
```bash
cd /Users/harish/potato-disease-classification/api
source venv/bin/activate
python main.py
```

### **Terminal 2 - Frontend:**
```bash
cd /Users/harish/potato-disease-classification/frontend
NODE_OPTIONS="--openssl-legacy-provider" npm start
```

## 🧪 **Test Your Setup**

### **1. Test Backend API:**
```bash
# Test if API is alive
curl http://127.0.0.1:8000/ping

# Test model status
curl http://127.0.0.1:8000/model-status

# Test prediction with an image
curl -X POST -F "file=@/Users/harish/potato-disease-classification/test_images_from_internet/early_blight_1.jpg" http://127.0.0.1:8000/predict
```

### **2. Test Frontend:**
- Open browser to `http://localhost:3000`
- Upload a potato leaf image
- Check if you get real AI predictions (not mock ones)

## 📝 **API Endpoints Available:**

- **Health Check**: `GET http://127.0.0.1:8000/ping`
- **Model Status**: `GET http://127.0.0.1:8000/model-status`
- **Disease Prediction**: `POST http://127.0.0.1:8000/predict`

## 🎯 **Expected Results:**

### **Backend Console Output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Model loaded successfully!
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### **Frontend Console Output:**
```
Local:            http://localhost:3000
On Your Network:  http://192.168.x.x:3000
```

### **AI Predictions:**
Your system will classify potato leaves into:
- 🍃 **Early Blight** (with confidence %)
- 🍃 **Late Blight** (with confidence %)  
- 🍃 **Healthy** (with confidence %)

## 🚨 **Troubleshooting:**

### **If Backend Fails:**
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill any process using port 8000
kill -9 <PID>
```

### **If Frontend Fails:**
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### **If TensorFlow Issues:**
```bash
# Reinstall TensorFlow
pip uninstall tensorflow
pip install tensorflow==2.13.0
```

### **If Model Loading Issues:**
```bash
# Check if converted model exists
ls -la /Users/harish/potato-disease-classification/converted_model.keras

# Check if original model exists
ls -la /Users/harish/potato-disease-classification/potatoes.h5
```

## 🔧 **Project Structure:**

```
potato-disease-classification/
├── api/
│   ├── main.py              # Main FastAPI server with TensorFlow
│   ├── requirements.txt     # Python dependencies
│   └── venv/               # Virtual environment (created after setup)
├── frontend/
│   ├── src/                # React source code
│   ├── package.json        # Node.js dependencies
│   └── node_modules/       # Node.js packages (created after npm install)
├── converted_model.keras   # Keras 3 compatible model
├── potatoes.h5            # Original trained model
├── dataset/               # Training images
├── test_images_from_internet/ # Test images for validation
└── SETUP_AND_RUN.md       # This file
```

## 💡 **Tips:**

1. **Always activate the virtual environment** before running the backend
2. **Use NODE_OPTIONS** flag for the frontend to avoid OpenSSL issues
3. **Test the API endpoints** before testing the full frontend
4. **Check console logs** if something doesn't work as expected
5. **Keep both servers running** in separate terminals for development

## 🎉 **Success Indicators:**

- ✅ Backend API responds to `/ping` with `{"message": "Hello, I am alive"}`
- ✅ Model status shows model is loaded successfully
- ✅ Predictions return confidence percentages > 90% for clear images
- ✅ Frontend loads without errors and can upload images
- ✅ End-to-end flow: Upload image → Get real AI prediction

Your potato disease classification system is now ready for development and testing! 🥔🤖✨