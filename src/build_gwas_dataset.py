import pandas as pd

print("Loading files...")

# IMPORTANT
pheno = pd.read_csv("data/phenotype_final.csv")

snp = pd.read_csv("data/snp_encoded.csv")

selected = pd.read_csv("data/selected_snps.csv")

selected_snps = set(selected["SNP"])

# Keep GWAS SNPs only
gwas_snp = snp[snp["rs#"].isin(selected_snps)]

print("GWAS SNP rows:", gwas_snp.shape)

# Transpose
gwas_snp = gwas_snp.set_index("rs#").T
gwas_snp.index.name = "Accession ID"
gwas_snp.reset_index(inplace=True)

# Normalize both sides
pheno["Accession ID"] = (
    pheno["Accession ID"]
    .astype(str)
    .str.strip()
    .str.lower()
)

gwas_snp["Accession ID"] = (
    gwas_snp["Accession ID"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# Merge
dataset = pd.merge(
    pheno,
    gwas_snp,
    on="Accession ID",
    how="inner"
)

print("Final shape:", dataset.shape)

dataset.to_csv(
    "data/gwas_ml_dataset.csv",
    index=False
)

print("Saved gwas_ml_dataset.csv")