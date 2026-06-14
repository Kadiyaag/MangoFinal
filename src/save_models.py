import os
import joblib
import pandas as pd

from xgboost import XGBRegressor

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/gwas_ml_dataset.csv")

traits = [
    "fruitWeight (g)",
    "fruitLength (mm)",
    "fruitWidth (mm)",
    "fruitThickness (mm)",
    "stoneWeight (g)",
    "stoneLength (mm)",
    "stoneWidth (mm)",
    "stoneThickness (mm)",
    "seedWeight (g)",
    "seedLength (mm)",
    "seedWidth (mm)",
    "seedThickness (mm)",
    "brix",
    "Pulp"
]

snp_cols = [c for c in df.columns if c.startswith("NC_")]

X = df[snp_cols]

for trait in traits:

    temp = df[[trait] + snp_cols].dropna()

    X_trait = temp[snp_cols]
    y_trait = temp[trait]

    model = XGBRegressor(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        random_state=42
    )

    model.fit(X_trait, y_trait)

    filename = (
        "models/"
        + trait.replace("/", "_")
        .replace(" ", "_")
        .replace("(", "")
        .replace(")", "")
        + ".pkl"
    )

    joblib.dump(model, filename)

    print("Saved:", filename)