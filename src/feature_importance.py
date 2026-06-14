import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/gwas_ml_dataset.csv")

target = "fruitWeight (g)"

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=500,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

importance = pd.DataFrame({
    "SNP": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 20 SNPs")
print(importance.head(20))

os.makedirs("outputs", exist_ok=True)

importance.to_csv(
    "outputs/fruitweight_importance.csv",
    index=False
)

print("\nSaved: outputs/fruitweight_importance.csv")