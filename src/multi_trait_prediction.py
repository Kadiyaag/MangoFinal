import pandas as pd

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from xgboost import XGBRegressor

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

results = []

for trait in traits:

    print(f"\nRunning {trait}")

    temp = df[[trait] + snp_cols].copy()

    # Remove rows where target is missing
    temp = temp.dropna(subset=[trait])

    X = temp[snp_cols]
    y = temp[trait]

    model = XGBRegressor(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        random_state=42
    )

    scores = cross_val_score(
        model,
        X,
        y,
        cv=KFold(
            n_splits=5,
            shuffle=True,
            random_state=42
        ),
        scoring="r2"
    )

    results.append([
        trait,
        len(temp),
        scores.mean(),
        scores.std()
    ])

results = pd.DataFrame(
    results,
    columns=[
        "Trait",
        "Samples",
        "Mean_R2",
        "Std_R2"
    ]
)

results = results.sort_values(
    by="Mean_R2",
    ascending=False
)

print("\nRESULTS")
print(results)

results.to_csv(
    "outputs/multi_trait_results.csv",
    index=False
)

print("\nSaved outputs/multi_trait_results.csv")