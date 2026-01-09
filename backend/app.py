"""
Fund Data Chatbot Backend API
================================
This Flask application provides a REST API for querying fund data using multiple LLM providers.
It supports OpenAI GPT-4, Google Gemini, and Anthropic Claude models.

The application implements RAG (Retrieval Augmented Generation) to ensure responses
are based solely on the provided CSV data files.

Author: Fund Data Chatbot Team
Date: 2026-01-09
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime
import logging

# Import LLM clients
from llm_providers import (
    query_openai,
    query_gemini,
    query_anthropic,
    get_available_models
)
from data_processor import DataProcessor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Initialize data processor
data_processor = DataProcessor()


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    
    Returns:
        JSON response with status and timestamp
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Fund Data Chatbot API'
    })


@app.route('/api/models', methods=['GET'])
def get_models():
    """
    Get list of available LLM models.
    
    Returns:
        JSON response with available models grouped by provider
    """
    try:
        models = get_available_models()
        return jsonify({
            'success': True,
            'models': models
        })
    except Exception as e:
        logger.error(f"Error fetching models: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/data-summary', methods=['GET'])
def get_data_summary():
    """
    Get summary statistics of the loaded data.
    
    Returns:
        JSON response with data summary including:
        - Number of holdings and trades
        - List of unique funds
        - Date ranges
        - Basic statistics
    """
    try:
        summary = data_processor.get_data_summary()
        return jsonify({
            'success': True,
            'summary': summary
        })
    except Exception as e:
        logger.error(f"Error getting data summary: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/query', methods=['POST'])
def query_chatbot():
    """
    Main endpoint for querying the chatbot.
    
    Expected JSON payload:
    {
        "question": "Your question about fund data",
        "provider": "openai" | "gemini" | "anthropic",
        "model": "specific-model-name" (optional)
    }
    
    Returns:
        JSON response with:
        - answer: The LLM's response
        - context: Relevant data context used
        - provider: Which LLM was used
        - model: Specific model used
        - timestamp: When the query was processed
    """
    try:
        # Parse request data
        data = request.get_json()
        question = data.get('question', '').strip()
        provider = data.get('provider', 'openai').lower()
        model = data.get('model')
        
        # Validate input
        if not question:
            return jsonify({
                'success': False,
                'error': 'Question is required'
            }), 400
        
        # Get relevant context from data
        context = data_processor.get_relevant_context(question)
        
        # Check if context is empty
        if not context or context == "No relevant data found.":
            return jsonify({
                'success': True,
                'answer': "Sorry, I cannot find the answer in the provided fund data.",
                'context': context,
                'provider': provider,
                'model': model or 'N/A',
                'timestamp': datetime.now().isoformat()
            })
        
        # Query the appropriate LLM
        if provider == 'openai':
            answer = query_openai(question, context, model)
        elif provider == 'gemini':
            answer = query_gemini(question, context, model)
        elif provider == 'anthropic':
            answer = query_anthropic(question, context, model)
        else:
            return jsonify({
                'success': False,
                'error': f'Invalid provider: {provider}. Must be one of: openai, gemini, anthropic'
            }), 400
        
        # Return response
        return jsonify({
            'success': True,
            'answer': answer,
            'context': context,
            'provider': provider,
            'model': model or 'default',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500


@app.route('/api/funds', methods=['GET'])
def get_funds():
    """
    Get list of all unique funds in the dataset.
    
    Returns:
        JSON response with list of fund names
    """
    try:
        funds = data_processor.get_unique_funds()
        return jsonify({
            'success': True,
            'funds': funds
        })
    except Exception as e:
        logger.error(f"Error fetching funds: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    """
    Run the Flask application.
    
    Configuration:
    - Host: 0.0.0.0 (accessible from all network interfaces)
    - Port: 5000
    - Debug: False (production mode)
    """
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    logger.info("="*60)
    logger.info("Fund Data Chatbot API Starting...")
    logger.info(f"Port: {port}")
    logger.info(f"Debug Mode: {debug_mode}")
    logger.info("="*60)
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
