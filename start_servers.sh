#!/bin/bash

echo "🚀 Starting Potato Disease Classification Servers..."

# Start backend in background
echo "📡 Starting Backend API on http://127.0.0.1:8000..."
cd /Users/harish/potato-disease-classification/api
conda activate llmapp
nohup uvicorn main:app --host 127.0.0.1 --port 8000 > backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend started with PID: $BACKEND_PID"

# Wait a moment for backend to start
sleep 3

# Test backend
echo "🧪 Testing backend..."
if curl -s http://127.0.0.1:8000/ping > /dev/null; then
    echo "✅ Backend is running successfully!"
else
    echo "❌ Backend failed to start"
fi

echo ""
echo "🌐 Frontend should already be running on http://localhost:3000"
echo "📊 Backend API available at http://127.0.0.1:8000"
echo ""
echo "📋 Available endpoints:"
echo "  • GET  http://127.0.0.1:8000/ping"
echo "  • GET  http://127.0.0.1:8000/model-status"
echo "  • POST http://127.0.0.1:8000/predict"
echo ""
echo "🛑 To stop backend: kill $BACKEND_PID"
echo "📄 Backend logs: /Users/harish/potato-disease-classification/api/backend.log"