import streamlit as st
import pandas as pd

from src.predictor import predict

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Loan Prediction",
    page_icon="🏦",
    layout="wide"
)

# -------------------------------------------------------
# Hero Section
# -------------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(135deg,#1E3A8A,#2563EB);
padding:35px;
border-radius:18px;
margin-bottom:30px;
">

<h1 style="color:white;">
Loan Portfolio Risk Assessment
</h1>

<p style="
color:#DBEAFE;
font-size:18px;
line-height:1.7;
">

Evaluate the probability of loan repayment using a machine learning
model trained on historical Lending Club loan applications.

The dashboard estimates whether a borrower is more likely to
repay the loan successfully or become a potential default risk.

</p>

</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Information Cards
# -------------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:

    st.info("""

### Model

Random Forest Classifier

""")

with c2:

    st.info("""

### Dataset

396K+ Historical Loans

""")

with c3:

    st.info("""

### Prediction

Fully Paid vs Charged Off

""")

st.markdown("---")

st.markdown("""
## Applicant Information

Complete the following financial and credit information to generate
a loan repayment prediction.

Fields closely resemble the attributes used while training the model.
""")

# -------------------------------------------------------
# Loan Information
# -------------------------------------------------------

st.markdown("## Loan Details")

left, right = st.columns(2)

with left:

    loan_amnt = st.number_input(
        "Loan Amount ($)",
        min_value=500,
        max_value=50000,
        value=12000,
        step=500
    )

    term = st.selectbox(
        "Loan Term",
        [
            " 36 months",
            " 60 months"
        ]
    )

    int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=5.0,
        max_value=35.0,
        value=12.5
    )

    installment = st.number_input(
        "Monthly Installment ($)",
        min_value=50.0,
        value=350.0
    )

with right:

    grade = st.selectbox(
        "Loan Grade",
        [
            "A","B","C","D","E","F","G"
        ]
    )

    sub_grade = st.selectbox(
        "Sub Grade",
        [
            "A1","A2","A3","A4","A5",
            "B1","B2","B3","B4","B5",
            "C1","C2","C3","C4","C5",
            "D1","D2","D3","D4","D5",
            "E1","E2","E3","E4","E5",
            "F1","F2","F3","F4","F5",
            "G1","G2","G3","G4","G5"
        ]
    )

    st.success(f"""

### Quick Loan Summary

**Loan Amount**

${loan_amnt:,.0f}

**Interest Rate**

{int_rate:.2f}%

**Grade**

{grade}

**Sub Grade**

{sub_grade}

""")

st.markdown("---")

# -------------------------------------------------------
# Borrower Information
# -------------------------------------------------------

st.markdown("## Borrower Profile")

left, right = st.columns(2)

with left:

    annual_inc = st.number_input(
        "Annual Income ($)",
        min_value=10000,
        value=60000,
        step=5000
    )

    emp_length = st.slider(
        "Employment Length (Years)",
        0,
        10,
        5
    )

    home_ownership = st.selectbox(
        "Home Ownership",
        [
            "RENT",
            "OWN",
            "MORTGAGE",
            "OTHER"
        ]
    )

with right:

    verification_status = st.selectbox(
        "Verification Status",
        [
            "Verified",
            "Source Verified",
            "Not Verified"
        ]
    )

    purpose = st.selectbox(
        "Loan Purpose",
        [
            "debt_consolidation",
            "credit_card",
            "home_improvement",
            "major_purchase",
            "small_business",
            "car",
            "medical",
            "moving",
            "vacation",
            "house",
            "other",
            "wedding"
        ]
    )

    application_type = st.selectbox(
        "Application Type",
        [
            "INDIVIDUAL",
            "JOINT",
            "DIRECT_PAY"
        ]
    )

st.markdown("---")

# -------------------------------------------------------
# Credit Profile
# -------------------------------------------------------

st.markdown("## Credit Profile")

c1, c2 = st.columns(2)

with c1:

    dti = st.slider(
        "Debt-To-Income Ratio (%)",
        0.0,
        40.0,
        15.0
    )

    revol_util = st.slider(
        "Revolving Utilization (%)",
        0.0,
        150.0,
        45.0
    )

with c2:

    open_acc = st.slider(
        "Open Credit Accounts",
        1,
        50,
        10
    )

    total_acc = st.slider(
        "Total Credit Accounts",
        1,
        100,
        25
    )

st.markdown("---")

# -------------------------------------------------------
# Applicant Snapshot
# -------------------------------------------------------

st.markdown("## Applicant Snapshot")

m1, m2, m3, m4 = st.columns(4)

with m1:

    st.metric(
        "Loan Amount",
        f"${loan_amnt:,.0f}"
    )

with m2:

    st.metric(
        "Interest Rate",
        f"{int_rate:.2f}%"
    )

with m3:

    st.metric(
        "Annual Income",
        f"${annual_inc:,.0f}"
    )

with m4:

    st.metric(
        "Employment",
        f"{emp_length} Years"
    )

st.markdown("<br>", unsafe_allow_html=True)

m5, m6, m7, m8 = st.columns(4)

with m5:

    st.metric(
        "Loan Grade",
        grade
    )

with m6:

    st.metric(
        "DTI",
        f"{dti:.1f}%"
    )

with m7:

    st.metric(
        "Open Accounts",
        open_acc
    )

with m8:

    st.metric(
        "Total Accounts",
        total_acc
    )

st.markdown("---")

# -------------------------------------------------------
# Prepare Model Input
# -------------------------------------------------------

input_data = pd.DataFrame({

    "loan_amnt":[loan_amnt],

    "term":[term],

    "int_rate":[int_rate],

    "installment":[installment],

    "grade":[grade],

    "sub_grade":[sub_grade],

    "emp_length":[emp_length],

    "annual_inc":[annual_inc],

    "dti":[dti],

    "open_acc":[open_acc],

    "pub_rec":[0],

    "revol_bal":[15000],

    "revol_util":[revol_util],

    "total_acc":[total_acc],

    "mort_acc":[1],

    "pub_rec_bankruptcies":[0],

    "earliest_cr_line":["Jan-2000"],

    "issue_d":["Jan-2018"],

    "home_ownership":[home_ownership],

    "verification_status":[verification_status],

    "purpose":[purpose],

    "initial_list_status":["w"],

    "application_type":[application_type],

    "emp_title":["Unknown"],

    "address":["Unknown"]

})

predict_button = st.button(
    "Predict Loan Status",
    type="primary",
    use_container_width=True
)

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

if predict_button:

    try:

        prediction, confidence = predict(input_data)

        st.markdown("---")

        st.markdown("""
        <div style="
        background:linear-gradient(135deg,#1E3A8A,#2563EB);
        padding:25px;
        border-radius:15px;
        margin-bottom:25px;
        ">

        <h2 style="color:white;margin:0;">
        Prediction Results
        </h2>

        <p style="color:#DBEAFE;font-size:17px;">
        Machine learning assessment using the trained Random Forest model.
        </p>

        </div>
        """,
        unsafe_allow_html=True)

        left, right = st.columns([2,1])

        # ----------------------------------------------------
        # Prediction Result
        # ----------------------------------------------------

        with left:

            if prediction == "Fully Paid":

                st.success(
                    "### ✅ Low Risk Applicant\n\nThe model predicts that this loan is likely to be **Fully Paid**."
                )

                risk_level = "LOW"

                recommendation = "Recommended for Approval"

                risk_color = "🟢"

            else:

                st.error(
                    "### ❌ High Risk Applicant\n\nThe model predicts that this loan is likely to be **Charged Off**."
                )

                risk_level = "HIGH"

                recommendation = "Manual Review Recommended"

                risk_color = "🔴"

            st.write("")

            st.subheader("Prediction Confidence")

            st.progress(float(confidence))

            st.metric(
                "Confidence Score",
                f"{confidence*100:.2f}%"
            )

        # ----------------------------------------------------
        # Decision Card
        # ----------------------------------------------------

        with right:

            st.markdown(f"""
<div style="
background:white;
padding:20px;
border-radius:15px;
border:1px solid #E5E7EB;
box-shadow:0px 5px 15px rgba(0,0,0,0.08);
">

<h3 style="color:#1E3A8A;">
Loan Decision
</h3>

<hr>

<b>Prediction</b>

<br>

{prediction}

<br><br>

<b>Risk Level</b>

<br>

{risk_color} {risk_level}

<br><br>

<b>Recommendation</b>

<br>

{recommendation}

</div>
""",
unsafe_allow_html=True)

        # ----------------------------------------------------
        # Risk Meter
        # ----------------------------------------------------

        st.markdown("---")

        st.subheader("Risk Assessment")

        risk_score = (1 - confidence) * 100 if prediction == "Fully Paid" else confidence * 100

        st.progress(min(risk_score / 100, 1.0))

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Risk Score",
                f"{risk_score:.1f}%"
            )

        with c2:

            st.metric(
                "Decision",
                prediction
            )

        with c3:

            st.metric(
                "Model",
                "Random Forest"
            )

        st.markdown("---")

        # ----------------------------------------------------
        # Business Interpretation
        # ----------------------------------------------------

        st.subheader("Business Interpretation")

        if prediction == "Fully Paid":

            st.markdown("""
<div style="
background:#ECFDF5;
padding:22px;
border-radius:15px;
border-left:7px solid #10B981;
">

<h3 style="color:#065F46;">
✅ Low Credit Risk
</h3>

The applicant demonstrates characteristics commonly associated with
successful loan repayment.

<b>Positive Indicators</b>

<ul>
<li>Healthy financial profile</li>
<li>Reasonable debt-to-income ratio</li>
<li>Stable employment history</li>
<li>Acceptable loan grade</li>
<li>Strong repayment potential</li>
</ul>

Overall, the model estimates a relatively low probability of default.

</div>
""",
unsafe_allow_html=True)

        else:

            st.markdown("""
<div style="
background:#FEF2F2;
padding:22px;
border-radius:15px;
border-left:7px solid #DC2626;
">

<h3 style="color:#991B1B;">
⚠ High Credit Risk
</h3>

The applicant exhibits characteristics frequently associated with
historical loan defaults.

<b>Potential Risk Factors</b>

<ul>
<li>Higher borrowing risk</li>
<li>Higher interest rate</li>
<li>Elevated debt burden</li>
<li>Credit profile indicates increased default probability</li>
</ul>

The lender should perform additional verification before approval.

</div>
""",
unsafe_allow_html=True)

        st.markdown("---")

        # ----------------------------------------------------
        # Applicant Summary
        # ----------------------------------------------------

        st.subheader("Applicant Summary")

        summary_df = pd.DataFrame({

            "Feature":[
                "Loan Amount",
                "Interest Rate",
                "Loan Grade",
                "Sub Grade",
                "Employment Length",
                "Annual Income",
                "Debt-To-Income Ratio",
                "Home Ownership",
                "Verification Status",
                "Loan Purpose",
                "Application Type"
            ],

            "Value":[
                f"${loan_amnt:,.0f}",
                f"{int_rate:.2f}%",
                grade,
                sub_grade,
                f"{emp_length} Years",
                f"${annual_inc:,.0f}",
                f"{dti:.1f}%",
                home_ownership,
                verification_status,
                purpose,
                application_type
            ]

        })

        st.dataframe(
            summary_df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        # ----------------------------------------------------
        # Credit Metrics
        # ----------------------------------------------------

        st.subheader("Credit Profile Metrics")

        a,b,c,d = st.columns(4)

        with a:

            st.metric(
                "Open Accounts",
                open_acc
            )

        with b:

            st.metric(
                "Total Accounts",
                total_acc
            )

        with c:

            st.metric(
                "Revolving Utilization",
                f"{revol_util:.1f}%"
            )

        with d:

            st.metric(
                "Debt-To-Income",
                f"{dti:.1f}%"
            )

        st.markdown("---")

        # ----------------------------------------------------
        # AI Recommendation
        # ----------------------------------------------------

        st.subheader("Model Recommendation")

        if prediction == "Fully Paid":

            st.success("""
### Recommendation

The applicant appears financially reliable according to the trained
Random Forest model.

Recommended Actions

• Proceed with loan approval

• Continue standard verification

• Monitor repayments through routine portfolio management

""")

        else:

            st.warning("""
### Recommendation

The applicant presents an elevated probability of loan default.

Recommended Actions

• Perform additional credit verification

• Review applicant documentation carefully

• Consider adjusting loan amount or interest rate

• Conduct manual risk assessment before approval

""")

        st.markdown("---")

        # ----------------------------------------------------
        # Footer
        # ----------------------------------------------------

        st.markdown("""
<div style="
background:#F8FAFC;
padding:20px;
border-radius:15px;
text-align:center;
">

<h3 style="color:#1E3A8A;">
Loan Prediction Completed
</h3>

<p>

Prediction generated using the trained Random Forest model developed
during this machine learning project.

</p>

</div>
""",
unsafe_allow_html=True)

    except Exception as e:

        st.error("Prediction failed.")

        st.exception(e)