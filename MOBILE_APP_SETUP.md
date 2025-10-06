# 📱 **Potato Disease Classification Mobile App Setup Guide**

## 🛠 **Prerequisites**

### **Required Software:**
1. **Node.js** (version 14 or higher)
2. **npm** or **yarn**
3. **React Native CLI** 
4. **Xcode** (for iOS development - macOS only)
5. **Android Studio** (for Android development)
6. **CocoaPods** (for iOS dependencies)

## 🚀 **Setup Instructions**

### **1. Install React Native CLI**
```bash
npm install -g react-native-cli
```

### **2. Install CocoaPods (for iOS)**
```bash
sudo gem install cocoapods
```

### **3. Navigate to Mobile App Directory**
```bash
cd /Users/harish/potato-disease-classification/mobile-app
```

### **4. Install Dependencies**
```bash
# Install Node.js dependencies
npm install

# For iOS - install CocoaPods dependencies
cd ios && pod install && cd ..
```

### **5. Configure Environment Variables**
```bash
# Create .env file from example
cp .env.example .env

# Edit .env file to point to your API
echo "URL='http://127.0.0.1:8000/predict'" > .env
```

## 🎯 **Running the App**

### **For iOS Simulator:**
```bash
cd /Users/harish/potato-disease-classification/mobile-app
npx react-native run-ios
```

### **For Android Emulator:**
```bash
cd /Users/harish/potato-disease-classification/mobile-app
npx react-native run-android
```

### **Start Metro Bundler (in separate terminal):**
```bash
cd /Users/harish/potato-disease-classification/mobile-app
npx react-native start
```

## 📋 **Step-by-Step Setup Process**

### **Step 1: Check Prerequisites**
```bash
# Check Node.js version
node --version

# Check npm version  
npm --version

# Check if React Native CLI is installed
react-native --version
```

### **Step 2: Install Xcode (for iOS)**
1. Download Xcode from App Store
2. Install Xcode Command Line Tools:
   ```bash
   xcode-select --install
   ```

### **Step 3: Install Android Studio (for Android)**
1. Download Android Studio
2. Set up Android SDK
3. Configure Android environment variables

### **Step 4: Setup iOS Development**
```bash
cd /Users/harish/potato-disease-classification/mobile-app/ios
pod install
```

### **Step 5: Configure API Endpoint**
Edit the `.env` file:
```bash
URL='http://127.0.0.1:8000/predict'
```

**Note**: For physical devices, replace `127.0.0.1` with your computer's IP address.

## 🔧 **Troubleshooting**

### **Common Issues:**

#### **1. Metro Bundler Issues**
```bash
# Reset Metro cache
npx react-native start --reset-cache
```

#### **2. iOS Build Issues**
```bash
# Clean iOS build
cd ios && xcodebuild clean && cd ..
```

#### **3. Android Build Issues**
```bash
# Clean Android build
cd android && ./gradlew clean && cd ..
```

#### **4. Permission Issues**
```bash
# Fix permission for gradlew
chmod +x android/gradlew
```

## 📱 **Device Setup**

### **iOS Physical Device:**
1. Enable Developer Mode on iPhone
2. Trust the developer certificate
3. Update .env with computer's IP address

### **Android Physical Device:**
1. Enable Developer Options
2. Enable USB Debugging
3. Update .env with computer's IP address

## 🌐 **Network Configuration**

### **Find Your Computer's IP Address:**
```bash
# On macOS
ifconfig | grep "inet " | grep -v 127.0.0.1

# Your IP will be something like: 192.168.1.xxx
```

### **Update .env for Physical Devices:**
```bash
# Replace 127.0.0.1 with your actual IP
URL='http://192.168.1.xxx:8000/predict'
```

## 🧪 **Testing the App**

### **1. Ensure Backend is Running**
```bash
# In api directory
cd /Users/harish/potato-disease-classification/api
conda activate llmapp
uvicorn main:app --host 0.0.0.0 --port 8000
```

### **2. Test API Connection**
```bash
curl http://127.0.0.1:8000/ping
```

### **3. Run Mobile App**
```bash
# In mobile-app directory
npx react-native run-ios
# or
npx react-native run-android
```

## 📸 **App Features**

The mobile app allows users to:
- 📷 **Take photos** with camera
- 🖼️ **Select images** from gallery
- 🔍 **Get disease predictions** from your AI model
- 📊 **View confidence scores** for predictions
- 🍃 **Classify**: Early Blight, Late Blight, Healthy

## 🎉 **Success Indicators**

- ✅ Metro bundler starts without errors
- ✅ App launches on simulator/device
- ✅ Camera and gallery access work
- ✅ Image upload and prediction work
- ✅ Results display properly

## 🆘 **Need Help?**

If you encounter issues:
1. Check that all prerequisites are installed
2. Ensure the backend API is running
3. Verify network connectivity
4. Check device/simulator setup
5. Review error logs in terminal

Your mobile app is ready to provide portable potato disease classification! 📱🥔🤖