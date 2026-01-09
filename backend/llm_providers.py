"""
LLM Providers Module
====================
This module provides unified interfaces to multiple Large Language Model providers:
- OpenAI (GPT-4, GPT-5.1)
- Google Gemini (Gemini Pro, Gemini 3)
- Anthropic (Claude 3 Opus, Claude 3.5 Sonnet)

Each provider has a consistent interface for querying with context.

Author: Fund Data Chatbot Team
Date: 2026-01-09
"""

import os
import logging
from typing import Optional, Dict, List
import openai
import anthropic
import google.generativeai as genai

logger = logging.getLogger(__name__)

# Initialize API clients
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

# Configure OpenAI
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

# Configure Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None


# Model configurations
MODELS_CONFIG = {
    'openai': {
        'models': [
            {'id': 'gpt-4', 'name': 'GPT-4', 'description': 'Most capable OpenAI model'},
            {'id': 'gpt-4-turbo-preview', 'name': 'GPT-4 Turbo', 'description': 'Faster GPT-4 variant'},
            {'id': 'gpt-3.5-turbo', 'name': 'GPT-3.5 Turbo', 'description': 'Fast and efficient'},
        ],
        'default': 'gpt-4'
    },
    'gemini': {
        'models': [
            {'id': 'gemini-pro', 'name': 'Gemini Pro', 'description': 'Google\'s most capable model'},
            {'id': 'gemini-1.5-pro', 'name': 'Gemini 1.5 Pro', 'description': 'Enhanced Gemini Pro'},
            {'id': 'gemini-1.5-flash', 'name': 'Gemini 1.5 Flash', 'description': 'Fast and efficient'},
        ],
        'default': 'gemini-pro'
    },
    'anthropic': {
        'models': [
            {'id': 'claude-3-5-sonnet-20241022', 'name': 'Claude 3.5 Sonnet', 'description': 'Most capable Claude model'},
            {'id': 'claude-3-opus-20240229', 'name': 'Claude 3 Opus', 'description': 'Powerful analysis and reasoning'},
            {'id': 'claude-3-sonnet-20240229', 'name': 'Claude 3 Sonnet', 'description': 'Balanced performance'},
        ],
        'default': 'claude-3-5-sonnet-20241022'
    }
}


def get_available_models() -> Dict[str, List[Dict]]:
    """
    Get list of available models for each provider.
    
    Returns:
        Dictionary with provider names as keys and model lists as values
    """
    available = {}
    
    # Check OpenAI
    if OPENAI_API_KEY:
        available['openai'] = MODELS_CONFIG['openai']
    
    # Check Gemini
    if GEMINI_API_KEY:
        available['gemini'] = MODELS_CONFIG['gemini']
    
    # Check Anthropic
    if ANTHROPIC_API_KEY:
        available['anthropic'] = MODELS_CONFIG['anthropic']
    
    return available


def create_system_prompt(context: str) -> str:
    """
    Create a system prompt that includes the data context and instructions.
    
    Args:
        context: The relevant data context
    
    Returns:
        Formatted system prompt
    """
    return f"""You are a helpful financial data analyst assistant specialized in analyzing fund data.

You have access to the following fund data:

{context}

IMPORTANT RULES:
1. Only answer questions based on the data provided above
2. If the answer is not in the provided data, you MUST respond with: "Sorry, I cannot find the answer in the provided fund data."
3. Do not use external knowledge or make assumptions
4. Provide specific numbers and facts from the data when available
5. Be concise and accurate
6. When comparing funds, use the Profit/Loss YTD (PL_YTD) values
7. Format numbers with appropriate currency symbols and thousands separators

Answer the user's question based solely on the data provided above."""


def query_openai(question: str, context: str, model: Optional[str] = None) -> str:
    """
    Query OpenAI's GPT models.
    
    Args:
        question: User's question
        context: Relevant data context
        model: Specific model to use (default: gpt-4)
    
    Returns:
        Model's response
    
    Raises:
        Exception: If API key is not set or API call fails
    """
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key not configured. Please set OPENAI_API_KEY environment variable."
    
    try:
        model_name = model or MODELS_CONFIG['openai']['default']
        system_prompt = create_system_prompt(context)
        
        logger.info(f"Querying OpenAI model: {model_name}")
        
        response = openai.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.3,  # Lower temperature for more factual responses
            max_tokens=1000
        )
        
        answer = response.choices[0].message.content
        logger.info("OpenAI response received successfully")
        return answer
        
    except Exception as e:
        logger.error(f"Error querying OpenAI: {str(e)}")
        return f"Error querying OpenAI: {str(e)}"


def query_gemini(question: str, context: str, model: Optional[str] = None) -> str:
    """
    Query Google's Gemini models.
    
    Args:
        question: User's question
        context: Relevant data context
        model: Specific model to use (default: gemini-pro)
    
    Returns:
        Model's response
    
    Raises:
        Exception: If API key is not set or API call fails
    """
    if not GEMINI_API_KEY:
        return "Error: Gemini API key not configured. Please set GEMINI_API_KEY environment variable."
    
    try:
        model_name = model or MODELS_CONFIG['gemini']['default']
        system_prompt = create_system_prompt(context)
        
        logger.info(f"Querying Gemini model: {model_name}")
        
        # Initialize model
        gemini_model = genai.GenerativeModel(model_name)
        
        # Create full prompt
        full_prompt = f"{system_prompt}\n\nUser Question: {question}"
        
        # Generate response
        response = gemini_model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.3,
                max_output_tokens=1000,
            )
        )
        
        answer = response.text
        logger.info("Gemini response received successfully")
        return answer
        
    except Exception as e:
        logger.error(f"Error querying Gemini: {str(e)}")
        return f"Error querying Gemini: {str(e)}"


def query_anthropic(question: str, context: str, model: Optional[str] = None) -> str:
    """
    Query Anthropic's Claude models.
    
    Args:
        question: User's question
        context: Relevant data context
        model: Specific model to use (default: claude-3-5-sonnet)
    
    Returns:
        Model's response
    
    Raises:
        Exception: If API key is not set or API call fails
    """
    if not ANTHROPIC_API_KEY or not anthropic_client:
        return "Error: Anthropic API key not configured. Please set ANTHROPIC_API_KEY environment variable."
    
    try:
        model_name = model or MODELS_CONFIG['anthropic']['default']
        system_prompt = create_system_prompt(context)
        
        logger.info(f"Querying Anthropic model: {model_name}")
        
        response = anthropic_client.messages.create(
            model=model_name,
            max_tokens=1000,
            temperature=0.3,
            system=system_prompt,
            messages=[
                {"role": "user", "content": question}
            ]
        )
        
        answer = response.content[0].text
        logger.info("Anthropic response received successfully")
        return answer
        
    except Exception as e:
        logger.error(f"Error querying Anthropic: {str(e)}")
        return f"Error querying Anthropic: {str(e)}"


def test_providers() -> Dict[str, bool]:
    """
    Test which providers are available and configured.
    
    Returns:
        Dictionary with provider names and their availability status
    """
    status = {
        'openai': bool(OPENAI_API_KEY),
        'gemini': bool(GEMINI_API_KEY),
        'anthropic': bool(ANTHROPIC_API_KEY)
    }
    
    logger.info(f"Provider status: {status}")
    return status
