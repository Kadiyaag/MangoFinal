import pandas as pd

print("Loading phenotype...")
phenotype = pd.read_excel(
    "data/TableS1.xlsx",
    sheet_name=" Table S1"
)

print("Loading FarmCPU...")
farmcpu = pd.read_excel(
    "data/TableS1.xlsx",
    sheet_name=" Table S3"
)

print("Loading GLM...")
glm = pd.read_excel(
    "data/TableS1.xlsx",
    sheet_name=" Table S4"
)

print("Loading SNPs...")
snp = pd.read_excel(
    "data/TableS2.xlsx",
    sheet_name="Sheet1"
)

print("\nLoaded successfully!")

print("Phenotype shape:", phenotype.shape)
print("FarmCPU shape:", farmcpu.shape)
print("GLM shape:", glm.shape)
print("SNP shape:", snp.shape)