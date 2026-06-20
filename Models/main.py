import streamlit as st
from predict_helper import predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Hamro Finance Credit Risk App",
    page_icon="🏦",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

h1 {
    color: #38bdf8 !important;
    text-align: center;
    font-weight: 700;
}

h3 {
    color: #e2e8f0 !important;
    text-align: center;
}

[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    text-align: center;
}
            div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label {
    color: white !important;
    font-weight: bold !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: white !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 12px;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1>🏦 Hamro Finance Credit Risk Modeling</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3>Evaluate Credit Risk and Generate Credit Score</h3>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUTS ----------------
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=28
    )

with row1[1]:
    income = st.number_input(
        "Income",
        min_value=0,
        value=1200000
    )

with row1[2]:
    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=2560000
    )

loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.metric(
        "Loan / Income Ratio",
        f"{loan_to_income_ratio:.2f}"
    )

with row2[1]:
    loan_tenure_months = st.number_input(
        "Loan Tenure (Months)",
        min_value=0,
        value=36
    )

with row2[2]:
    avg_dpd_per_deliquence = st.number_input(
        "Average DPD",
        min_value=0,
        value=20
    )

with row3[0]:
    deliquent_ratio = st.number_input(
        "Delinquency Ratio (%)",
        min_value=0,
        max_value=100,
        value=30
    )

with row3[1]:
    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio (%)",
        min_value=0,
        max_value=100,
        value=30
    )

with row3[2]:
    num_open_accounts = st.number_input(
        "Open Loan Accounts",
        min_value=1,
        max_value=10,
        value=2
    )

with row4[0]:
    residence_type = st.selectbox(
        "Residence Type",
        ["Owned", "Rented", "Mortgage"]
    )

with row4[1]:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Education", "Home", "Auto", "Personal"]
    )

with row4[2]:
    loan_type = st.selectbox(
        "Loan Type",
        ["Unsecured", "Secured"]
    )

st.write("")
st.write("")

# ---------------- PREDICTION BUTTON ----------------
if st.button("🔍 Calculate Credit Risk"):

    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_deliquence,
        deliquent_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    st.divider()
    st.subheader("📊 Credit Assessment Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Default Probability",
            f"{probability:.2%}"
        )

    with col2:
        st.metric(
            "Credit Score",
            credit_score
        )

    with col3:
        st.metric(
            "Credit Rating",
            rating
        )

    st.write("")

    if rating == "Excellent":
        st.success(f"✅ Rating: {rating} | Very Low Risk Applicant")

    elif rating == "Good":
        st.info(f"👍 Rating: {rating} | Low Risk Applicant")

    elif rating == "Average":
        st.warning(f"⚠️ Rating: {rating} | Moderate Risk Applicant")

    else:
        st.error(f"❌ Rating: {rating} | High Risk Applicant")