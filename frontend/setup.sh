#!/bin/bash

###############################################################################
# Frontend Setup Script
# ======================
# This script automates the setup process for the React frontend.
#
# Usage: ./setup_frontend.sh
###############################################################################

set -e  # Exit on error

echo "========================================="
echo "Fund Data Chatbot - Frontend Setup"
echo "========================================="
echo ""

# Check Node.js version
echo "Checking Node.js version..."
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed"
    echo "Please install Node.js 18 or higher from https://nodejs.org/"
    exit 1
fi

node_version=$(node --version)
echo "Found Node.js $node_version"

# Check npm
if ! command -v npm &> /dev/null; then
    echo "Error: npm is not installed"
    exit 1
fi

npm_version=$(npm --version)
echo "Found npm $npm_version"

# Install dependencies
echo ""
echo "Installing dependencies..."
npm install
echo "✓ Dependencies installed"

# Setup environment file
echo ""
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
else
    echo ".env file already exists. Skipping..."
fi

echo ""
echo "========================================="
echo "Frontend setup completed successfully! ✓"
echo "========================================="
echo ""
echo "Next steps:"
echo "  1. Ensure backend is running on port 5000"
echo "  2. Run: npm run dev"
echo "  3. Open: http://localhost:3000"
echo ""
