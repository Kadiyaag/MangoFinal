import pandas as pd

print("Loading files...")

pheno = pd.read_csv("data/phenotype_final.csv")
snp = pd.read_csv("data/snp_encoded.csv")

print("Transposing SNP matrix...")

snp_t = snp.set_index("rs#").T
snp_t.index.name = "Accession ID"
snp_t.reset_index(inplace=True)

# lower case for safe merge
pheno["Accession ID"] = (
    pheno["Accession ID"]
    .astype(str)
    .str.lower()
)

snp_t["Accession ID"] = (
    snp_t["Accession ID"]
    .astype(str)
    .str.lower()
)

print("Merging...")

ml = pd.merge(
    pheno,
    snp_t,
    on="Accession ID",
    how="inner"
)

print("Final ML shape:")
print(ml.shape)

ml.to_csv(
    "data/ml_ready.csv",
    index=False
)

print("Saved: data/ml_ready.csv")