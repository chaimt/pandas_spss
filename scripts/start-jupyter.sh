#!/bin/bash
# Start Jupyter Lab for pandas-spss project

set -e

echo "🚀 Starting Jupyter Lab for pandas-spss project..."

# Change to project root
cd "$(dirname "$0")/.."

# Check if uv is available
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv is not installed or not in PATH"
    exit 1
fi

# Install dependencies if needed
echo "📦 Installing dependencies..."
uv pip install -e .

# Start Jupyter Lab
echo "🔬 Launching Jupyter Lab..."
echo "📁 Project root: $(pwd)"
echo "📁 Notebooks directory: $(pwd)/notebooks"
echo "🐍 Python path includes: $(pwd)/src"
echo ""
echo "💡 Tips:"
echo "  - Open notebooks/pandas_spss_demo.ipynb to get started"
echo "  - The src/ directory is automatically added to Python path"
echo "  - Use Ctrl+C to stop Jupyter Lab"
echo ""

uv run jupyter lab --notebook-dir="$(pwd)" --ip=0.0.0.0 --port=8888 --no-browser
