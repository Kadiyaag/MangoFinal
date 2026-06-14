import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

from xgboost import XGBRegressor

print("Loading data...")

df = pd.read_csv("data/gwas_ml_dataset.csv")

target = "fruitWeight (g)"

snp_cols = [c for c in df.columns if c.startswith("NC_")]

X = df[snp_cols]

y = df[target]

print("Features:", X.shape)
print("Target:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    random_state=42
)

print("Training XGBoost...")

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nRESULTS")

print("R2:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))
print("RMSE:", mean_squared_error(
    y_test,
    pred
) ** 0.5)