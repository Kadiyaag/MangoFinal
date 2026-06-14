import pandas as pd

snp = pd.read_csv("data/snp_encoded.csv")

print(snp.head())

print("\nShape:")
print(snp.shape)