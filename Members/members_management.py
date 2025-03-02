import streamlit as st

def show_members_management(container):
    with container:
        st.write("Status: Active Members - 0")
        st.text_input("Member Name")
        st.button("Save Member")
