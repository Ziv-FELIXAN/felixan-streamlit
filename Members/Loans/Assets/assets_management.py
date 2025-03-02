import streamlit as st

def show_assets_management(container):
    with container:
        st.write("Status: Total Assets - 0")
        st.text_input("Asset Name")
        st.button("Register Asset")
