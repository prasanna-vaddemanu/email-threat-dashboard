import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="Security Analytics",

    page_icon="📊",

    layout="wide"
)


# =========================================================
# LOAD DATA
# =========================================================

LOG_PATH = "logs/predictions.csv"


try:

    df = pd.read_csv(LOG_PATH)

    # =========================================
    # CLEAN NULL VALUES
    # =========================================

    df = df.dropna()

except:

    st.error(
        "Prediction logs not found."
    )

    st.stop()


if len(df) == 0:

    st.warning(
        "No prediction data available."
    )

    st.stop()


# =========================================================
# PAGE TITLE
# =========================================================

st.title(
    "🛡️ AI Security Analytics Center"
)

st.caption(
    "Real-time monitoring and threat intelligence analytics."
)


# =========================================================
# KPI METRICS
# =========================================================

spam_count = len(
    df[df["label"] == "SPAM"]
)

ham_count = len(
    df[df["label"] == "HAM"]
)

high_threats = len(
    df[df["threat_level"] == "HIGH"]
)

avg_risk = round(
    df["risk_score"].mean(),
    2
)


st.markdown("---")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(

        "Total Emails",

        len(df)
    )


with col2:

    st.metric(

        "Spam Detected",

        spam_count
    )


with col3:

    st.metric(

        "High Threats",

        high_threats
    )


with col4:

    st.metric(

        "Avg Risk Score",

        avg_risk
    )


# =========================================================
# CHART GRID
# =========================================================

st.markdown("---")

left_col, right_col = st.columns(2)


# =========================================================
# SPAM VS HAM
# =========================================================

with left_col:

    st.subheader(
        "📬 Spam vs Ham"
    )

    fig1, ax1 = plt.subplots(
        figsize=(4, 4)
    )

    df["label"].value_counts().plot(

        kind="pie",

        autopct="%1.1f%%",

        ax=ax1
    )

    ax1.set_ylabel("")

    plt.tight_layout()

    st.pyplot(fig1)


# =========================================================
# THREAT LEVELS
# =========================================================

with right_col:

    st.subheader(
        "🚨 Threat Levels"
    )

    fig2, ax2 = plt.subplots(
        figsize=(5, 4)
    )

    df["threat_level"].value_counts().plot(

        kind="bar",

        ax=ax2
    )

    ax2.set_xlabel(
        "Threat Level"
    )

    ax2.set_ylabel(
        "Count"
    )

    plt.tight_layout()

    st.pyplot(fig2)


# =========================================================
# SECOND ROW
# =========================================================

st.markdown("---")

left_col2, right_col2 = st.columns(2)


# =========================================================
# RISK DISTRIBUTION
# =========================================================

with left_col2:

    st.subheader(
        "🔥 Risk Distribution"
    )

    fig3, ax3 = plt.subplots(
        figsize=(5, 3)
    )

    ax3.hist(

        df["risk_score"],

        bins=10
    )

    ax3.set_xlabel(
        "Risk Score"
    )

    ax3.set_ylabel(
        "Frequency"
    )

    plt.tight_layout()

    st.pyplot(fig3)


# =========================================================
# ML CONFIDENCE
# =========================================================

with right_col2:

    st.subheader(
        "🧠 ML Confidence"
    )

    fig4, ax4 = plt.subplots(
        figsize=(5, 3)
    )

    ax4.hist(

        df["spam_probability"],

        bins=10
    )

    ax4.set_xlabel(
        "Spam Probability"
    )

    ax4.set_ylabel(
        "Frequency"
    )

    plt.tight_layout()

    st.pyplot(fig4)


# =========================================================
# RECENT PREDICTIONS TABLE
# =========================================================

st.markdown("---")

st.subheader(
    "🕒 Recent Predictions"
)

recent_df = df.tail(15)

st.dataframe(

    recent_df,

    use_container_width=True
)