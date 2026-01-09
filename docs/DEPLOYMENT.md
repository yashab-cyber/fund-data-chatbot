# Deployment Guide
## Fund Data Chatbot

This guide covers deploying the Fund Data Chatbot to production environments.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Backend Deployment](#backend-deployment)
3. [Frontend Deployment](#frontend-deployment)
4. [Environment Variables](#environment-variables)
5. [Reverse Proxy Setup](#reverse-proxy-setup)
6. [Monitoring](#monitoring)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- Linux server (Ubuntu 20.04+ recommended)
- Python 3.9+
- Node.js 18+
- Nginx or Apache (for reverse proxy)
- Domain name (optional but recommended)
- SSL certificate (Let's Encrypt recommended)

---

## Backend Deployment

### Option 1: Using Gunicorn (Linux/Mac)

1. **Install Gunicorn**:
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn**:
   ```bash
   cd backend
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Create systemd service** (`/etc/systemd/system/fundbot-api.service`):
   ```ini
   [Unit]
   Description=Fund Data Chatbot API
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/var/www/fund-data-chatbot/backend
   Environment="PATH=/var/www/fund-data-chatbot/backend/venv/bin"
   ExecStart=/var/www/fund-data-chatbot/backend/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app

   [Install]
   WantedBy=multi-user.target
   ```

4. **Enable and start service**:
   ```bash
   sudo systemctl enable fundbot-api
   sudo systemctl start fundbot-api
   sudo systemctl status fundbot-api
   ```

### Option 2: Using Waitress (Windows)

1. **Install Waitress**:
   ```bash
   pip install waitress
   ```

2. **Run with Waitress**:
   ```bash
   cd backend
   waitress-serve --host=0.0.0.0 --port=5000 app:app
   ```

---

## Frontend Deployment

### Build Production Files

1. **Build the frontend**:
   ```bash
   cd frontend
   npm run build
   ```

2. **Output directory**: `frontend/dist/`

### Deployment Options

#### Option 1: Nginx

1. **Copy build files**:
   ```bash
   sudo cp -r dist/* /var/www/fund-data-chatbot/
   ```

2. **Nginx configuration** (`/etc/nginx/sites-available/fundbot`):
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       root /var/www/fund-data-chatbot;
       index index.html;

       # Frontend
       location / {
           try_files $uri $uri/ /index.html;
       }

       # API proxy
       location /api/ {
           proxy_pass http://127.0.0.1:5000/api/;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }

       location /health {
           proxy_pass http://127.0.0.1:5000/health;
       }
   }
   ```

3. **Enable site**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/fundbot /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl reload nginx
   ```

#### Option 2: Apache

1. **Apache configuration**:
   ```apache
   <VirtualHost *:80>
       ServerName yourdomain.com
       DocumentRoot /var/www/fund-data-chatbot

       <Directory /var/www/fund-data-chatbot>
           Options -Indexes +FollowSymLinks
           AllowOverride All
           Require all granted
       </Directory>

       ProxyPass /api/ http://127.0.0.1:5000/api/
       ProxyPassReverse /api/ http://127.0.0.1:5000/api/
       
       ProxyPass /health http://127.0.0.1:5000/health
       ProxyPassReverse /health http://127.0.0.1:5000/health

       ErrorLog ${APACHE_LOG_DIR}/fundbot_error.log
       CustomLog ${APACHE_LOG_DIR}/fundbot_access.log combined
   </VirtualHost>
   ```

---

## Environment Variables

### Backend (.env)

```env
# Production settings
OPENAI_API_KEY=your_production_key
GEMINI_API_KEY=your_production_key
ANTHROPIC_API_KEY=your_production_key

PORT=5000
DEBUG=False

# Security
ALLOWED_ORIGINS=https://yourdomain.com
```

### Frontend (.env)

```env
VITE_API_URL=https://yourdomain.com
```

---

## SSL/HTTPS Setup

### Using Let's Encrypt (Certbot)

1. **Install Certbot**:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   ```

2. **Obtain certificate**:
   ```bash
   sudo certbot --nginx -d yourdomain.com
   ```

3. **Auto-renewal**:
   ```bash
   sudo certbot renew --dry-run
   ```

---

## Monitoring

### Backend Logs

```bash
# Systemd logs
sudo journalctl -u fundbot-api -f

# Application logs
tail -f /var/www/fund-data-chatbot/backend/logs/app.log
```

### Nginx Logs

```bash
# Access logs
tail -f /var/log/nginx/access.log

# Error logs
tail -f /var/log/nginx/error.log
```

### Health Checks

Set up monitoring for:
- `GET /health` - API health
- Response time metrics
- Error rates

---

## Performance Optimization

### Backend

1. **Increase Gunicorn workers**:
   ```bash
   gunicorn -w 8 -b 127.0.0.1:5000 app:app
   ```

2. **Add caching** (Redis recommended)

3. **Database connection pooling** (if using database)

### Frontend

1. **Enable gzip compression** in Nginx:
   ```nginx
   gzip on;
   gzip_types text/css application/javascript application/json;
   ```

2. **Add caching headers**:
   ```nginx
   location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
       expires 1y;
       add_header Cache-Control "public, immutable";
   }
   ```

---

## Security Best Practices

1. **Firewall**: Only allow ports 80, 443, and 22
2. **API Keys**: Use environment variables, never commit to git
3. **Rate Limiting**: Implement Flask-Limiter
4. **Input Validation**: Already implemented in backend
5. **CORS**: Configure allowed origins properly
6. **HTTPS**: Always use SSL in production
7. **Regular Updates**: Keep dependencies updated

---

## Backup Strategy

1. **Database backups** (if using database)
2. **Environment files**: Backup `.env` files securely
3. **Application code**: Use git for version control
4. **CSV data files**: Regular backups of holdings.csv and trades.csv

---

## Troubleshooting

### Backend won't start
```bash
# Check logs
sudo journalctl -u fundbot-api -n 50

# Test manually
cd /var/www/fund-data-chatbot/backend
source venv/bin/activate
python app.py
```

### Frontend shows blank page
```bash
# Check Nginx configuration
sudo nginx -t

# Check file permissions
ls -la /var/www/fund-data-chatbot/

# Check browser console for errors
```

### API connection errors
```bash
# Test API directly
curl http://localhost:5000/health

# Check if service is running
sudo systemctl status fundbot-api

# Check firewall
sudo ufw status
```

---

## Scaling

For high-traffic scenarios:

1. **Load Balancer**: Use Nginx or HAProxy
2. **Multiple Backend Instances**: Run multiple Gunicorn instances
3. **CDN**: Use CloudFlare or AWS CloudFront for static assets
4. **Database**: Move to PostgreSQL for better performance
5. **Caching**: Implement Redis for response caching
6. **Message Queue**: Add Celery for async processing

---

## Maintenance

### Regular Tasks

- Update dependencies monthly
- Review logs weekly
- Monitor API key usage
- Check disk space
- Update SSL certificates (auto with Certbot)

### Updates

```bash
# Backend updates
cd backend
git pull
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart fundbot-api

# Frontend updates
cd frontend
git pull
npm install
npm run build
sudo cp -r dist/* /var/www/fund-data-chatbot/
```
