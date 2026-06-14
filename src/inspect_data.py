import pandas as pd

phenotype = pd.read_excel(
    "data/TableS1.xlsx",
    sheet_name=0,
    header=1
)

snp = pd.read_excel(
    "data/TableS2.xlsx",
    sheet_name=0,
    header=1
)

print("\nPHENOTYPE")
print(phenotype.head())

print("\nColumns:")
print(list(phenotype.columns))

print("\nSNP")
print(snp.head())

print("\nColumns:")
print(list(snp.columns[:10]))