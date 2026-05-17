import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="Email Threat Intelligence",

    page_icon="🛡️",

    layout="wide"
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title(
    "🛡️ Navigation"
)

page = st.sidebar.radio(

    "Go To",

    [

        "Dashboard",

        "Upload",

        "Analytics",

        "Monitoring"
    ]
)


# =========================================================
# DASHBOARD PAGE
# =========================================================

if page == "Dashboard":

    from pages.dashboard import *

    st.success(
        "Dashboard Loaded"
    )


# =========================================================
# UPLOAD PAGE
# =========================================================

elif page == "Upload":

    from pages.upload import *

    st.success(
        "Upload Page Loaded"
    )


# =========================================================
# ANALYTICS PAGE
# =========================================================

elif page == "Analytics":

    from pages.analytics import *

    st.success(
        "Analytics Loaded"
    )


# =========================================================
# MONITORING PAGE
# =========================================================

elif page == "Monitoring":

    from pages.monitoring import *

    st.success(
        "Monitoring Loaded"
    )