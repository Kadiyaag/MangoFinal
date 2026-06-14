import pandas as pd

print("Loading cleaned files...")

pheno = pd.read_csv("data/phenotype_clean.csv")
snp = pd.read_csv("data/snp_clean.csv")

print("Phenotype:", pheno.shape)
print("SNP:", snp.shape)

# ----------------------------------
# TRANSPOSE SNP MATRIX
# ----------------------------------

print("\nTransposing SNP matrix...")

snp_t = snp.set_index("rs#").T

snp_t.reset_index(inplace=True)

snp_t.rename(
    columns={"index": "Accession ID"},
    inplace=True
)

print("Transposed SNP shape:")
print(snp_t.shape)

# ----------------------------------
# MERGE
# ----------------------------------

print("\nMerging phenotype + SNP")

merged = pd.merge(
    pheno,
    snp_t,
    on="Accession ID"
)

print("Merged shape:")
print(merged.shape)

merged.to_csv(
    "data/ml_dataset.csv",
    index=False
)

print("\nSaved:")
print("data/ml_dataset.csv")