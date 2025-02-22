import streamlit as st
import joblib
import numpy as np

# Load the saved Random Forest model
model = joblib.load('random_forest_model.pkl')

# Title and description
st.title("💳 Online Payment Fraud Detection")
st.write("Enter transaction details below to predict whether the transaction is fraudulent or not.")

# Input fields for the transaction details
step = st.number_input("Step (Time step of the transaction)", min_value=1)
amount = st.number_input("Transaction Amount", min_value=0.0)
nameOrig = st.number_input("Origin Account ID (numerical representation)", min_value=0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
nameDest = st.number_input("Destination Account ID (numerical representation)", min_value=0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)
isFlaggedFraud = st.checkbox("Is Flagged Fraud (1 if yes, 0 if no)")

# Transaction type selection
st.write("Transaction Type:")
type_CASH_OUT = st.checkbox("CASH_OUT")
type_DEBIT = st.checkbox("DEBIT")
type_PAYMENT = st.checkbox("PAYMENT")
type_TRANSFER = st.checkbox("TRANSFER")

# Prediction
if st.button("🔍 Predict"):
    # Prepare input data in the correct format (13 features)
    input_data = np.array([[
        step, amount, nameOrig, oldbalanceOrg, newbalanceOrig,
        nameDest, oldbalanceDest, newbalanceDest, int(isFlaggedFraud),
        int(type_CASH_OUT), int(type_DEBIT), int(type_PAYMENT), int(type_TRANSFER)
    ]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1:
        st.error("🚨 This transaction is FRAUDULENT!")
    else:
        st.success("✅ This transaction is NOT fraudulent.")
