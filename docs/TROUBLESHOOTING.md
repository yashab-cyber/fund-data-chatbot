# Troubleshooting Guide
## Fund Data Chatbot - Common Issues & Solutions

---

## 🔍 Quick Diagnostics

### Is Everything Running?

Run these checks first:

1. **Backend Health**:
   ```bash
   curl http://localhost:5000/health
   ```
   Should return: `{"status": "healthy", ...}`

2. **Frontend Access**:
   - Open browser: http://localhost:3000
   - Should see the chatbot interface

3. **Check Logs**:
   - Backend: Look at terminal where you ran `python app.py`
   - Frontend: Check browser console (F12)

---

## ❌ Backend Issues

### Issue: Backend won't start

**Symptoms**: Error when running `python app.py`

**Solutions**:

1. **Check Python version**:
   ```bash
   python --version  # Should be 3.9 or higher
   ```

2. **Check if virtual environment is activated**:
   ```bash
   # You should see (venv) in your prompt
   # If not, activate it:
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Reinstall dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Check if port 5000 is in use**:
   ```bash
   # Linux/Mac
   lsof -i :5000
   
   # Windows
   netstat -ano | findstr :5000
   ```
   If port is busy, either:
   - Kill the process using the port
   - Change port in `.env`: `PORT=5001`

---

### Issue: ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solutions**:

1. Ensure virtual environment is activated
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

---

### Issue: API Key Errors

**Error**: `Error: OpenAI API key not configured`

**Solutions**:

1. **Check .env file exists**:
   ```bash
   ls -la .env  # Should show the file
   ```

2. **Verify .env format**:
   ```env
   # NO SPACES around =
   OPENAI_API_KEY=sk-your-key-here
   
   # NOT THIS:
   # OPENAI_API_KEY = sk-your-key-here  ❌
   ```

3. **Check API key is valid**:
   - OpenAI: https://platform.openai.com/api-keys
   - Verify key has credits/quota

4. **Restart backend** after changing .env:
   ```bash
   # Stop with Ctrl+C
   python app.py
   ```

---

### Issue: CSV Files Not Found

**Error**: `FileNotFoundError: holdings.csv not found`

**Solutions**:

1. **Ensure CSVs are in project root**:
   ```bash
   ls -la *.csv
   # Should show holdings.csv and trades.csv
   ```

2. **Check file paths in code** (if you moved CSVs):
   Edit `backend/data_processor.py` line ~50

3. **Verify file permissions**:
   ```bash
   chmod 644 holdings.csv trades.csv
   ```

---

## 🌐 Frontend Issues

### Issue: Frontend won't start

**Error**: `Error: Cannot find module`

**Solutions**:

1. **Check Node.js version**:
   ```bash
   node --version  # Should be 18 or higher
   ```

2. **Delete and reinstall dependencies**:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Clear cache**:
   ```bash
   npm cache clean --force
   npm install
   ```

---

### Issue: Blank page in browser

**Symptoms**: White screen, no UI visible

**Solutions**:

1. **Check browser console** (F12):
   - Look for error messages
   - Check Network tab for failed requests

2. **Verify frontend is running**:
   ```bash
   # Terminal should show:
   # VITE v5.0.11  ready in 500 ms
   # ➜  Local:   http://localhost:3000/
   ```

3. **Check build files**:
   ```bash
   npm run build
   npm run preview
   ```

4. **Clear browser cache**:
   - Hard refresh: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
   - Or use incognito mode

---

### Issue: Cannot connect to backend

**Error**: "Failed to get response from chatbot" or CORS errors

**Solutions**:

1. **Verify backend is running**:
   ```bash
   curl http://localhost:5000/health
   ```

2. **Check .env in frontend**:
   ```env
   VITE_API_URL=http://localhost:5000
   ```

3. **Verify CORS settings** in `backend/app.py`:
   ```python
   CORS(app)  # Should be present
   ```

4. **Check browser console** for specific CORS error

5. **Restart both servers**:
   ```bash
   # Stop both with Ctrl+C
   # Restart backend
   python app.py
   # Restart frontend
   npm run dev
   ```

---

## 🤖 LLM Issues

### Issue: "API key not configured"

**Error**: `Error: OpenAI API key not configured`

**Solutions**:

1. Add API key to `backend/.env`:
   ```env
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

2. Restart backend server

3. Try a different provider (Gemini or Anthropic)

---

### Issue: Slow responses

**Symptoms**: Takes 30+ seconds to respond

**Solutions**:

1. **Try a faster model**:
   - Use GPT-3.5 instead of GPT-4
   - Use Gemini Flash instead of Gemini Pro

2. **Reduce context size**:
   - Edit `data_processor.py`
   - Limit samples to top 5 instead of 10

3. **Check internet connection**:
   - LLM APIs require internet
   - Test: `ping api.openai.com`

---

### Issue: "Rate limit exceeded"

**Error**: `Error: Rate limit exceeded for API key`

**Solutions**:

1. **Wait a few minutes** and try again

2. **Upgrade API plan**:
   - OpenAI: https://platform.openai.com/account/billing
   - Check usage limits

3. **Switch to another provider**:
   - Use Gemini or Anthropic instead

---

### Issue: Incorrect or irrelevant answers

**Symptoms**: Bot gives wrong information

**Solutions**:

1. **Rephrase your question**:
   - Be more specific
   - Use exact fund names from data

2. **Check data files**:
   - Ensure holdings.csv and trades.csv have data
   - Verify column names are correct

3. **Try different LLM provider**:
   - Different models may interpret differently
   - Claude is good for careful reasoning

---

## 🔧 Development Issues

### Issue: Hot reload not working

**Symptoms**: Changes don't reflect without restart

**Solutions**:

**Backend**:
```bash
# Use Flask debug mode
export DEBUG=True  # Linux/Mac
set DEBUG=True     # Windows
python app.py
```

**Frontend**:
```bash
# Vite should auto-reload
# If not, restart dev server
npm run dev
```

---

### Issue: Import errors

**Error**: `ImportError: cannot import name 'X'`

**Solutions**:

1. **Check Python path**:
   ```bash
   which python  # Should point to venv
   ```

2. **Reinstall specific package**:
   ```bash
   pip install --force-reinstall package-name
   ```

---

## 💾 Data Issues

### Issue: "No relevant data found"

**Symptoms**: Bot says it can't find answers

**Solutions**:

1. **Check CSV files have data**:
   ```bash
   wc -l holdings.csv trades.csv
   # Should show line counts
   ```

2. **Verify data format**:
   - CSV files should have headers
   - Check for encoding issues

3. **Use exact fund names**:
   - Get list: http://localhost:5000/api/funds
   - Use names exactly as shown

---

### Issue: Data not loading

**Error**: `Error loading data`

**Solutions**:

1. **Check file permissions**:
   ```bash
   ls -la *.csv
   ```

2. **Verify CSV format**:
   - Open in spreadsheet software
   - Check for special characters

3. **Check backend logs** for specific error

---

## 🌍 Network Issues

### Issue: Cannot access frontend from other devices

**Symptoms**: Works on localhost but not from other computers

**Solutions**:

1. **Start Vite with --host**:
   ```bash
   npm run dev -- --host
   ```

2. **Find your IP address**:
   ```bash
   # Linux/Mac
   ifconfig | grep "inet "
   
   # Windows
   ipconfig
   ```

3. **Access using IP**:
   ```
   http://192.168.1.x:3000
   ```

4. **Check firewall settings**:
   - Allow port 3000 and 5000

---

## 🔐 Security Issues

### Issue: CORS errors in production

**Error**: `Access-Control-Allow-Origin error`

**Solutions**:

1. **Update backend/.env**:
   ```env
   ALLOWED_ORIGINS=https://yourdomain.com,http://localhost:3000
   ```

2. **Update Flask CORS config** in `app.py`:
   ```python
   CORS(app, origins=["https://yourdomain.com"])
   ```

3. **Restart backend server**

---

## 🐛 Common Error Messages

### "Connection refused"
- Backend is not running
- Check port 5000 is correct

### "504 Gateway Timeout"
- LLM API taking too long
- Increase timeout in `api.js`

### "Invalid JSON response"
- Backend returned error
- Check backend logs

### "Module not found"
- Missing dependency
- Run `pip install -r requirements.txt`

---

## 📊 Performance Issues

### Issue: High memory usage

**Solutions**:

1. **Reduce data samples**:
   - Edit `data_processor.py`
   - Limit DataFrame operations

2. **Use chunking**:
   ```python
   # Process data in chunks
   for chunk in pd.read_csv('file.csv', chunksize=1000):
       process(chunk)
   ```

---

## 🔄 Reset & Clean Install

If all else fails, try a clean install:

### Backend
```bash
cd backend
rm -rf venv
./setup.sh  # or setup.bat
# Re-add API keys to .env
python app.py
```

### Frontend
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

---

## 📞 Getting More Help

Still stuck? Try these:

1. **Check logs carefully**:
   - Backend terminal output
   - Browser console (F12)
   - Look for specific error messages

2. **Review documentation**:
   - [README.md](../README.md)
   - [QUICKSTART.md](QUICKSTART.md)
   - [DEVELOPMENT.md](DEVELOPMENT.md)

3. **Search for error messages**:
   - Google the specific error
   - Check Stack Overflow

4. **Create detailed issue report**:
   - OS and versions (Python, Node)
   - Exact error message
   - Steps to reproduce
   - What you've already tried

---

## ✅ Prevention Tips

### Best Practices

1. **Always use virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Keep dependencies updated**:
   ```bash
   pip install --upgrade pip
   pip list --outdated
   ```

3. **Check API key quotas regularly**:
   - Monitor usage on provider dashboards

4. **Test after changes**:
   - Make one change at a time
   - Test before moving to next change

5. **Use version control**:
   ```bash
   git status
   git diff
   ```

---

## 🎯 Quick Fixes Checklist

Before asking for help, try:

- [ ] Restart backend server
- [ ] Restart frontend dev server  
- [ ] Clear browser cache
- [ ] Check .env file format
- [ ] Verify API keys
- [ ] Check Python version (3.9+)
- [ ] Check Node version (18+)
- [ ] Ensure virtual env is activated
- [ ] Check both servers are running
- [ ] Look at error logs
- [ ] Try in incognito mode
- [ ] Test with curl/Postman

---

**Still need help? Don't hesitate to reach out! 🤝**
