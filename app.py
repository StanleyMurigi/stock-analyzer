from flask import Flask, request, jsonify
from services.stock_service import fetch_stock_data, summarize_stock
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Stock Summary Agent is running"})


@app.route("/stock-summary", methods=["POST"])
def stock_summary():
    try:
        payload = request.get_json(force=True)
        message = payload.get("message", "").strip()

        if not message:
            return jsonify({"error": "Missing message"}), 400

        # Extract stock symbol (e.g., "Check AAPL" → "AAPL")
        parts = message.split()
        symbol = parts[-1].upper() if len(parts) > 1 else parts[0].upper()

        # Fetch and summarize stock data
        data = fetch_stock_data(symbol)
        summary = summarize_stock(symbol, data)

        # Return in Telex-readable JSON
        return jsonify({"response": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

