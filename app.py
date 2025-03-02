import streamlit as st
import Members.members_management as members
import Loans.loans_management as loans
import Assets.assets_management as assets
import Contracts.contracts_management as contracts
import Carat.carat_management as carat
import Insurance.insurance_management as insurance
import TransactionsAudit.transactions_audit_management as audit
import SecureTransport.secure_transport_management as transport
import Dashboard.dashboard as dashboard

# Top section: Branding
st.title("FELIXAN")
st.write("User: Admin | Contact: admin@felixan.com")

# Navigation bar with buttons
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6, nav_col7, nav_col8, nav_col9 = st.columns(9)
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
with nav_col5:
    if st.button("Contracts"):
        st.session_state.current_module = "Contracts"
with nav_col6:
    with st.container():
        if st.button("Carat"):
            st.session_state.current_module = "Carat"
        carat_option = st.selectbox("Carat Options", ["Token Minting", "Transactions"], key="carat_dropdown")
with nav_col7:
    if st.button("Insurance"):
        st.session_state.current_module = "Insurance"
with nav_col8:
    if st.button("Transactions Audit"):
        st.session_state.current_module = "Transactions Audit"
with nav_col9:
    if st.button("Secure Transport"):
        st.session_state.current_module = "Secure Transport"

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
    "Assets": assets.show_assets_management,
    "Contracts": contracts.show_contracts_management,
    "Carat": carat.show_carat_management,
    "Insurance": insurance.show_insurance_management,
    "Transactions Audit": audit.show_transactions_audit_management,
    "Secure Transport": transport.show_secure_transport_management
}

current_module = st.session_state.current_module
module_func = module_map.get(current_module, dashboard.show_dashboard)
status_container.write(f"### {current_module}")
module_func(module_container)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.write("© 2025 FELIXAN | Contact: support@felixan.com | Terms & Privacy")
