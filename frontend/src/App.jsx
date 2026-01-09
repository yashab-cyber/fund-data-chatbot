/**
 * App Component
 * =============
 * Main application component for the Fund Data Chatbot.
 * Features a beautiful, modern UI with:
 * - Real-time chat interface
 * - Multiple LLM provider selection
 * - Data summary dashboard
 * - Responsive design
 * 
 * @component
 */

import React, { useState, useEffect, useRef } from 'react';
import { 
  MessageCircle, 
  Send, 
  TrendingUp, 
  Database, 
  Sparkles,
  ChevronDown,
  Activity,
  DollarSign,
  BarChart3,
  AlertCircle
} from 'lucide-react';
import { queryChatbot, getAvailableModels, getDataSummary } from './services/api';
import ReactMarkdown from 'react-markdown';

function App() {
  // State management
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedProvider, setSelectedProvider] = useState('openai');
  const [selectedModel, setSelectedModel] = useState(null);
  const [availableModels, setAvailableModels] = useState({});
  const [dataSummary, setDataSummary] = useState(null);
  const [showProviderMenu, setShowProviderMenu] = useState(false);
  const [error, setError] = useState(null);
  
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  /**
   * Auto-scroll to bottom of messages
   */
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  /**
   * Load available models and data summary on component mount
   */
  useEffect(() => {
    const loadInitialData = async () => {
      try {
        // Load available models
        const modelsResponse = await getAvailableModels();
        if (modelsResponse.success) {
          setAvailableModels(modelsResponse.models);
          
          // Set default provider and model
          const providers = Object.keys(modelsResponse.models);
          if (providers.length > 0) {
            const firstProvider = providers[0];
            setSelectedProvider(firstProvider);
            setSelectedModel(modelsResponse.models[firstProvider].default);
          }
        }

        // Load data summary
        const summaryResponse = await getDataSummary();
        if (summaryResponse.success) {
          setDataSummary(summaryResponse.summary);
        }

        // Add welcome message
        setMessages([{
          type: 'bot',
          content: '👋 Welcome to Fund Data Chatbot! I can help you analyze fund holdings and trades. Try asking me:\n\n• "How many holdings does Garfield fund have?"\n• "Which funds performed better based on yearly P&L?"\n• "Show me total trades for MNC Investment Fund"',
          timestamp: new Date().toISOString(),
        }]);

      } catch (err) {
        setError('Failed to initialize chatbot. Please check if the backend server is running.');
        console.error('Initialization error:', err);
      }
    };

    loadInitialData();
  }, []);

  /**
   * Handle form submission
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    const userMessage = {
      type: 'user',
      content: inputValue,
      timestamp: new Date().toISOString(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    setError(null);

    try {
      const response = await queryChatbot(
        inputValue,
        selectedProvider,
        selectedModel
      );

      if (response.success) {
        const botMessage = {
          type: 'bot',
          content: response.answer,
          timestamp: response.timestamp,
          provider: response.provider,
          model: response.model,
        };
        setMessages(prev => [...prev, botMessage]);
      } else {
        throw new Error(response.error || 'Failed to get response');
      }
    } catch (err) {
      const errorMessage = {
        type: 'bot',
        content: `❌ Error: ${err.message}`,
        timestamp: new Date().toISOString(),
        isError: true,
      };
      setMessages(prev => [...prev, errorMessage]);
      setError(err.message);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  /**
   * Format numbers with commas
   */
  const formatNumber = (num) => {
    return num?.toLocaleString() || '0';
  };

  /**
   * Get provider icon color
   */
  const getProviderColor = (provider) => {
    const colors = {
      openai: 'text-green-600',
      gemini: 'text-blue-600',
      anthropic: 'text-purple-600',
    };
    return colors[provider] || 'text-gray-600';
  };

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="glass-effect border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="bg-gradient-to-br from-blue-600 to-purple-600 p-2 rounded-xl">
                <TrendingUp className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                  Fund Data Chatbot
                </h1>
                <p className="text-sm text-gray-600">AI-Powered Financial Analysis</p>
              </div>
            </div>
            
            {/* Provider Selection */}
            <div className="relative">
              <button
                onClick={() => setShowProviderMenu(!showProviderMenu)}
                className="flex items-center space-x-2 px-4 py-2 bg-white rounded-lg border-2 border-gray-200 hover:border-blue-500 transition-all"
              >
                <Sparkles className={`w-5 h-5 ${getProviderColor(selectedProvider)}`} />
                <span className="font-medium capitalize">{selectedProvider}</span>
                <ChevronDown className="w-4 h-4" />
              </button>

              {/* Provider Dropdown */}
              {showProviderMenu && (
                <div className="absolute right-0 mt-2 w-64 bg-white rounded-lg shadow-xl border border-gray-200 py-2 z-20">
                  {Object.keys(availableModels).map((provider) => (
                    <div key={provider} className="px-4 py-2">
                      <button
                        onClick={() => {
                          setSelectedProvider(provider);
                          setSelectedModel(availableModels[provider].default);
                          setShowProviderMenu(false);
                        }}
                        className={`w-full text-left px-3 py-2 rounded-md transition-all ${
                          selectedProvider === provider
                            ? 'bg-blue-100 text-blue-700'
                            : 'hover:bg-gray-100'
                        }`}
                      >
                        <div className="flex items-center space-x-2">
                          <Sparkles className={`w-4 h-4 ${getProviderColor(provider)}`} />
                          <span className="font-medium capitalize">{provider}</span>
                        </div>
                        <div className="text-xs text-gray-500 mt-1 ml-6">
                          {availableModels[provider].models.length} models available
                        </div>
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 h-full">
          {/* Sidebar - Data Summary */}
          <aside className="lg:col-span-1 space-y-4">
            <div className="card animate-fade-in">
              <h2 className="text-lg font-bold text-gray-800 mb-4 flex items-center">
                <Database className="w-5 h-5 mr-2 text-blue-600" />
                Data Overview
              </h2>
              
              {dataSummary ? (
                <div className="space-y-3">
                  <div className="bg-gradient-to-r from-blue-50 to-blue-100 p-3 rounded-lg">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-gray-600">Holdings</span>
                      <BarChart3 className="w-4 h-4 text-blue-600" />
                    </div>
                    <p className="text-2xl font-bold text-blue-700">
                      {formatNumber(dataSummary.holdings?.total_records)}
                    </p>
                  </div>

                  <div className="bg-gradient-to-r from-purple-50 to-purple-100 p-3 rounded-lg">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-gray-600">Trades</span>
                      <Activity className="w-4 h-4 text-purple-600" />
                    </div>
                    <p className="text-2xl font-bold text-purple-700">
                      {formatNumber(dataSummary.trades?.total_records)}
                    </p>
                  </div>

                  <div className="bg-gradient-to-r from-green-50 to-green-100 p-3 rounded-lg">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-gray-600">Funds</span>
                      <DollarSign className="w-4 h-4 text-green-600" />
                    </div>
                    <p className="text-2xl font-bold text-green-700">
                      {dataSummary.funds?.length || 0}
                    </p>
                  </div>

                  <div className="mt-4 pt-4 border-t border-gray-200">
                    <h3 className="text-xs font-semibold text-gray-500 uppercase mb-2">
                      Sample Funds
                    </h3>
                    <div className="space-y-1 max-h-40 overflow-y-auto">
                      {dataSummary.funds?.slice(0, 10).map((fund, idx) => (
                        <div
                          key={idx}
                          className="text-xs text-gray-700 py-1 px-2 bg-gray-50 rounded"
                        >
                          {fund}
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              ) : (
                <div className="text-center py-4">
                  <div className="loading-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                  <p className="text-sm text-gray-500 mt-2">Loading data...</p>
                </div>
              )}
            </div>

            {/* Example Questions */}
            <div className="card animate-fade-in">
              <h2 className="text-lg font-bold text-gray-800 mb-3 flex items-center">
                <MessageCircle className="w-5 h-5 mr-2 text-purple-600" />
                Try Asking
              </h2>
              <div className="space-y-2">
                {[
                  'Total holdings for Garfield fund',
                  'Which funds performed better?',
                  'Show trades summary',
                ].map((question, idx) => (
                  <button
                    key={idx}
                    onClick={() => setInputValue(question)}
                    className="w-full text-left text-sm p-2 rounded-lg bg-gray-50 hover:bg-blue-50 hover:text-blue-700 transition-all"
                  >
                    {question}
                  </button>
                ))}
              </div>
            </div>
          </aside>

          {/* Chat Area */}
          <div className="lg:col-span-3 flex flex-col h-[calc(100vh-200px)]">
            <div className="card flex-1 flex flex-col">
              {/* Messages Container */}
              <div className="flex-1 overflow-y-auto space-y-4 mb-4 pr-2">
                {error && (
                  <div className="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-2">
                    <AlertCircle className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" />
                    <div className="flex-1">
                      <p className="text-sm font-medium text-red-800">Connection Error</p>
                      <p className="text-xs text-red-600 mt-1">{error}</p>
                    </div>
                  </div>
                )}

                {messages.map((message, idx) => (
                  <div
                    key={idx}
                    className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
                  >
                    <div className={message.type === 'user' ? 'message-user' : 'message-bot'}>
                      <ReactMarkdown>{message.content}</ReactMarkdown>
                      {message.provider && (
                        <div className="text-xs opacity-70 mt-2 flex items-center space-x-1">
                          <Sparkles className="w-3 h-3" />
                          <span className="capitalize">{message.provider}</span>
                          {message.model && <span>• {message.model}</span>}
                        </div>
                      )}
                    </div>
                  </div>
                ))}

                {isLoading && (
                  <div className="flex justify-start">
                    <div className="message-bot">
                      <div className="loading-dots">
                        <span></span>
                        <span></span>
                        <span></span>
                      </div>
                      <p className="text-sm text-gray-600 mt-2">Analyzing data...</p>
                    </div>
                  </div>
                )}

                <div ref={messagesEndRef} />
              </div>

              {/* Input Form */}
              <form onSubmit={handleSubmit} className="flex space-x-2">
                <input
                  ref={inputRef}
                  type="text"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  placeholder="Ask about fund holdings, trades, or performance..."
                  className="input-field flex-1"
                  disabled={isLoading}
                />
                <button
                  type="submit"
                  disabled={isLoading || !inputValue.trim()}
                  className="btn-primary flex items-center space-x-2"
                >
                  <Send className="w-5 h-5" />
                  <span>Send</span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="glass-effect border-t border-gray-200 py-4">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <p className="text-center text-sm text-gray-600">
            Powered by <span className="font-semibold">OpenAI GPT</span>, 
            <span className="font-semibold"> Google Gemini</span>, and 
            <span className="font-semibold"> Anthropic Claude</span>
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
