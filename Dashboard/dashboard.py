import streamlit as st

def show_dashboard(container):
    with container:
        st.write("Status: System Online")
        st.text_input("Dashboard Info")
        st.button("Refresh Dashboard")
