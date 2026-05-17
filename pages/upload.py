import requests
import streamlit as st


# =========================================================
# TITLE
# =========================================================

st.title(
    "📂 Upload Email File"
)

st.markdown(
    "Upload .txt or .eml email files for threat analysis."
)


# =========================================================
# FILE UPLOADER
# =========================================================

uploaded_file = st.file_uploader(

    "Choose Email File",

    type=[

        "txt",

        "eml"
    ]
)


# =========================================================
# API URL
# =========================================================

API_URL = "https://email-threat-intelligence-app-3.onrender.com/predict"


# =========================================================
# PROCESS FILE
# =========================================================

if uploaded_file is not None:

    email_content = uploaded_file.read().decode(

        "utf-8",

        errors="ignore"
    )


    st.markdown("---")

    st.subheader(
        "📧 Uploaded Email Content"
    )

    st.text_area(

        "Raw Email",

        email_content,

        height=300
    )


    if st.button("Analyze Uploaded Email"):

        payload = {

            "email_text": email_content
        }


        # =================================================
        # API REQUEST
        # =================================================

        try:

            response = requests.post(

                API_URL,

                json=payload,

                timeout=60
            )


            if response.status_code == 200:

                result = response.json()

            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

                st.stop()


        except Exception as e:

            st.error(
                f"Connection Error: {str(e)}"
            )

            st.stop()


        # =================================================
        # FINAL RESULT
        # =================================================

        st.markdown("---")

        st.subheader(
            "🎯 Threat Assessment"
        )


        if result["prediction"] == 1:

            st.error(

                f"🚨 {result['label']}"
            )

        else:

            st.success(

                f"✅ {result['label']}"
            )


        # =================================================
        # RISK SCORE
        # =================================================

        risk_score = result[
            "risk_score"
        ]

        st.markdown(

            f"### Risk Score: {risk_score}/100"
        )

        st.progress(
            risk_score / 100
        )


        # =================================================
        # SECURITY METRICS
        # =================================================

        st.markdown("---")

        st.subheader(
            "📊 Security Metrics"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(

            "Spam Probability",

            result["spam_probability"]
        )

        col2.metric(

            "Threat Level",

            result["threat_level"]
        )

        col3.metric(

            "Links Found",

            result["url_count"]
        )


        col4, col5, col6 = st.columns(3)


        col4.metric(

            "HTML Tags",

            result["html_tag_count"]
        )

        col5.metric(

            "Uppercase Ratio",

            result["uppercase_ratio"]
        )

        col6.metric(

            "Exclamation Count",

            result["exclamation_count"]
        )


        # =================================================
        # THREAT INDICATORS
        # =================================================

        st.markdown("---")

        st.subheader(
            "🚨 Threat Indicators"
        )


        for reason in result["reasons"]:

            st.write(
                f"- {reason}"
            )


        # =================================================
        # THREAT SCORE BREAKDOWN
        # =================================================

        st.markdown("---")

        st.subheader(
            "📊 Threat Score Breakdown"
        )

        breakdown = result[
            "score_breakdown"
        ]


        if len(breakdown) > 0:

            for item, points in breakdown.items():

                st.write(
                    f"{item}: +{points}"
                )

        else:

            st.success(
                "No major threat indicators found."
            )


        # =================================================
        # DETECTED PATTERNS
        # =================================================

        st.markdown("---")

        st.subheader(
            "🧠 Threat Intelligence"
        )


        patterns = result[
            "detected_patterns"
        ]


        if len(patterns) > 0:

            for category, words in patterns.items():

                st.warning(

                    f"{category.upper()} → {', '.join(words)}"
                )

        else:

            st.success(
                "No suspicious patterns detected."
            )


        # =================================================
        # CLEAN TEXT
        # =================================================

        st.markdown("---")

        st.subheader(
            "🧹 Processed Text"
        )

        st.code(

            result["clean_text"]
        )