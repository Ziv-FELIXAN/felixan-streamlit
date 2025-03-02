import streamlit as st

def show_loans_management(container):
    with container:
        st.write("Status: Total Loans - 0")
        st.text_input("Loan Amount")
        st.button("Issue Loan")
