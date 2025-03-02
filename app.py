import streamlit as st
import Dashboard.dashboard as dashboard

# Top section: Branding
st.title("FELIXAN")
st.write("User: Admin | Contact: admin@felixan.com")

# Navigation bar with buttons (only Dashboard for now)
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6, nav_col7, nav_col8, nav_col9 = st.columns(9)
with nav_col1:
    if st.button("Dashboard"):
        st.session_state.current_module = "Dashboard"

# Initialize session state
if 'current_module' not in st.session_state:
    st.session_state.current_module = "Dashboard"

# Content area (Stage 3 split into status and content)
content_container = st.container()
with content_container:
    st.markdown("---")
    status_container = st.container()
    module_container = st.container()

# Module display logic (only Dashboard for now)
module_map = {
    "Dashboard": dashboard.show_dashboard
}

current_module = st.session_state.current_module
module_func = module_map.get(current_module, dashboard.show_dashboard)
status_container.write(f"### {current_module}")
module_func(module_container)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.write("© 2025 FELIXAN | Contact: support@felixan.com | Terms & Privacy")
