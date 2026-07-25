import joblib
import pandas as pd

MODEL = joblib.load("models/best_random_forest.pkl")
ENCODER = joblib.load("models/onehot_encoder.pkl")
SCALER = joblib.load("models/scaler.pkl")
FEATURE_COLUMNS = joblib.load("models/feature_columns.pkl")
NUMERICAL_COLUMNS = joblib.load("models/numerical_columns.pkl")

GRADE_MAPPING = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6
}

SUBGRADE_MAPPING = {}
index = 0

for grade in ["A", "B", "C", "D", "E", "F", "G"]:
    for number in range(1, 6):
        SUBGRADE_MAPPING[f"{grade}{number}"] = index
        index += 1

NOMINAL_COLUMNS = [
    "term",
    "home_ownership",
    "verification_status",
    "purpose",
    "initial_list_status",
    "application_type"
]


def preprocess_input(df: pd.DataFrame):

    df = df.copy()

    if "emp_title" in df.columns:
        df.drop(columns=["emp_title"], inplace=True)

    if "address" in df.columns:
        df.drop(columns=["address"], inplace=True)

    df["earliest_cr_year"] = (
        df["earliest_cr_line"]
        .str[-4:]
        .astype(int)
    )

    df.drop(columns=["earliest_cr_line"], inplace=True)

    issue_date = pd.to_datetime(
        df["issue_d"],
        format="%b-%Y"
    )

    df["issue_month"] = issue_date.dt.month
    df["issue_year"] = issue_date.dt.year

    df.drop(columns=["issue_d"], inplace=True)

    df["grade"] = df["grade"].map(GRADE_MAPPING)
    df["sub_grade"] = df["sub_grade"].map(SUBGRADE_MAPPING)

    encoded = ENCODER.transform(
        df[NOMINAL_COLUMNS]
    )

    encoded_df = pd.DataFrame(
        encoded,
        columns=ENCODER.get_feature_names_out(NOMINAL_COLUMNS),
        index=df.index
    )

    df.drop(columns=NOMINAL_COLUMNS, inplace=True)

    df = pd.concat(
        [df, encoded_df],
        axis=1
    )

    for column in FEATURE_COLUMNS:
        if column not in df.columns:
            df[column] = 0

    df = df[FEATURE_COLUMNS]

    df[NUMERICAL_COLUMNS] = SCALER.transform(
        df[NUMERICAL_COLUMNS]
    )

    return df


def predict(df: pd.DataFrame):

    processed = preprocess_input(df)

    prediction = MODEL.predict(processed)[0]

    probabilities = MODEL.predict_proba(processed)[0]

    confidence = probabilities[prediction]

    label = (
        "Charged Off"
        if prediction == 1
        else "Fully Paid"
    )

    return label, confidence