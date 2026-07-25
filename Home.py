import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Loan Portfolio Status Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("# 🏦 Loan Portfolio")

    st.caption("Machine Learning Analytics Dashboard")

    st.markdown("---")

    st.success("""
### 🎯 Our Mission

Build an intelligent loan risk prediction system that assists financial
institutions in identifying risky borrowers before loan approval.

The dashboard demonstrates a complete end-to-end machine learning workflow.
""")

    st.markdown("---")

    st.metric("Dataset", "396K+")
    st.metric("Input Features", "49")
    st.metric("ML Models", "4")
    st.metric("Best Model", "Random Forest")

    st.markdown("---")

    st.info("""
### Navigation

🏠 Home

📊 Dataset & EDA

🤖 Prediction

📈 Model Performance

🎯 Feature Importance

📘 About
""")

# ==========================================================
# HERO SECTION
# ==========================================================

left, right = st.columns([3.5,1])

with left:

    st.markdown("""
<div style="
background:linear-gradient(135deg,#1E3A8A,#2563EB);
padding:40px;
border-radius:24px;
min-height:240px;
box-shadow:0 12px 30px rgba(0,0,0,.12);
">

<h1 style="
color:white;
margin-bottom:12px;
font-size:40px;
">

Loan Portfolio Status Prediction & Analytics

</h1>

<p style="
font-size:19px;
color:#DBEAFE;
line-height:1.8;
">

Predict whether a borrower is likely to repay a loan or default
using historical Lending Club loan data.

This dashboard demonstrates a complete machine learning pipeline
covering preprocessing, exploratory data analysis, model training,
hyperparameter tuning, explainability, and deployment.

</p>

</div>
""", unsafe_allow_html=True)

with right:

    st.markdown("""
<div style="
background:white;
border-radius:24px;
padding:30px;
height:240px;
display:flex;
justify-content:center;
align-items:center;
box-shadow:0 10px 30px rgba(0,0,0,.08);
">

<div style="
font-size:120px;
">
🏦
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# KPI SECTION
# ==========================================================

st.markdown("## Dashboard Overview")

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric(
        "Loan Records",
        "396K+",
        "Lending Club"
    )

with k2:
    st.metric(
        "Features",
        "49",
        "Engineered Variables"
    )

with k3:
    st.metric(
        "Algorithms",
        "4",
        "Models Evaluated"
    )

with k4:
    st.metric(
        "Production Model",
        "Random Forest",
        "Best Accuracy"
    )

st.write("")

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

left,right = st.columns([2.2,1])

with left:

    st.markdown("""
<div style="
background:white;
padding:30px;
border-radius:22px;
box-shadow:0 8px 25px rgba(0,0,0,.08);
min-height:430px;
">

<h2 style="color:#1E3A8A;">
📌 Project Overview
</h2>

<p style="font-size:17px; line-height:1.9; color:#334155;">

Loan Portfolio Status Prediction is an end-to-end Machine Learning
project developed using the Lending Club loan dataset.

The objective is to predict whether a borrower will successfully
repay a loan or become a loan default.

The project demonstrates the complete industrial machine learning
workflow including:

</p>

<ul style="font-size:17px; line-height:2; color:#334155;">

<li>Data Understanding</li>

<li>Data Cleaning</li>

<li>Exploratory Data Analysis</li>

<li>Feature Engineering</li>

<li>Data Preprocessing</li>

<li>Model Training</li>

<li>Hyperparameter Tuning</li>

<li>Feature Importance Analysis</li>

<li>Interactive Prediction Dashboard</li>

</ul>

</div>
""",
unsafe_allow_html=True)

with right:

    st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:22px;
box-shadow:0 8px 25px rgba(0,0,0,.08);
min-height:430px;
">

<h2 style="color:#1E3A8A;">
📊 Project Info
</h2>

<hr>

<b>Dataset</b>

<br>

Lending Club

<hr>

<b>Domain</b>

<br>

Financial Analytics

<hr>

<b>Problem</b>

<br>

Binary Classification

<hr>

<b>Target</b>

<br>

loan_status

<hr>

<b>Final Model</b>

<br>

Random Forest

<hr>

<b>Deployment</b>

<br>

Streamlit Dashboard

</div>
""",
unsafe_allow_html=True)

st.write("")

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.markdown("## 💻 Technology Stack")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
min-height:220px;
">

<h3 style="color:#2563EB;">🐍 Programming</h3>

• Python

• Pandas

• NumPy

• Joblib

</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
min-height:220px;
">

<h3 style="color:#2563EB;">🤖 Machine Learning</h3>

• Scikit-Learn

• Random Forest

• SMOTE

• RandomizedSearchCV

</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
min-height:220px;
">

<h3 style="color:#2563EB;">📊 Visualization</h3>

• Streamlit

• Matplotlib

• Feature Importance

• EDA Charts

</div>
""", unsafe_allow_html=True)

with c4:
    st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
min-height:220px;
">

<h3 style="color:#2563EB;">⚙️ Development</h3>

• VS Code

• Git

• GitHub

• Streamlit

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# MACHINE LEARNING WORKFLOW
# ==========================================================

left, right = st.columns([1,2])

with left:

    st.markdown("## 🔄 Workflow")

    st.markdown("""
1️⃣ Data Collection

⬇️

2️⃣ Data Cleaning

⬇️

3️⃣ Exploratory Data Analysis

⬇️

4️⃣ Feature Engineering

⬇️

5️⃣ Data Preprocessing

⬇️

6️⃣ Model Training

⬇️

7️⃣ Hyperparameter Tuning

⬇️

8️⃣ Model Evaluation

⬇️

9️⃣ Feature Importance

⬇️

🔟 Loan Prediction
""")

with right:

    st.markdown("## 📖 Workflow Description")

    st.info("""

This application demonstrates a complete end-to-end machine learning pipeline.

• Historical Lending Club loan data was collected.

• Missing values and outliers were handled.

• Exploratory Data Analysis identified important patterns.

• Feature Engineering improved predictive performance.

• Multiple ML algorithms were trained.

• Random Forest achieved the highest performance.

• Hyperparameter tuning was performed using RandomizedSearchCV.

• SMOTE was applied to handle class imbalance.

• The trained model was deployed using Streamlit.

""")

st.write("")

# ==========================================================
# FEATURES
# ==========================================================

st.markdown("## ✨ Dashboard Features")

f1, f2 = st.columns(2)

with f1:

    st.success("""
### 📊 Analytics

✔ Dataset Overview

✔ Statistical Summary

✔ Exploratory Data Analysis

✔ Feature Engineering

✔ Feature Importance

✔ Interactive Tables
""")

with f2:

    st.success("""
### 🤖 Prediction

✔ Loan Status Prediction

✔ Confidence Score

✔ Business Interpretation

✔ Model Comparison

✔ Risk Assessment

✔ Interactive Dashboard
""")

st.write("")

# ==========================================================
# BUSINESS VALUE
# ==========================================================

st.markdown("## 💼 Business Value")

st.markdown("""
<div style="
background:white;
padding:30px;
border-radius:20px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
">

Loan default prediction is one of the most important applications of
machine learning in banking and finance.

This dashboard helps financial institutions:

✔ Identify risky loan applicants.

✔ Reduce financial losses.

✔ Improve lending decisions.

✔ Support explainable AI through feature importance.

✔ Provide faster and more consistent credit risk assessment.

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# QUICK STATS
# ==========================================================

st.markdown("## 📈 Project Statistics")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Rows", "396,030")

with m2:
    st.metric("Columns", "49")

with m3:
    st.metric("Models", "4")

with m4:
    st.metric("Deployment", "Streamlit")

st.write("")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown("""
<div style="
background:#0F172A;
padding:30px;
border-radius:20px;
text-align:center;
color:white;
">

<h2 style="color:white;">
🏦 Loan Portfolio Status Prediction & Analytics
</h2>

<p style="font-size:17px;color:#CBD5E1;">

End-to-End Machine Learning Project

</p>

<p style="color:#94A3B8;">

Developed using Python • Scikit-Learn • Streamlit • Random Forest

</p>

</div>
""", unsafe_allow_html=True)