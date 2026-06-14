import pandas as pd
import numpy as np

print("Loading SNP data...")

snp = pd.read_csv("data/snp_final.csv")

print("Original shape:", snp.shape)

encoding = {
    "A": 0,
    "T": 1,
    "C": 2,
    "G": 3,
    "R": 4,
    "Y": 5,
    "M": 6,
    "K": 7,
    "W": 8,
    "S": 9,
    "N": -1
}

# SNP IDs
snp_ids = snp["rs#"]

# SNP values only
snp_values = snp.drop(columns=["rs#"])

print("Encoding alleles...")

snp_encoded = snp_values.replace(encoding)

# Put SNP IDs back
snp_encoded.insert(0, "rs#", snp_ids)

print("Encoded shape:", snp_encoded.shape)

snp_encoded.to_csv(
    "data/snp_encoded.csv",
    index=False
)

print("Saved: data/snp_encoded.csv")