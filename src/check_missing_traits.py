import pandas as pd

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

for trait in traits:
    missing = df[trait].isna().sum()
    print(f"{trait}: {missing}")