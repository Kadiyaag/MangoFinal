import pandas as pd

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from xgboost import XGBRegressor

df = pd.read_csv("data/gwas_ml_dataset.csv")

target = "fruitWeight (g)"

snp_cols = [c for c in df.columns if c.startswith("NC_")]

X = df[snp_cols]
y = df[target]

model = XGBRegressor(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    random_state=42
)

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=kf,
    scoring="r2"
)

print("Fold scores:")
print(scores)

print("\nMean R2:")
print(scores.mean())

print("\nStd:")
print(scores.std())