import streamlit as st
import Members.members_management as members
import Loans.loans_management as loans
import Assets.assets_management as assets
import Dashboard.dashboard as dashboard

# Top section: Branding
st.title("FELIXAN")
st.write("User: Admin | Contact: admin@felixan.com")

# Navigation bar with buttons
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
with nav_col1:
    if st.button("Dashboard"):
        st.session_state.current_module = "Dashboard"
with nav_col2:
    if st.button("Members"):
        st.session_state.current_module = "Members"
with nav_col3:
    if st.button("Loans"):
        st.session_state.current_module = "Loans"
with nav_col4:
    if st.button("Assets"):
        st.session_state.current_module = "Assets"

# Initialize session state
if 'current_module' not in st.session_state:
    st.session_state.current_module = "Dashboard"

# Content area (Stage 3 split into status and content)
with st.container():
    st.markdown("---")
    status_container = st.empty()  # Status area
    module_container = st.container()  # Module content area

# Module display logic
module_map = {
    "Dashboard": dashboard.show_dashboard,
    "Members": members.show_members_management,
    "Loans": loans.show_loans_management,
    "Assets": assets.show_assets_management
}

current_module = st.session_state.current_module
module_func = module_map.get(current_module, dashboard.show_dashboard)
status_container.write(f"### {current_module}")
module_func(module_container)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.write("© 2025 FELIXAN | Contact: support@felixan.com | Terms & Privacy")
