import requests
import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="AI Monitoring",

    page_icon="🖥️",

    layout="wide"
)


# =========================================================
# PAGE TITLE
# =========================================================

st.title(
    "🖥️ AI Monitoring Center"
)

st.caption(
    "Real-time monitoring for the Email Threat Intelligence platform."
)


# =========================================================
# API ENDPOINTS
# =========================================================

HEALTH_API = "https://email-threat-intelligence-app-3.onrender.com/health"

METRICS_API = "https://email-threat-intelligence-app-3.onrender.com/monitoring/metrics"

DRIFT_API = "https://email-threat-intelligence-app-3.onrender.com/monitoring/drift"


# =========================================================
# FETCH API DATA
# =========================================================

health_ok = False

metrics_data = {}

drift_data = {}


# =========================================================
# HEALTH CHECK
# =========================================================

try:

    health_response = requests.get(
        HEALTH_API
    )

    health_data = health_response.json()

    if health_data["status"] == "healthy":

        health_ok = True

except:

    health_ok = False


# =========================================================
# METRICS FETCH
# =========================================================

try:

    metrics_response = requests.get(
        METRICS_API
    )

    metrics_data = metrics_response.json()

except:

    metrics_data = {

        "total_predictions": 0,

        "spam_predictions": 0,

        "ham_predictions": 0
    }


# =========================================================
# DRIFT FETCH
# =========================================================

try:

    drift_response = requests.get(
        DRIFT_API
    )

    drift_data = drift_response.json()

except:

    drift_data = {

        "drift_detected": False,

        "system_status": "UNKNOWN",

        "alert": "Monitoring unavailable"
    }


# =========================================================
# KPI DASHBOARD
# =========================================================

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)


# =========================================================
# SYSTEM HEALTH
# =========================================================

with col1:

    if health_ok:

        st.success(
            "🟢 System Healthy"
        )

    else:

        st.error(
            "🔴 API Offline"
        )


# =========================================================
# TOTAL PREDICTIONS
# =========================================================

with col2:

    st.metric(

        "Total Predictions",

        metrics_data[
            "total_predictions"
        ]
    )


# =========================================================
# SPAM DETECTIONS
# =========================================================

with col3:

    st.metric(

        "Spam Detections",

        metrics_data[
            "spam_predictions"
        ]
    )


# =========================================================
# HAM EMAILS
# =========================================================

with col4:

    st.metric(

        "Ham Emails",

        metrics_data[
            "ham_predictions"
        ]
    )


# =========================================================
# SYSTEM STATUS SECTION
# =========================================================

st.markdown("---")

left_col, right_col = st.columns(2)


# =========================================================
# DRIFT STATUS
# =========================================================

with left_col:

    st.subheader(
        "📉 Drift Monitoring"
    )

    if drift_data["drift_detected"]:

        st.error(
            "⚠️ Model drift detected"
        )

    else:

        st.success(
            "✅ No significant drift detected"
        )


    st.metric(

        "System Status",

        drift_data[
            "system_status"
        ]
    )


# =========================================================
# ALERTS PANEL
# =========================================================

with right_col:

    st.subheader(
        "🚨 Monitoring Alerts"
    )

    st.info(

        drift_data[
            "alert"
        ]
    )

    if health_ok:

        st.success(
            "Backend API operational"
        )

    else:

        st.error(
            "Backend API unreachable"
        )


# =========================================================
# OBSERVABILITY FEATURES
# =========================================================

st.markdown("---")

st.subheader(
    "🔍 Active Monitoring Features"
)

feature_col1, feature_col2 = st.columns(2)


with feature_col1:

    st.write(
        "✅ Prediction Logging"
    )

    st.write(
        "✅ Threat Analytics"
    )

    st.write(
        "✅ Hybrid Threat Intelligence"
    )


with feature_col2:

    st.write(
        "✅ Drift Detection"
    )

    st.write(
        "✅ Real-time Monitoring"
    )

    st.write(
        "✅ Security Observability"
    )