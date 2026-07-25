import pandas as pd
import streamlit as st

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------------
# Load Data
# --------------------------------------------------------

comparison = pd.read_csv(
    "reports/model_comparison.csv"
)

tuning = pd.read_csv(
    "reports/hyperparameter_results.csv"
)

# --------------------------------------------------------
# Hero Section
# --------------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(135deg,#1E3A8A,#2563EB);
padding:35px;
border-radius:18px;
margin-bottom:30px;
">

<h1 style="color:white;">
Machine Learning Model Performance
</h1>

<p style="
color:#DBEAFE;
font-size:18px;
line-height:1.7;
">

Multiple machine learning algorithms were trained and evaluated for
loan repayment prediction.

The final Random Forest model was selected after extensive comparison
and hyperparameter optimization.

</p>

</div>
""",
unsafe_allow_html=True)

# --------------------------------------------------------
# KPI Cards
# --------------------------------------------------------

best_accuracy = comparison["Accuracy"].max()
best_f1 = comparison["F1 Score"].max()

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Models Compared",
        len(comparison)
    )

with c2:
    st.metric(
        "Best Model",
        "Random Forest"
    )

with c3:
    st.metric(
        "Accuracy",
        f"{best_accuracy:.4f}"
    )

with c4:
    st.metric(
        "F1 Score",
        f"{best_f1:.4f}"
    )

st.markdown("---")

# --------------------------------------------------------
# Model Comparison
# --------------------------------------------------------

st.markdown("## Model Comparison")

st.write("""
The following table compares the performance of all machine learning
models evaluated during this project.
""")

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# --------------------------------------------------------
# Best Model
# --------------------------------------------------------

left,right = st.columns([2,1])

with left:

    st.markdown("## Selected Model")

    st.success("""

### Random Forest Classifier

The Random Forest model achieved the strongest overall performance.

Reasons for selection:

✔ Highest Accuracy

✔ Strong Precision

✔ High Recall

✔ Best F1 Score

✔ Excellent Generalization

✔ Robust against overfitting

✔ Suitable for financial risk prediction

""")

with right:

    st.info("""

### Final Algorithm

Random Forest

---

Problem Type

Binary Classification

---

Target

loan_status

---

Deployment

Streamlit

""")

st.markdown("---")

# --------------------------------------------------------
# Hyperparameter Tuning
# --------------------------------------------------------

st.markdown("## Hyperparameter Tuning")

st.write("""

Randomized Search Cross Validation was used to optimize the
Random Forest classifier.

The tuning process evaluated multiple parameter combinations
to maximize predictive performance.

""")

st.dataframe(
    tuning,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# --------------------------------------------------------
# Model Development Pipeline
# --------------------------------------------------------

st.markdown("## Machine Learning Pipeline")

st.info("""

1️⃣ Data Cleaning

⬇

2️⃣ Feature Engineering

⬇

3️⃣ Data Preprocessing

⬇

4️⃣ Train-Test Split

⬇

5️⃣ SMOTE Oversampling

⬇

6️⃣ Model Training

⬇

7️⃣ Hyperparameter Tuning

⬇

8️⃣ Model Evaluation

⬇

9️⃣ Best Model Selection

⬇

🔟 Deployment using Streamlit

""")

st.markdown("---")

# --------------------------------------------------------
# Evaluation Metrics
# --------------------------------------------------------

st.markdown("## Evaluation Metrics")

m1,m2,m3,m4 = st.columns(4)

with m1:

    st.success("""

### Accuracy

Overall prediction correctness.

""")

with m2:

    st.success("""

### Precision

Correct positive predictions.

""")

with m3:

    st.success("""

### Recall

Ability to detect risky loans.

""")

with m4:

    st.success("""

### F1 Score

Balance of Precision & Recall.

""")

st.markdown("---")

# --------------------------------------------------------
# Business Value
# --------------------------------------------------------

st.markdown("## Business Value")

left,right = st.columns(2)

with left:

    st.success("""

### Benefits

✔ Reduce loan defaults

✔ Improve lending decisions

✔ Lower financial losses

✔ Better credit risk assessment

✔ Faster application screening

✔ Data-driven decision making

""")

with right:

    st.warning("""

### Why Random Forest?

• Handles nonlinear relationships

• Works well with mixed data

• Robust to noise

• Excellent predictive accuracy

• Provides feature importance

• Easy to deploy

""")

st.markdown("---")

# --------------------------------------------------------
# Project Conclusion
# --------------------------------------------------------

st.markdown("## Project Conclusion")

st.write("""

After comparing multiple machine learning algorithms and performing
hyperparameter tuning, the Random Forest classifier demonstrated the
best overall balance between Accuracy, Precision, Recall and F1 Score.

Its ability to capture complex relationships between borrower
characteristics makes it highly suitable for loan default prediction.

The trained model was deployed within this interactive Streamlit
dashboard, enabling real-time loan repayment prediction and
business-friendly decision support.

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
Model Evaluation Completed
</h3>

<p>

The Random Forest classifier was selected as the final production
model after extensive experimentation and optimization.

</p>

</div>
""",
unsafe_allow_html=True)