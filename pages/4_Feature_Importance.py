import pandas as pd
import streamlit as st

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="Feature Importance",
    page_icon="🎯",
    layout="wide"
)

# --------------------------------------------------------
# Load Data
# --------------------------------------------------------

importance = pd.read_csv(
    "reports/feature_importance.csv"
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
Feature Importance Analysis
</h1>

<p style="
color:#DBEAFE;
font-size:18px;
line-height:1.7;
">

Explainable Artificial Intelligence (XAI) helps us understand how the
Random Forest model makes its predictions.

This page highlights the features that contributed the most to loan
repayment prediction.

</p>

</div>
""",
unsafe_allow_html=True)

# --------------------------------------------------------
# KPI Cards
# --------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Model",
        "Random Forest"
    )

with c2:
    st.metric(
        "Total Features",
        len(importance)
    )

with c3:
    st.metric(
        "Top Features",
        "10"
    )

with c4:
    st.metric(
        "Explainability",
        "High"
    )

st.markdown("---")

# --------------------------------------------------------
# Feature Importance Plot
# --------------------------------------------------------

st.markdown("## Feature Importance Visualization")

st.write("""
The chart below illustrates the contribution of each feature to the
Random Forest prediction process.
""")

st.image(
    "images/feature_importance.png",
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------------
# Feature Ranking
# --------------------------------------------------------

st.markdown("## Complete Feature Ranking")

st.dataframe(
    importance,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# --------------------------------------------------------
# Top Features
# --------------------------------------------------------

st.markdown("## Top 10 Most Influential Features")

st.success("""
The following variables had the greatest impact on the model's ability
to distinguish between **Fully Paid** and **Charged Off** loans.
""")

st.dataframe(
    importance.head(10),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# --------------------------------------------------------
# Important Risk Indicators
# --------------------------------------------------------

st.markdown("## Major Risk Indicators")

left, right = st.columns(2)

with left:

    st.success("""

### Financial Indicators

✔ Interest Rate

✔ Loan Amount

✔ Annual Income

✔ Debt-To-Income Ratio

✔ Revolving Utilization

✔ Revolving Balance

""")

with right:

    st.info("""

### Credit Profile

✔ Grade

✔ Sub Grade

✔ Employment Length

✔ Total Accounts

✔ Open Accounts

✔ Mortgage Accounts

""")

st.markdown("---")

# --------------------------------------------------------
# Business Interpretation
# --------------------------------------------------------

st.markdown("## Business Interpretation")

st.write("""

Feature Importance provides transparency by identifying which borrower
characteristics most strongly influence the machine learning model.

For this project, financial variables such as **Interest Rate**,
**Loan Amount**, **Debt-To-Income Ratio**, and **Annual Income**
play a significant role in determining repayment behavior.

Credit history variables including **Grade**, **Sub Grade**, and
**Revolving Utilization** further improve prediction accuracy.

These insights help financial institutions:

- Identify high-risk loan applicants
- Improve lending strategies
- Reduce credit losses
- Support explainable AI
- Increase trust in machine learning predictions

""")

st.markdown("---")

# --------------------------------------------------------
# Explainable AI
# --------------------------------------------------------

st.markdown("## Why Feature Importance Matters")

c1, c2 = st.columns(2)

with c1:

    st.info("""

### For Data Scientists

• Validate model behavior

• Detect bias

• Improve feature engineering

• Interpret predictions

""")

with c2:

    st.info("""

### For Business Teams

• Better lending policies

• Transparent decision making

• Risk assessment

• Regulatory compliance

""")

st.markdown("---")

# --------------------------------------------------------
# Conclusion
# --------------------------------------------------------

st.markdown("## Conclusion")

st.success("""

The Random Forest model demonstrates strong predictive performance while
remaining interpretable through Feature Importance analysis.

Understanding which variables influence predictions allows financial
institutions to build more transparent, reliable and trustworthy
loan approval systems.

""")

st.markdown("---")

# --------------------------------------------------------
# Footer
# --------------------------------------------------------

st.markdown("""
<div style="
background:#F8FAFC;
padding:20px;
border-radius:15px;
text-align:center;
">

<h3 style="color:#2563EB;">
Explainable Machine Learning
</h3>

<p>

Feature Importance makes machine learning models easier to understand,
trust and deploy in real-world financial applications.

</p>

</div>
""",
unsafe_allow_html=True)