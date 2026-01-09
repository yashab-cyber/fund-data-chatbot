# Project Structure Overview
## Fund Data Chatbot

```
fund-data-chatbot/
│
├── 📁 backend/                              # Backend API (Python/Flask)
│   ├── app.py                               # Main Flask application with API endpoints
│   ├── data_processor.py                    # Data loading, processing, and context retrieval
│   ├── llm_providers.py                     # Multi-LLM provider integration (OpenAI, Gemini, Anthropic)
│   ├── requirements.txt                     # Python dependencies
│   ├── .env.example                         # Environment variables template
│   ├── .gitignore                           # Git ignore rules for Python
│   ├── setup.sh                             # Setup script for Linux/Mac
│   └── setup.bat                            # Setup script for Windows
│
├── 📁 frontend/                             # Frontend UI (React/Vite)
│   ├── 📁 src/
│   │   ├── App.jsx                         # Main React component with chat UI
│   │   ├── main.jsx                        # React entry point
│   │   ├── index.css                       # Tailwind CSS custom styles
│   │   └── 📁 services/
│   │       └── api.js                      # API service layer (axios)
│   │
│   ├── index.html                          # HTML template
│   ├── package.json                        # Node.js dependencies and scripts
│   ├── vite.config.js                      # Vite build configuration
│   ├── tailwind.config.js                  # Tailwind CSS configuration
│   ├── postcss.config.js                   # PostCSS configuration
│   ├── .eslintrc.cjs                       # ESLint configuration
│   ├── .env.example                        # Environment variables template
│   ├── .gitignore                          # Git ignore rules for Node.js
│   ├── setup.sh                            # Setup script for Linux/Mac
│   └── setup.bat                           # Setup script for Windows
│
├── 📁 docs/                                 # Documentation
│   ├── API.md                              # Complete API documentation
│   ├── DEPLOYMENT.md                       # Production deployment guide
│   ├── DEVELOPMENT.md                      # Developer guide
│   └── QUICKSTART.md                       # Quick start guide (5 minutes)
│
├── 📄 holdings.csv                          # Fund holdings data (1023 rows)
├── 📄 trades.csv                            # Fund trades data (650 rows)
├── 📄 README.md                             # Main project documentation
└── 📄 project_structure.txt                 # This file

```

## File Count Summary

- **Backend Files**: 8 files
- **Frontend Files**: 12+ files
- **Documentation**: 4 files
- **Data Files**: 2 CSV files
- **Total Project Files**: 26+ core files

## Lines of Code (Approximate)

- **Backend Python**: ~1,200 lines
- **Frontend JavaScript/React**: ~800 lines
- **CSS/Styling**: ~300 lines
- **Documentation**: ~2,000 lines
- **Configuration**: ~200 lines
- **Total**: ~4,500+ lines

## Key Components

### Backend Architecture
1. **Flask API Server** (app.py)
   - RESTful endpoints
   - Error handling
   - CORS configuration
   - Health checks

2. **Data Processor** (data_processor.py)
   - CSV file loading
   - Data transformation
   - Context extraction
   - Fund analytics

3. **LLM Providers** (llm_providers.py)
   - OpenAI integration
   - Gemini integration
   - Anthropic integration
   - Unified interface

### Frontend Architecture
1. **React Application** (App.jsx)
   - Chat interface
   - Provider selection
   - Data dashboard
   - Real-time updates

2. **API Service** (api.js)
   - HTTP client
   - Request handling
   - Error management
   - Response parsing

3. **Styling** (Tailwind CSS)
   - Modern design
   - Responsive layout
   - Custom animations
   - Glass-morphism effects

## Technology Stack

### Backend
- **Framework**: Flask 3.0
- **Language**: Python 3.9+
- **Data**: Pandas, NumPy
- **LLMs**: OpenAI, Gemini, Anthropic
- **Server**: Gunicorn/Waitress

### Frontend
- **Framework**: React 18
- **Build**: Vite 5
- **Styling**: Tailwind CSS 3
- **HTTP**: Axios
- **Icons**: Lucide React
- **Markdown**: React Markdown

## Data Files

### holdings.csv
- **Rows**: 1,023
- **Columns**: 25
- **Key Fields**: 
  - AsOfDate, PortfolioName, SecurityTypeName
  - MV_Base, PL_YTD, PL_MTD, PL_QTD
  - Price, Quantity, FXRate

### trades.csv
- **Rows**: 650
- **Columns**: 31
- **Key Fields**:
  - TradeDate, TradeTypeName, PortfolioName
  - Quantity, Price, Principal
  - AllocationQTY, AllocationCash

## Quick Navigation

### 🚀 Getting Started
- [Quick Start Guide](docs/QUICKSTART.md) - Get running in 5 minutes
- [README.md](README.md) - Complete overview

### 📚 Documentation
- [API Documentation](docs/API.md) - All API endpoints
- [Development Guide](docs/DEVELOPMENT.md) - For developers
- [Deployment Guide](docs/DEPLOYMENT.md) - Production setup

### 🔧 Setup Scripts
- `backend/setup.sh` or `backend/setup.bat` - Backend setup
- `frontend/setup.sh` or `frontend/setup.bat` - Frontend setup

### 🎯 Main Entry Points
- `backend/app.py` - Start backend server
- `frontend/src/main.jsx` - Frontend entry
- `frontend/src/App.jsx` - Main UI component

## Features Implemented

✅ Multi-LLM support (OpenAI, Gemini, Anthropic)  
✅ Beautiful responsive React UI  
✅ Real-time chat interface  
✅ Data-driven responses (RAG)  
✅ Fund performance analysis  
✅ Holdings and trades queries  
✅ Comprehensive error handling  
✅ Production-ready code  
✅ Complete documentation  
✅ Setup automation scripts  
✅ Environment configuration  
✅ Security best practices  

## Dependencies

### Backend (Python)
- flask==3.0.0
- flask-cors==4.0.0
- pandas==2.1.4
- numpy==1.26.2
- openai==1.10.0
- anthropic==0.18.1
- google-generativeai==0.3.2
- python-dotenv==1.0.0
- gunicorn==21.2.0

### Frontend (Node.js)
- react==18.2.0
- react-dom==18.2.0
- vite==5.0.11
- tailwindcss==3.4.1
- axios==1.6.5
- lucide-react==0.309.0
- react-markdown==9.0.1

## Getting Help

- 📖 Read the [README.md](README.md)
- 🚀 Follow [QUICKSTART.md](docs/QUICKSTART.md)
- 💻 Check [DEVELOPMENT.md](docs/DEVELOPMENT.md)
- 🐛 Report issues on GitHub
- 📧 Contact the development team
