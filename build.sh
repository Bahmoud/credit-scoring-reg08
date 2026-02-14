#!/bin/bash
# Build script for Render

set -e  # Exit on error

echo "🔧 Starting build process..."

# Update pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Train model if it doesn't exist
if [ ! -f "models/credit_scoring_model.pkl" ]; then
    echo "🤖 Training model..."
    python src/pipeline.py
else
    echo "✅ Model already exists, skipping training"
fi

echo "✅ Build completed successfully!"
