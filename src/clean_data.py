import pandas as pd

# ==========================
# LOAD RAW FILES
# ==========================

pheno_raw = pd.read_excel(
    "data/TableS1.xlsx",
    sheet_name=0,
    header=1
)

snp_raw = pd.read_excel(
    "data/TableS2.xlsx",
    sheet_name=0,
    header=1
)

# ==========================
# FIX PHENOTYPE TABLE
# ==========================

pheno = pheno_raw.copy()

# use first row as header
pheno.columns = pheno.iloc[0]

# remove header row from data
pheno = pheno.iloc[1:].reset_index(drop=True)

print("\nPHENOTYPE")
print(pheno.head())

print("\nPhenotype columns:")
print(list(pheno.columns))

# ==========================
# FIX SNP TABLE
# ==========================

snp = snp_raw.copy()

snp.columns = snp.iloc[0]

snp = snp.iloc[1:].reset_index(drop=True)

print("\nSNP")
print(snp.head())

print("\nSNP columns:")
print(list(snp.columns[:10]))

# ==========================
# SAVE CLEAN FILES
# ==========================

pheno.to_csv(
    "data/phenotype_clean.csv",
    index=False
)

snp.to_csv(
    "data/snp_clean.csv",
    index=False
)

print("\nSaved cleaned files!")