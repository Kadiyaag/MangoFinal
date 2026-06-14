import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

print("Loading dataset...")

df = pd.read_csv("data/gwas_ml_dataset.csv")

target = "fruitWeight (g)"

# Remove ALL phenotype traits
non_snp_columns = [
    "Accession ID",
    "Subpopulation",

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

X = df.drop(columns=non_snp_columns)

y = df[target]

print("SNP Feature Matrix:", X.shape)
print("Target:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Random Forest...")

model = RandomForestRegressor(
    n_estimators=500,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nRESULTS")

print("R2:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))
print(
    "RMSE:",
    mean_squared_error(y_test, pred) ** 0.5
)