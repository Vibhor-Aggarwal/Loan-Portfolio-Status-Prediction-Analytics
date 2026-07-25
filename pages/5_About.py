import streamlit as st

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="About Project",
    page_icon="📘",
    layout="wide"
)

# --------------------------------------------------------
# Hero Banner
# --------------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(135deg,#1E3A8A,#2563EB);
padding:35px;
border-radius:18px;
margin-bottom:30px;
">

<h1 style="color:white;">
About This Project
</h1>

<p style="
color:#DBEAFE;
font-size:18px;
line-height:1.7;
">

Loan Portfolio Status Prediction & Analytics is an end-to-end Machine
Learning project that predicts whether a borrower is likely to repay
a loan or default using historical Lending Club loan data.

The project demonstrates the complete machine learning lifecycle,
from raw data preprocessing to deployment through an interactive
Streamlit dashboard.

</p>

</div>
""",
unsafe_allow_html=True)

# --------------------------------------------------------
# Dashboard Cards
# --------------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Dataset",
        "396K+ Records"
    )

with c2:
    st.metric(
        "Features",
        "49"
    )

with c3:
    st.metric(
        "Models",
        "4"
    )

with c4:
    st.metric(
        "Best Model",
        "Random Forest"
    )

st.markdown("---")

# --------------------------------------------------------
# Project Overview
# --------------------------------------------------------

left,right = st.columns([2,1])

with left:

    st.markdown("## Project Overview")

    st.write("""

This project was developed to solve a real-world financial risk
prediction problem.

Using historical Lending Club loan data, several machine learning
algorithms were trained and evaluated to predict whether a loan would
be **Fully Paid** or **Charged Off**.

The project covers the complete data science pipeline including data
cleaning, exploratory data analysis, feature engineering,
preprocessing, model development, evaluation, explainability and
deployment.

""")

with right:

    st.info("""

### Project Details

Domain

Financial Analytics

---

Problem Type

Binary Classification

---

Target Variable

loan_status

---

Deployment

Streamlit Dashboard

""")

st.markdown("---")

# --------------------------------------------------------
# Workflow
# --------------------------------------------------------

st.markdown("## Machine Learning Workflow")

st.info("""

Raw Dataset

⬇

Data Understanding

⬇

Data Cleaning

⬇

Exploratory Data Analysis

⬇

Feature Engineering

⬇

Feature Encoding

⬇

Feature Scaling

⬇

Train-Test Split

⬇

SMOTE Oversampling

⬇

Model Training

⬇

Model Comparison

⬇

Hyperparameter Tuning

⬇

Feature Importance

⬇

Prediction Dashboard

""")

st.markdown("---")

# --------------------------------------------------------
# Technology Stack
# --------------------------------------------------------

st.markdown("## Technology Stack")

a,b,c,d = st.columns(4)

with a:

    st.success("""

### Programming

Python

Pandas

NumPy

""")

with b:

    st.success("""

### Machine Learning

Scikit-Learn

Random Forest

SMOTE

Joblib

""")

with c:

    st.success("""

### Visualization

Matplotlib

Streamlit

EDA

Dashboard

""")

with d:

    st.success("""

### Development

Git

GitHub

VS Code

""")

st.markdown("---")

# --------------------------------------------------------
# Models Used
# --------------------------------------------------------

st.markdown("## Machine Learning Models")

left,right = st.columns(2)

with left:

    st.info("""

### Models Evaluated

• Logistic Regression

• Decision Tree

• Random Forest

• Gradient Boosting

""")

with right:

    st.success("""

### Final Selection

🏆 Random Forest

Highest Accuracy

Best F1 Score

Best Overall Performance

""")

st.markdown("---")

# --------------------------------------------------------
# Skills Demonstrated
# --------------------------------------------------------

st.markdown("## Skills Demonstrated")

s1,s2 = st.columns(2)

with s1:

    st.success("""

✔ Data Cleaning

✔ Exploratory Data Analysis

✔ Feature Engineering

✔ Data Preprocessing

✔ Feature Encoding

✔ Feature Scaling

✔ SMOTE

""")

with s2:

    st.success("""

✔ Machine Learning

✔ Hyperparameter Tuning

✔ Model Evaluation

✔ Explainable AI

✔ Feature Importance

✔ Streamlit Development

✔ Dashboard Design

""")

st.markdown("---")

# --------------------------------------------------------
# Business Value
# --------------------------------------------------------

st.markdown("## Business Impact")

st.write("""

Financial institutions receive thousands of loan applications every day.

Predictive machine learning models help lenders identify risky
borrowers before approval, reducing financial losses while improving
credit risk management.

This dashboard provides an interactive decision-support system capable
of estimating repayment risk using historical borrower information.

""")

st.markdown("---")

# --------------------------------------------------------
# Future Improvements
# --------------------------------------------------------

st.markdown("## Future Enhancements")

col1,col2 = st.columns(2)

with col1:

    st.warning("""

### Possible Improvements

• Cloud Deployment

• REST API

• User Authentication

• Real-Time Prediction

• Model Monitoring

""")

with col2:

    st.warning("""

### Advanced Features

• SHAP Explainability

• Live Banking Data

• Automated Retraining

• Deep Learning Models

• Portfolio Analytics

""")

st.markdown("---")

# --------------------------------------------------------
# Developer
# --------------------------------------------------------

st.markdown("## Developer")

st.success("""

**Vibhor Aggarwal**

Computer Science Engineering Student

End-to-End Machine Learning Project

Technologies Used

Python • Pandas • NumPy • Scikit-Learn • Streamlit • Git • GitHub

""")

st.markdown("---")

# --------------------------------------------------------
# Footer
# --------------------------------------------------------

st.markdown("""
<div style="
background:#F8FAFC;
padding:25px;
border-radius:15px;
text-align:center;
">

<h2 style="color:#2563EB;">
Loan Portfolio Status Prediction & Analytics
</h2>

<p>

End-to-End Machine Learning Project

</p>

<p>

Developed by <strong>Vibhor Aggarwal</strong>

</p>

</div>
""",
unsafe_allow_html=True)