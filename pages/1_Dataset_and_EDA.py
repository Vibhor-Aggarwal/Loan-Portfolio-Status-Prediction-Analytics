import os
import pandas as pd
import streamlit as st

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="Dataset & Exploratory Data Analysis",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------------
# Load CSS
# --------------------------------------------------------

def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# --------------------------------------------------------
# Load Dataset
# --------------------------------------------------------

DATA_PATH = "data/processed/cleaned_data.csv"

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------------
# Hero Banner
# --------------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(135deg,#1E3A8A,#2563EB);
padding:35px;
border-radius:20px;
margin-bottom:30px;
">

<h1 style="color:white;">
Dataset & Exploratory Data Analysis
</h1>

<p style="
color:#DBEAFE;
font-size:18px;
line-height:1.7;
">

Explore the Lending Club loan dataset, understand its structure,
analyze important financial variables, and discover insights that
drive loan repayment prediction.

</p>

</div>
""",
unsafe_allow_html=True)

# --------------------------------------------------------
# Dashboard Cards
# --------------------------------------------------------

def card(title,value,color):

    st.markdown(
        f"""
        <div style="
        background:white;
        border-left:6px solid {color};
        padding:20px;
        border-radius:15px;
        box-shadow:0px 6px 18px rgba(0,0,0,0.08);
        ">

        <h4 style="margin-bottom:5px;color:#64748B;">
        {title}
        </h4>

        <h1 style="margin:0;color:#0F172A;">
        {value}
        </h1>

        </div>
        """,
        unsafe_allow_html=True
    )

c1,c2,c3,c4 = st.columns(4)

with c1:
    card(
        "Loan Records",
        f"{df.shape[0]:,}",
        "#2563EB"
    )

with c2:
    card(
        "Features",
        df.shape[1],
        "#059669"
    )

with c3:
    card(
        "Missing Values",
        int(df.isnull().sum().sum()),
        "#DC2626"
    )

with c4:
    card(
        "Duplicate Rows",
        int(df.duplicated().sum()),
        "#D97706"
    )

st.markdown("<br>",unsafe_allow_html=True)

# --------------------------------------------------------
# Dataset Overview
# --------------------------------------------------------

left,right = st.columns([2,1])

with left:

    st.markdown("## Dataset Overview")

    st.write("""

The Lending Club dataset contains historical loan applications collected
from borrowers applying for personal loans.

Each record contains applicant information, financial indicators,
credit history and loan characteristics that help determine whether
the borrower successfully repaid the loan.

The cleaned dataset is used throughout this project for machine learning,
feature engineering and loan risk prediction.

""")

with right:

    st.info("""

### Dataset Information

**Source**

Lending Club

---

**Problem**

Binary Classification

---

**Target**

loan_status

---

**Records**

396,000+

---

**Features**

49

""")

st.markdown("---")

# --------------------------------------------------------
# Sample Dataset
# --------------------------------------------------------

st.markdown("## Sample Loan Records")

st.write(
"Preview of the cleaned dataset used throughout the machine learning pipeline."
)

st.dataframe(
    df.head(10),
    use_container_width=True,
    height=420
)

st.markdown("---")

# --------------------------------------------------------
# Feature Summary
# --------------------------------------------------------

st.markdown("## Feature Summary")

summary = pd.DataFrame({

    "Feature":df.columns,

    "Data Type":df.dtypes.astype(str),

    "Missing Values":df.isnull().sum().values,

    "Unique Values":df.nunique().values

})

st.dataframe(
    summary,
    use_container_width=True,
    height=500
)

st.markdown("---")

# --------------------------------------------------------
# Statistical Summary
# --------------------------------------------------------

st.markdown("## Descriptive Statistics")

st.write(
"Summary statistics for all numerical variables after data cleaning."
)

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------------
# Exploratory Data Analysis
# --------------------------------------------------------

st.markdown("## Visual Exploratory Data Analysis")

st.info(
"""
The following visualizations were generated during the Exploratory Data
Analysis phase to better understand feature distributions, relationships,
loan repayment behaviour and borrower characteristics.
"""
)

# --------------------------------------------------------
# Load EDA Images
# --------------------------------------------------------

IMAGE_FOLDER = "images"

if os.path.exists(IMAGE_FOLDER):

    image_files = sorted([
        file
        for file in os.listdir(IMAGE_FOLDER)
        if file.endswith(".png")
    ])

    for i in range(0, len(image_files), 2):

        col1, col2 = st.columns(2)

        with col1:

            image_path = os.path.join(
                IMAGE_FOLDER,
                image_files[i]
            )

            st.image(
                image_path,
                caption=image_files[i]
                .replace("_", " ")
                .replace(".png", "")
                .title(),
                use_container_width=True
            )

        if i + 1 < len(image_files):

            with col2:

                image_path = os.path.join(
                    IMAGE_FOLDER,
                    image_files[i + 1]
                )

                st.image(
                    image_path,
                    caption=image_files[i + 1]
                    .replace("_", " ")
                    .replace(".png", "")
                    .title(),
                    use_container_width=True
                )

else:

    st.warning(
        "EDA images folder not found."
    )

# --------------------------------------------------------
# Business Insights
# --------------------------------------------------------

st.markdown("---")

st.markdown("## Business Insights")

left, right = st.columns([2,1])

with left:

    st.success("""

### Key Findings

✔ The dataset contains nearly **400,000 historical loan applications**.

✔ Financial variables such as interest rate, annual income,
loan amount and debt-to-income ratio strongly influence repayment.

✔ Both categorical and numerical variables are available,
making feature engineering an important preprocessing step.

✔ Loan repayment behaviour depends on multiple borrower
characteristics rather than a single feature.

✔ Proper preprocessing significantly improves model performance.

✔ Exploratory Data Analysis helped identify trends,
relationships and potential predictors before training
machine learning models.

""")

with right:

    st.info("""

### Dataset Quality

Dataset Size

396K+ Records

---

Missing Values

Minimal after Cleaning

---

Duplicates

Removed

---

Ready for ML

Yes

""")

# --------------------------------------------------------
# Feature Categories
# --------------------------------------------------------

st.markdown("---")

st.markdown("## Feature Categories")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("""

### Applicant Information

• Annual Income

• Employment Length

• Home Ownership

• Verification Status

""")

with c2:

    st.info("""

### Loan Information

• Loan Amount

• Interest Rate

• Installment

• Loan Term

• Purpose

""")

with c3:

    st.info("""

### Credit History

• Revolving Balance

• Open Accounts

• Total Accounts

• Public Records

""")

# --------------------------------------------------------
# Why EDA Matters
# --------------------------------------------------------

st.markdown("---")

st.markdown("## Why Exploratory Data Analysis Matters")

st.write("""

Exploratory Data Analysis (EDA) is one of the most important stages
of every machine learning project.

It helps understand the dataset before model training by identifying:

- Missing values

- Outliers

- Feature distributions

- Relationships between variables

- Class imbalance

- Trends and hidden patterns

These insights guide preprocessing, feature engineering,
algorithm selection and model optimization.

""")

# --------------------------------------------------------
# Conclusion
# --------------------------------------------------------

st.markdown("---")

st.markdown("## Conclusion")

st.success("""

The Lending Club dataset provides rich financial and borrower
information that enables accurate loan risk prediction.

After cleaning and preprocessing, the dataset becomes suitable
for machine learning algorithms capable of distinguishing between
loans that are likely to be Fully Paid and those at higher risk
of being Charged Off.

The next pages demonstrate preprocessing techniques,
model comparison, feature importance analysis and
interactive loan prediction.

""")

# --------------------------------------------------------
# Footer
# --------------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div style="
text-align:center;
padding:20px;
background:#F8FAFC;
border-radius:15px;
">

<h3 style="color:#2563EB;">
Dataset & Exploratory Data Analysis
</h3>

<p>
Understanding the data is the first step toward building reliable
machine learning models.
</p>

</div>
""",
unsafe_allow_html=True
)