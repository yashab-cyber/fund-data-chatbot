#!/bin/bash

###############################################################################
# Backend Setup Script
# ====================
# This script automates the setup process for the backend server.
# It creates a virtual environment, installs dependencies, and sets up
# environment variables.
#
# Usage: ./setup_backend.sh
###############################################################################

set -e  # Exit on error

echo "========================================="
echo "Fund Data Chatbot - Backend Setup"
echo "========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

if ! python3 -c 'import sys; exit(0 if sys.version_info >= (3, 9) else 1)'; then
    echo "Error: Python 3.9 or higher is required"
    exit 1
fi

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Setup environment file
echo ""
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env file and add your API keys!"
    echo ""
    echo "Required API keys:"
    echo "  - OPENAI_API_KEY (https://platform.openai.com/api-keys)"
    echo "  - GEMINI_API_KEY (https://makersuite.google.com/app/apikey)"
    echo "  - ANTHROPIC_API_KEY (https://console.anthropic.com/)"
else
    echo ".env file already exists. Skipping..."
fi

echo ""
echo "========================================="
echo "Backend setup completed successfully! ✓"
echo "========================================="
echo ""
echo "Next steps:"
echo "  1. Edit backend/.env and add your API keys"
echo "  2. Run: source venv/bin/activate"
echo "  3. Run: python app.py"
echo ""
