import streamlit as st
import dotenv
import os
import logging
from check_eligibility import get_recommendation

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Please set the GEMINI_API_KEY environment variable.")
    st.stop()

st.title("Loan Eligibility Checker")

st.sidebar.header("Enter Loan Details")

income = st.sidebar.number_input("Income", min_value=0, step=1000)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0, step=1000)
loan_type = st.sidebar.selectbox("Loan Type", ["Home Loan", "Car Loan", "Personal Loan", "Education Loan"])
credit_score = st.sidebar.slider("Credit Score", min_value=300, max_value=850, step=1)

if st.sidebar.button("Check Eligibility"):
    try:
        recommendation = get_recommendation(income, loan_amount, loan_type, credit_score)
        
        st.subheader("Eligibility Result")
        st.subheader("Eligible" if recommendation["is_eligible"] else "Not eligible")
        st.write(recommendation["recommendation"])
    except Exception as e:
        logging.error(f"Error checking eligibility: {e}")
        st.error("An error occurred while checking eligibility.")
