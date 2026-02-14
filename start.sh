#!/bin/bash
# Start script for Render

set -e

echo "🚀 Starting Credit Scoring API..."

# Check if model exists
if [ ! -f "models/credit_scoring_model.pkl" ]; then
    echo "⚠️  Model not found, training..."
    python src/pipeline.py
fi

# Start the API
echo "🌐 Launching API on port ${PORT:-8000}..."
exec uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}
