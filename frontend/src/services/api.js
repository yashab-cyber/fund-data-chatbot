/**
 * API Service Module
 * ==================
 * Handles all communication with the backend API.
 * Provides methods for querying the chatbot, fetching models, and getting data summaries.
 * 
 * @module apiService
 */

import axios from 'axios';

// Configure API base URL - reads from environment variable or defaults to localhost
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000, // 60 second timeout for LLM responses
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Query the chatbot with a question
 * 
 * @param {string} question - The user's question
 * @param {string} provider - LLM provider (openai, gemini, anthropic)
 * @param {string} model - Specific model to use (optional)
 * @returns {Promise<Object>} Response containing answer and metadata
 */
export const queryChatbot = async (question, provider = 'openai', model = null) => {
  try {
    const response = await apiClient.post('/api/query', {
      question,
      provider,
      model,
    });
    return response.data;
  } catch (error) {
    console.error('Error querying chatbot:', error);
    throw new Error(
      error.response?.data?.error || 
      error.message || 
      'Failed to get response from chatbot'
    );
  }
};

/**
 * Get list of available LLM models
 * 
 * @returns {Promise<Object>} Object with available models per provider
 */
export const getAvailableModels = async () => {
  try {
    const response = await apiClient.get('/api/models');
    return response.data;
  } catch (error) {
    console.error('Error fetching models:', error);
    throw new Error('Failed to fetch available models');
  }
};

/**
 * Get summary of the fund data
 * 
 * @returns {Promise<Object>} Data summary with statistics
 */
export const getDataSummary = async () => {
  try {
    const response = await apiClient.get('/api/data-summary');
    return response.data;
  } catch (error) {
    console.error('Error fetching data summary:', error);
    throw new Error('Failed to fetch data summary');
  }
};

/**
 * Get list of all funds
 * 
 * @returns {Promise<Array>} Array of fund names
 */
export const getFunds = async () => {
  try {
    const response = await apiClient.get('/api/funds');
    return response.data;
  } catch (error) {
    console.error('Error fetching funds:', error);
    throw new Error('Failed to fetch funds');
  }
};

/**
 * Check API health status
 * 
 * @returns {Promise<Object>} Health status object
 */
export const checkHealth = async () => {
  try {
    const response = await apiClient.get('/health');
    return response.data;
  } catch (error) {
    console.error('Error checking API health:', error);
    throw new Error('API is not responding');
  }
};

export default {
  queryChatbot,
  getAvailableModels,
  getDataSummary,
  getFunds,
  checkHealth,
};
