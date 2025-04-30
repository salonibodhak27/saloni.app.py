import streamlit as st
import pandas as pd
import os

st.title("User Input Form")

# Collecting user input
name = st.text_input("Name")
email = st.text_input("Email")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
comments = st.text_area("Additional Comments")

# Submit button
if st.button("Submit"):
    # Prepare data
    new_data = pd.DataFrame({
        "Name": [name],
        "Email": [email],
        "Age": [age],
        "Gender": [gender],
        "Comments": [comments]
    })

    # File path
    file_path = "user_inputs.csv"

    # Save to CSV (append if file exists)
    if os.path.exists(file_path):
        new_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_data.to_csv(file_path, index=False)

    st.success("Your input has been saved to CSV!")
