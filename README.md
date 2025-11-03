# 📈 Stock Summary AI Agent for Telex.im

A Flask-based AI Agent that fetches live stock market data and summarizes the recent performance of a given stock symbol in natural language.

---

## 🚀 Features
- Fetches daily stock data via Alpha Vantage API (https://www.alphavantage.co/documentation/).
- Generates human-readable summaries of stock performance.
- Integrates seamlessly with Telex.im using the A2A protocol.
- Example response:
  AAPL closed at $178.45 on 2025-11-03, down 0.34% from yesterday. The recent trend appears to be an uptrend.

---

## ⚙️ Setup

1. Clone the Project
   git clone https://github.com/yourusername/stock_summary_agent.git
   cd stock_summary_agent

2. Create Virtual Environment
   python3 -m venv venv
   source venv/bin/activate

3. Install Dependencies
   pip install -r requirements.txt

4. Set Environment Variables
   export ALPHA_VANTAGE_API_KEY="your_key_here"

---

## 🧪 Local Testing

Run the server:
   python app.py

Send a test request:
   curl -X POST http://127.0.0.1:5000/stock-summary \
        -H "Content-Type: application/json" \
        -d '{"message": "Check AAPL"}'

Expected response:
{
  "response": "AAPL closed at $178.45 on 2025-11-03, down 0.34% from yesterday. The recent trend appears to be an uptrend."
}

---

## 🌍 Deploy to Telex.im

Expose your Flask app via ngrok:
   ngrok http 5000

Copy your ngrok URL (e.g., https://abcd1234.ngrok.io) and add it to your Telex workflow.

Telex Agent Configuration:
id: stock_agent
name: Stock Summary Agent
type: a2a/mastra-a2a-node
url: https://abcd1234.ngrok.io/stock-summary
description: >
  A Flask-based AI agent that fetches and summarizes real-time stock performance data.
author: Your Name
version: 1.0.0

Then test via your channel logs:
   https://api.telex.im/agent-logs/{channel-id}.txt

---

## 📘 Notes
- Free API limits apply (5 requests/min for Alpha Vantage free plan).
- Add caching or database persistence if needed.
- For production, deploy to Render, Railway, or Google Cloud Run.

---

## 🧾 License
MIT License

---

## ✅ Quick Summary
1. Run the Flask app locally.  
2. Test using curl or Postman.  
3. Connect to Telex using ngrok.  
4. View logs in your Telex dashboard.

