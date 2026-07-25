import pandas as pd
import joblib


def load_dataset():
    """Load cleaned dataset."""
    return pd.read_csv("data/processed/cleaned_data.csv")


def load_model():
    """Load the best trained model."""
    return joblib.load("models/best_random_forest.pkl")


def load_model_comparison():
    """Load model comparison report."""
    return pd.read_csv("reports/model_comparison.csv")


def load_feature_importance():
    """Load feature importance report."""
    return pd.read_csv("reports/feature_importance.csv")