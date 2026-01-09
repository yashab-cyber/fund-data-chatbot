# Quick Start Guide 🚀
## Fund Data Chatbot - Get Started in 5 Minutes

---

## Prerequisites Checklist

- [ ] Python 3.9+ installed ([Download](https://www.python.org/downloads/))
- [ ] Node.js 18+ installed ([Download](https://nodejs.org/))
- [ ] At least ONE API key from:
  - [ ] OpenAI ([Get Key](https://platform.openai.com/api-keys))
  - [ ] Google Gemini ([Get Key](https://makersuite.google.com/app/apikey))
  - [ ] Anthropic ([Get Key](https://console.anthropic.com/))

---

## Step 1: Backend Setup (2 minutes)

### Linux/Mac
```bash
cd backend
./setup.sh
```

### Windows
```cmd
cd backend
setup.bat
```

### Configure API Keys
Edit `backend/.env` and add at least one API key:
```env
OPENAI_API_KEY=sk-your-key-here
# OR
GEMINI_API_KEY=your-key-here
# OR
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### Start Backend
```bash
# Linux/Mac
source venv/bin/activate
python app.py

# Windows
venv\Scripts\activate
python app.py
```

✅ Backend should now be running on http://localhost:5000

---

## Step 2: Frontend Setup (2 minutes)

### Open a NEW terminal window

### Linux/Mac
```bash
cd frontend
./setup.sh
```

### Windows
```cmd
cd frontend
setup.bat
```

### Start Frontend
```bash
npm run dev
```

✅ Frontend should now be running on http://localhost:3000

---

## Step 3: Use the Chatbot (1 minute)

1. **Open browser**: Go to http://localhost:3000

2. **Select LLM provider**: Click dropdown in top-right corner

3. **Ask a question**:
   - "How many holdings does Garfield fund have?"
   - "Which funds performed better based on yearly P&L?"
   - "Show me total trades"

4. **Get AI-powered answers** based on your fund data!

---

## Verification Checklist

✅ Backend is running (check http://localhost:5000/health)  
✅ Frontend is accessible (http://localhost:3000)  
✅ Can select LLM provider  
✅ Chatbot responds to questions  
✅ Data summary shows in sidebar  

---

## Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version  # Should be 3.9+

# Check if port 5000 is already in use
# Linux/Mac: lsof -i :5000
# Windows: netstat -ano | findstr :5000
```

### Frontend won't start
```bash
# Check Node version
node --version  # Should be 18+

# Try deleting node_modules and reinstalling
rm -rf node_modules
npm install
```

### API Key Errors
- Make sure there are no spaces around the `=` sign in .env
- Restart the backend server after changing .env
- Check if API key has available credits/quota

### Can't connect to backend
- Ensure backend is running on port 5000
- Check frontend/.env has `VITE_API_URL=http://localhost:5000`
- Check browser console for CORS errors

---

## Next Steps

📚 **Read the full documentation**: [README.md](../README.md)  
🔧 **API Documentation**: [docs/API.md](API.md)  
🚀 **Deploy to production**: [docs/DEPLOYMENT.md](DEPLOYMENT.md)  
💻 **Start developing**: [docs/DEVELOPMENT.md](DEVELOPMENT.md)  

---

## Example Questions to Try

### Basic Queries
- "How many holdings are there in total?"
- "List all funds in the data"
- "How many trades were executed?"

### Fund-Specific
- "Show me holdings for Garfield fund"
- "What are the trades for MNC Investment Fund?"
- "Tell me about Heather fund"

### Performance Analysis
- "Which funds have the highest yearly profit?"
- "Compare performance of Garfield vs Heather"
- "Show funds with negative P&L"
- "What is the best performing fund?"

### Statistics
- "What is the total market value?"
- "How many different securities are there?"
- "What types of trades were made?"

---

## Need Help?

- 📖 Check [README.md](../README.md) for detailed information
- 🐛 Found a bug? Create an issue
- 💡 Have a suggestion? We'd love to hear it!
- 📧 Contact the development team

---

## Quick Commands Reference

### Backend
```bash
# Start backend
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py

# Stop backend
Ctrl+C
```

### Frontend
```bash
# Start frontend
cd frontend
npm run dev

# Build for production
npm run build

# Stop frontend
Ctrl+C
```

---

**🎉 You're all set! Enjoy using the Fund Data Chatbot!**
