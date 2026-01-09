# Development Guide
## Fund Data Chatbot

Complete guide for developers working on the Fund Data Chatbot project.

---

## Project Structure

```
fund-data-chatbot/
│
├── backend/                          # Flask API Backend
│   ├── app.py                       # Main Flask application
│   ├── data_processor.py            # Data loading and context retrieval
│   ├── llm_providers.py             # Multi-LLM integration
│   ├── requirements.txt             # Python dependencies
│   ├── .env.example                 # Environment variables template
│   ├── .gitignore                   # Git ignore rules
│   ├── setup.sh                     # Linux/Mac setup script
│   └── setup.bat                    # Windows setup script
│
├── frontend/                        # React Frontend
│   ├── src/
│   │   ├── App.jsx                 # Main React component
│   │   ├── main.jsx                # React entry point
│   │   ├── index.css               # Tailwind CSS styles
│   │   └── services/
│   │       └── api.js              # API service layer
│   ├── public/                      # Static assets
│   ├── index.html                   # HTML template
│   ├── package.json                 # Node dependencies
│   ├── vite.config.js               # Vite configuration
│   ├── tailwind.config.js           # Tailwind CSS configuration
│   ├── postcss.config.js            # PostCSS configuration
│   ├── .env.example                 # Environment variables template
│   ├── .gitignore                   # Git ignore rules
│   ├── setup.sh                     # Linux/Mac setup script
│   └── setup.bat                    # Windows setup script
│
├── docs/                            # Documentation
│   ├── API.md                       # API documentation
│   ├── DEPLOYMENT.md                # Deployment guide
│   └── DEVELOPMENT.md               # This file
│
├── holdings.csv                     # Holdings data
├── trades.csv                       # Trades data
└── README.md                        # Main documentation

```

---

## Technology Stack

### Backend
- **Framework**: Flask 3.0
- **Language**: Python 3.9+
- **Data Processing**: Pandas, NumPy
- **LLM APIs**:
  - OpenAI (GPT-4, GPT-3.5)
  - Google Gemini
  - Anthropic Claude
- **CORS**: Flask-CORS

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite 5
- **Styling**: Tailwind CSS 3
- **Icons**: Lucide React
- **HTTP Client**: Axios
- **Markdown**: React Markdown

---

## Development Setup

### Backend Development

1. **Setup environment**:
   ```bash
   cd backend
   ./setup.sh  # or setup.bat on Windows
   ```

2. **Activate virtual environment**:
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Run in development mode**:
   ```bash
   export DEBUG=True  # Linux/Mac
   set DEBUG=True     # Windows
   python app.py
   ```

4. **Run tests** (if implemented):
   ```bash
   pytest
   ```

### Frontend Development

1. **Setup environment**:
   ```bash
   cd frontend
   ./setup.sh  # or setup.bat on Windows
   ```

2. **Run development server**:
   ```bash
   npm run dev
   ```

3. **Build for production**:
   ```bash
   npm run build
   ```

4. **Preview production build**:
   ```bash
   npm run preview
   ```

---

## Code Style & Standards

### Python (Backend)

- **Style Guide**: PEP 8
- **Docstrings**: Google-style docstrings
- **Type Hints**: Use type hints for function parameters and returns
- **Formatting**: Black (recommended)
- **Linting**: Flake8 or Pylint

Example:
```python
def get_fund_performance(self, fund_name: Optional[str] = None) -> Dict[str, Any]:
    """
    Calculate fund performance metrics.
    
    Args:
        fund_name: Specific fund to analyze (None for all funds)
    
    Returns:
        Dictionary with performance metrics
    """
    # Implementation here
    pass
```

### JavaScript/React (Frontend)

- **Style Guide**: Airbnb JavaScript Style Guide
- **Component Structure**: Functional components with hooks
- **Prop Types**: JSDoc comments for documentation
- **Formatting**: Prettier (recommended)
- **Linting**: ESLint

Example:
```javascript
/**
 * Query the chatbot with a question
 * 
 * @param {string} question - The user's question
 * @param {string} provider - LLM provider
 * @returns {Promise<Object>} Response object
 */
export const queryChatbot = async (question, provider) => {
  // Implementation here
};
```

---

## Adding New Features

### Adding a New LLM Provider

1. **Update `llm_providers.py`**:
   ```python
   def query_new_provider(question: str, context: str, model: Optional[str] = None) -> str:
       """Query new LLM provider."""
       # Implementation
       pass
   ```

2. **Add to MODELS_CONFIG**:
   ```python
   MODELS_CONFIG['new_provider'] = {
       'models': [...],
       'default': 'model-name'
   }
   ```

3. **Update frontend** to include new provider in dropdown

### Adding a New API Endpoint

1. **Add route in `app.py`**:
   ```python
   @app.route('/api/new-endpoint', methods=['POST'])
   def new_endpoint():
       """Endpoint description."""
       try:
           # Implementation
           return jsonify({'success': True, 'data': data})
       except Exception as e:
           return jsonify({'success': False, 'error': str(e)}), 500
   ```

2. **Add service method in `frontend/src/services/api.js`**:
   ```javascript
   export const newEndpointCall = async (params) => {
     const response = await apiClient.post('/api/new-endpoint', params);
     return response.data;
   };
   ```

3. **Update documentation** in `docs/API.md`

---

## Testing

### Backend Testing

Create `backend/tests/` directory:

```python
# test_data_processor.py
import pytest
from data_processor import DataProcessor

def test_load_data():
    processor = DataProcessor()
    assert processor.data_loaded == True
    
def test_get_unique_funds():
    processor = DataProcessor()
    funds = processor.get_unique_funds()
    assert len(funds) > 0
```

Run tests:
```bash
pytest backend/tests/
```

### Frontend Testing

Add testing libraries:
```bash
npm install --save-dev @testing-library/react @testing-library/jest-dom vitest
```

Create `frontend/src/__tests__/` directory and add tests.

---

## Debugging

### Backend Debugging

1. **Enable debug mode**:
   ```python
   # In app.py
   app.run(debug=True)
   ```

2. **Add logging**:
   ```python
   import logging
   logger = logging.getLogger(__name__)
   logger.debug("Debug message")
   ```

3. **Use Python debugger**:
   ```python
   import pdb; pdb.set_trace()
   ```

### Frontend Debugging

1. **Browser DevTools**: Use React DevTools extension

2. **Console logging**:
   ```javascript
   console.log('Debug info:', data);
   ```

3. **Network tab**: Monitor API calls

---

## Performance Optimization

### Backend

1. **Caching**: Implement Redis for frequently accessed data
2. **Database**: Move to PostgreSQL for large datasets
3. **Async Processing**: Use Celery for long-running tasks
4. **Connection Pooling**: Reuse database connections

### Frontend

1. **Code Splitting**: Use React.lazy() for route-based splitting
2. **Memoization**: Use React.memo() and useMemo()
3. **Virtual Scrolling**: For large lists
4. **Image Optimization**: Compress and lazy-load images

---

## Common Issues & Solutions

### Issue: API key not working
**Solution**: Check .env file, ensure no extra spaces, restart server

### Issue: CORS errors
**Solution**: Update ALLOWED_ORIGINS in backend .env

### Issue: Slow LLM responses
**Solution**: Increase timeout, optimize context size, use faster models

### Issue: Out of memory
**Solution**: Reduce data batch size, implement pagination

---

## Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Commit changes**: `git commit -m 'Add new feature'`
4. **Push to branch**: `git push origin feature/new-feature`
5. **Submit Pull Request**

### Commit Message Format
```
type(scope): subject

body (optional)

footer (optional)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

---

## Useful Commands

### Backend
```bash
# Install new package
pip install package-name
pip freeze > requirements.txt

# Format code
black app.py

# Lint code
flake8 app.py

# Check types
mypy app.py
```

### Frontend
```bash
# Install new package
npm install package-name

# Update dependencies
npm update

# Audit security
npm audit

# Format code
npx prettier --write src/
```

---

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [OpenAI API](https://platform.openai.com/docs)
- [Anthropic API](https://docs.anthropic.com/)
- [Google Gemini API](https://ai.google.dev/)

---

## Getting Help

1. Check the documentation in `docs/`
2. Review existing issues on GitHub
3. Contact the development team
4. Submit a new issue with detailed description
