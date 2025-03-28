from flask import Flask, request, jsonify
from flask_cors import CORS
import dotenv
import os
import logging
from check_eligibility import get_recommendation

dotenv.load_dotenv()

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Please set the GEMINI_API_KEY environment variable.")


@app.route("/check-eligibility", methods=["POST"])
def check_eligibility():
    try:
        data = request.json

        income = data["income"]
        loan_amount = data["loan_amount"]
        loan_type = data["loan_type"]
        credit_score = data["credit_score"]

        recommendation = get_recommendation(
            income, loan_amount, loan_type, credit_score
        )

        return jsonify(recommendation)
    except Exception as e:
        logging.error(f"Error checking eligibility: {e}")
        return jsonify({"is_eligible": False, "recommendation": "Unclear"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
