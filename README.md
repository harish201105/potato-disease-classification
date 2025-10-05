# Potato Disease Classification

## Setup for Python:

1. Install Python ([Setup instructions](https://wiki.python.org/moin/BeginnersGuide))

2. Install Python packages

```
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt
```

3. Install Tensorflow Serving ([Setup instructions](https://www.tensorflow.org/tfx/serving/setup))

## Setup for ReactJS

1. Install Nodejs ([Setup instructions](https://nodejs.org/en/download/package-manager/))
2. Install NPM ([Setup instructions](https://www.npmjs.com/get-npm))
3. Install dependencies

```bash
cd frontend
npm install --from-lock-json
npm audit fix
```

4. Copy `.env.example` as `.env`.

5. Change API url in `.env`.

## Setup for React-Native app

1. Go to the [React Native environment setup](https://reactnative.dev/docs/environment-setup), then select `React Native CLI Quickstart` tab.  

2. Install dependencies

```bash
cd mobile-app
yarn install
```

  - 2.1 Only for mac users
```bash
cd ios && pod install && cd ../
```

3. Copy `.env.example` as `.env`.

4. Change API url in `.env`.

## Training the Model

1. Download the data from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village).
2. Only keep folders related to Potatoes.
3. Run Jupyter Notebook in Browser.

```bash
jupyter notebook
```

4. Open `training/potato-disease-training.ipynb` in Jupyter Notebook.
5. In cell #2, update the path to dataset.
6. Run all the Cells one by one.
7. Copy the model generated and save it with the version number in the `models` folder.

## Running the API

1. Get inside `api` folder

```bash
cd api
```

2. Run the FastAPI Server using uvicorn

```bash
uvicorn main:app --reload --host 0.0.0.0
```

3. Your API is now running at `0.0.0.0:8000`

### Using FastAPI (Recommended for Local Development)

This is the simplest way to run the API locally without Docker dependencies.

## Running the Frontend

1. Get inside `api` folder

```bash
cd frontend
```

2. Copy the `.env.example` as `.env` and update `REACT_APP_API_URL` to API URL if needed.
3. Run the frontend

```bash
npm run start
```

## Running the app

1. Get inside `mobile-app` folder

```bash
cd mobile-app
```

2. Copy the `.env.example` as `.env` and update `URL` to API URL if needed.

3. Run the app (android/iOS)

```bash
npm run android
```

or

```bash
npm run ios
```

4. Creating public ([signed APK](https://reactnative.dev/docs/signed-apk-android))


## Creating the TF Lite Model

1. Run Jupyter Notebook in Browser.

```bash
jupyter notebook
```

2. Open `training/tf-lite-converter.ipynb` in Jupyter Notebook.
3. In cell #2, update the path to dataset.
4. Run all the Cells one by one.
5. Model would be saved in `tf-lite-models` folder.

---

## Project Structure

This project is organized for local development and includes:

- **`/api/`** - FastAPI backend for model inference
- **`/frontend/`** - React.js web application
- **`/mobile-app/`** - React Native mobile application
- **`/training/`** - Jupyter notebooks for model training and conversion
- **`/saved_models/`** - Trained TensorFlow models
- **`/tf-lite-models/`** - Optimized models for mobile deployment
- **`/test_images_from_internet/`** - Sample test images

## Local Development Workflow

1. **Train the model** using the Jupyter notebooks in `/training/`
2. **Run the API** using FastAPI in `/api/`
3. **Run the frontend** React app in `/frontend/`
4. **Test with mobile app** using React Native in `/mobile-app/`

All components are designed to work together locally without requiring cloud services.

