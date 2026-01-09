# API Documentation
## Fund Data Chatbot Backend API

### Base URL
```
http://localhost:5000
```

---

## Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Description:** Check if the API is running and healthy.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-01-09T12:00:00.000Z",
  "service": "Fund Data Chatbot API"
}
```

---

### 2. Get Available Models

**Endpoint:** `GET /api/models`

**Description:** Retrieve list of available LLM models for each provider.

**Response:**
```json
{
  "success": true,
  "models": {
    "openai": {
      "models": [
        {
          "id": "gpt-4",
          "name": "GPT-4",
          "description": "Most capable OpenAI model"
        }
      ],
      "default": "gpt-4"
    },
    "gemini": {
      "models": [...],
      "default": "gemini-pro"
    },
    "anthropic": {
      "models": [...],
      "default": "claude-3-5-sonnet-20241022"
    }
  }
}
```

---

### 3. Get Data Summary

**Endpoint:** `GET /api/data-summary`

**Description:** Get comprehensive summary of the fund data.

**Response:**
```json
{
  "success": true,
  "summary": {
    "holdings": {
      "total_records": 1023,
      "unique_funds": 15,
      "unique_securities": 8,
      "date_range": {
        "start": "01/08/23",
        "end": "01/08/23"
      },
      "total_market_value": 150000000.0,
      "columns": ["AsOfDate", "PortfolioName", ...]
    },
    "trades": {
      "total_records": 650,
      "unique_funds": 12,
      "trade_types": ["Buy", "Sell"],
      "total_principal": 50000000.0,
      "columns": ["id", "TradeTypeName", ...]
    },
    "funds": ["Garfield", "Heather", "MNC Investment Fund", ...],
    "data_loaded": true,
    "last_updated": "2026-01-09T12:00:00.000Z"
  }
}
```

---

### 4. Get Funds List

**Endpoint:** `GET /api/funds`

**Description:** Get list of all unique fund names.

**Response:**
```json
{
  "success": true,
  "funds": [
    "ClientA",
    "CoYold 1",
    "Garfield",
    "Heather",
    "HoldCo 1",
    "MNC Investment Fund",
    "Northpoint 401K",
    ...
  ]
}
```

---

### 5. Query Chatbot

**Endpoint:** `POST /api/query`

**Description:** Send a question to the chatbot and get an AI-powered response based on the fund data.

**Request Body:**
```json
{
  "question": "How many holdings does Garfield fund have?",
  "provider": "openai",
  "model": "gpt-4"
}
```

**Parameters:**
- `question` (string, required): The user's question about fund data
- `provider` (string, required): LLM provider - `"openai"`, `"gemini"`, or `"anthropic"`
- `model` (string, optional): Specific model to use (uses default if not provided)

**Response:**
```json
{
  "success": true,
  "answer": "Based on the data, Garfield fund has 123 holdings.",
  "context": "=== FUND DATA SUMMARY ===\n...",
  "provider": "openai",
  "model": "gpt-4",
  "timestamp": "2026-01-09T12:00:00.000Z"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message here"
}
```

---

## Error Codes

- `400 Bad Request`: Invalid input or missing required parameters
- `404 Not Found`: Endpoint not found
- `500 Internal Server Error`: Server error during processing

---

## Example Queries

### Count Holdings for a Fund
```json
{
  "question": "How many holdings does Garfield fund have?",
  "provider": "openai"
}
```

### Fund Performance Comparison
```json
{
  "question": "Which funds performed better based on yearly P&L?",
  "provider": "anthropic",
  "model": "claude-3-5-sonnet-20241022"
}
```

### Total Trades
```json
{
  "question": "Show me total trades for all funds",
  "provider": "gemini"
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production use, consider adding Flask-Limiter.

---

## Authentication

Currently no authentication is required. For production use, implement API key or OAuth authentication.
