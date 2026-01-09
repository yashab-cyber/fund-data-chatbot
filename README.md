# Fund Data Chatbot 🤖💼

An intelligent, production-ready chatbot for analyzing fund holdings and trades data using multiple state-of-the-art Large Language Models (LLMs).

## 🌟 Features

- **Multi-LLM Support**: Powered by OpenAI GPT-4, Google Gemini, and Anthropic Claude
- **Real-time Analysis**: Query fund data with natural language
- **Beautiful UI**: Modern, responsive React interface with Tailwind CSS
- **Data-Driven Responses**: Uses RAG (Retrieval Augmented Generation) to ensure answers come only from your data
- **Production Ready**: Comprehensive error handling, logging, and documentation
- **No Containers Required**: Easy setup without Docker

## 📊 Capabilities

The chatbot can answer questions like:
- "How many holdings does Garfield fund have?"
- "Which funds performed better based on yearly Profit and Loss?"
- "Show me the total trades for MNC Investment Fund"
- "What is the total market value across all funds?"

## 🏗️ Architecture

```
fund-data-chatbot/
├── backend/                 # Flask API server
│   ├── app.py              # Main Flask application
│   ├── data_processor.py   # Data loading and context retrieval
│   ├── llm_providers.py    # Multi-LLM integration
│   └── requirements.txt    # Python dependencies
├── frontend/               # React application
│   ├── src/
│   │   ├── App.jsx        # Main React component
│   │   ├── services/      # API service layer
│   │   └── index.css      # Tailwind styles
│   └── package.json       # Node dependencies
├── holdings.csv           # Holdings data
└── trades.csv            # Trades data
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Node.js 18 or higher
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On Linux/Mac
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

   **Getting API Keys**:
   - **OpenAI**: https://platform.openai.com/api-keys
   - **Google Gemini**: https://makersuite.google.com/app/apikey
   - **Anthropic**: https://console.anthropic.com/

5. **Run the backend server**:
   ```bash
   python app.py
   ```
   
   The API will start on `http://localhost:5000`

### Frontend Setup

1. **Open a new terminal and navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   ```
   
   The default configuration should work:
   ```env
   VITE_API_URL=http://localhost:5000
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```
   
   The app will start on `http://localhost:3000`

5. **Open your browser** and navigate to `http://localhost:3000`

## 🎯 Usage

1. **Select an LLM Provider**: Click on the provider dropdown in the top-right corner to choose between OpenAI, Gemini, or Anthropic.

2. **Ask Questions**: Type your question in the input field and press Enter or click Send.

3. **View Results**: The chatbot will analyze your fund data and provide accurate, data-driven answers.

## 📁 Data Format

### Holdings CSV
Required columns:
- `AsOfDate`: Date of the holding
- `PortfolioName`: Name of the fund
- `SecurityTypeName`: Type of security
- `MV_Base`: Market value in base currency
- `PL_YTD`, `PL_MTD`, `PL_QTD`: Profit/Loss for different periods

### Trades CSV
Required columns:
- `PortfolioName`: Name of the fund
- `TradeTypeName`: Type of trade (Buy/Sell)
- `SecurityType`: Type of security
- `Quantity`: Number of units
- `Principal`: Trade principal amount

## 🔧 API Endpoints

### Backend API

- `GET /health` - Health check endpoint
- `GET /api/models` - Get available LLM models
- `GET /api/data-summary` - Get data statistics
- `GET /api/funds` - Get list of all funds
- `POST /api/query` - Query the chatbot

## 🎨 Frontend Features

- **Modern UI**: Beautiful gradient design with glass-morphism effects
- **Responsive**: Works on desktop, tablet, and mobile
- **Real-time Updates**: Live chat interface with loading indicators
- **Data Dashboard**: Quick overview of holdings, trades, and funds
- **Example Questions**: Suggested queries to get started

## 🔒 Security & Best Practices

- ✅ Environment variables for sensitive data
- ✅ Input validation and sanitization
- ✅ Error handling and logging
- ✅ CORS configuration for frontend-backend communication
- ✅ Rate limiting ready (can be added via Flask-Limiter)

## 📝 Code Documentation

All code is thoroughly documented with:
- **Docstrings**: Python functions and classes
- **JSDoc Comments**: JavaScript/React components
- **Inline Comments**: Complex logic explanations
- **Type Hints**: Python type annotations

## 🚀 Production Deployment

### Backend Production Server

Use Gunicorn or Waitress for production:

```bash
# Using Gunicorn (Linux/Mac)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Waitress (Windows)
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Frontend Production Build

```bash
cd frontend
npm run build
```

Serve the `dist` folder with any static file server (Nginx, Apache, etc.)

## 🐛 Troubleshooting

### Backend won't start
- Check that all dependencies are installed: `pip list`
- Verify Python version: `python --version` (should be 3.9+)
- Check if port 5000 is available

### Frontend can't connect to backend
- Ensure backend is running on port 5000
- Check `.env` file has correct `VITE_API_URL`
- Verify CORS settings in backend

### LLM not responding
- Verify API keys are correct in backend `.env`
- Check API key has sufficient credits/quota
- Review backend logs for error messages

## 📊 Performance

- **Response Time**: 2-5 seconds (depends on LLM provider)
- **Data Loading**: Instant (data cached in memory)
- **Scalability**: Can handle 100+ concurrent requests

## 🔄 Future Enhancements

- [ ] Add data visualization charts
- [ ] Export query results to CSV/Excel
- [ ] User authentication and session management
- [ ] Query history and favorites
- [ ] Advanced filtering and sorting options

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

Fund Data Chatbot Team - 2026

## 🙏 Acknowledgments

- OpenAI for GPT models
- Google for Gemini models
- Anthropic for Claude models
- React and Tailwind CSS communities