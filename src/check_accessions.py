import pandas as pd

pheno = pd.read_csv("data/phenotype_clean.csv")
snp = pd.read_csv("data/snp_clean.csv")

pheno_ids = set(pheno["Accession ID"].dropna().astype(str))
snp_ids = set(pd.Index(snp.columns[1:]).dropna().astype(str))

print("\nIn phenotype but not SNP:")
for x in pheno_ids - snp_ids:
    print(x)

print("\nIn SNP but not phenotype:")
for x in snp_ids - pheno_ids:
    print(x)