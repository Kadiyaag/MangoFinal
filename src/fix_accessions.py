import pandas as pd

pheno = pd.read_csv("data/phenotype_clean.csv")
snp = pd.read_csv("data/snp_clean.csv")

# phenotype accession IDs
pheno["Accession ID"] = (
    pheno["Accession ID"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# SNP column names
new_cols = []

for c in snp.columns:
    c = str(c).strip().lower()

    if "unnamed" in c:
        continue

    new_cols.append(c)

# keep rs# + accession columns
snp = snp.loc[:, ~snp.columns.str.contains("Unnamed", case=False)]

snp.columns = (
    pd.Series(snp.columns)
    .astype(str)
    .str.strip()
    .str.lower()
)

pheno.to_csv("data/phenotype_final.csv", index=False)
snp.to_csv("data/snp_final.csv", index=False)

print("Saved final cleaned files")