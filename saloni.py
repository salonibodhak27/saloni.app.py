import streamlit as st
import hashlib
import time

# RechargeRecord class
class RechargeRecord:
    def __init__(self, mobile_number, amount, previous_hash='0'):
        self.timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.mobile_number = mobile_number
        self.amount = amount
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        data = f'{self.timestamp}{self.mobile_number}{self.amount}{self.previous_hash}'
        return hashlib.sha256(data.encode()).hexdigest()

# Initialize session state for ledger
if 'ledger' not in st.session_state:
    st.session_state.ledger = []

# Add record function
def add_record(mobile_number, amount):
    previous_hash = st.session_state.ledger[-1].hash if st.session_state.ledger else '0'
    new_record = RechargeRecord(mobile_number, amount, previous_hash)
    st.session_state.ledger.append(new_record)

# Streamlit UI
st.title("📱 Mobile Recharge Ledger (with Hashing)")

with st.form("recharge_form"):
    mobile_number = st.text_input("Enter Mobile Number", max_chars=10)
    amount = st.number_input("Recharge Amount (₹)", min_value=1, step=1)
    submitted = st.form_submit_button("Add Recharge")

    if submitted:
        if len(mobile_number) == 10 and mobile_number.isdigit():
            add_record(mobile_number, amount)
            st.success("Recharge record added!")
        else:
            st.error("Invalid mobile number. Please enter a 10-digit number.")

# Display Ledger
st.header("🔗 Recharge Ledger")
for i, record in enumerate(st.session_state.ledger, start=1):
    with st.expander(f"Record #{i} | ₹{record.amount} to {record.mobile_number}"):
        st.text(f"Timestamp   : {record.timestamp}")
        st.text(f"Mobile No.  : {record.mobile_number}")
        st.text(f"Amount      : ₹{record.amount}")
        st.text(f"Hash        : {record.hash}")
        st.text(f"Prev Hash   : {record.previous_hash}")
