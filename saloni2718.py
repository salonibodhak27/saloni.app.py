import streamlit as st
import pandas as pd
import os

# Streamlit app title
st.title("User Data Entry Form")

# Collect user inputs
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
comments = st.text_area("Any additional comments?")

# Submit button
if st.button("Submit"):
    if name and email:
        # Create a DataFrame with the input
        new_data = pd.DataFrame({
            "Name": [name],
            "Email": [email],
            "Age": [age],
            "Gender": [gender],
            "Comments": [comments]
        })

        file_path = "user_data.csv"

        # Save to CSV file
        if os.path.exists(file_path):
            new_data.to_csv(file_path, mode='a', header=False, index=False)
        else:
            new_data.to_csv(file_path, index=False)

        st.success("Your data has been saved successfully!")
    else:
        st.warning("Please fill in at least your name and email.")
