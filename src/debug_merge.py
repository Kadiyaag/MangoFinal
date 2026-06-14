import pandas as pd

pheno = pd.read_csv("data/phenotype_clean.csv")

snp = pd.read_csv("data/snp_encoded.csv")

selected = pd.read_csv("data/selected_snps.csv")

selected_snps = set(selected["SNP"])

gwas_snp = snp[snp["rs#"].isin(selected_snps)]

gwas_snp = gwas_snp.set_index("rs#").T
gwas_snp.index.name = "Accession ID"
gwas_snp.reset_index(inplace=True)

print("\nPHENOTYPE IDs")
print(pheno["Accession ID"].head(20).tolist())

print("\nSNP IDs")
print(gwas_snp["Accession ID"].head(20).tolist())