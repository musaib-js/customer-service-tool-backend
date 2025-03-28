import google.generativeai as genai
import dotenv
import os
import logging
from prompts import LOAN_ELIBILITY_CHECK_AND_RECOMMENDATION_PROMPT
import json

dotenv.load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def get_recommendation(income, loan_amount, loan_type, credit_score):
    try:
        logging.info(f"Checking loan eligibility for: {income}, {loan_amount}, {loan_type}, {credit_score}")
        prompt = LOAN_ELIBILITY_CHECK_AND_RECOMMENDATION_PROMPT.format(
            income=income, loan_amount=loan_amount, loan_type=loan_type, credit_score=credit_score
        )
        response = model.generate_content(prompt)
        response = response.text.strip().replace("```json", "").replace("```", "")
        response = json.loads(response)
        return response 
    except Exception as e:
        logging.error(f"Error checking loan eligibility: {e}")
        return {"is_eligible": False, "recommendation": "Unclear"}