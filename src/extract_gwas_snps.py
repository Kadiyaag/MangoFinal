import pandas as pd

# Load GWAS results
farm = pd.read_excel(
    "data/TableS1.xlsx",
    sheet_name=" Table S3",
    header=2
)

glm = pd.read_excel(
    "data/TableS1.xlsx",
    sheet_name=" Table S4",
    header=1
)

# Remove extra spaces in column names
farm.columns = farm.columns.str.strip()
glm.columns = glm.columns.str.strip()

# Extract SNP names
farm_snps = set(farm["SNP"].astype(str))
glm_snps = set(glm["SNP"].astype(str))

# Union of both methods
selected_snps = sorted(farm_snps | glm_snps)

print("FarmCPU SNPs:", len(farm_snps))
print("GLM SNPs:", len(glm_snps))
print("Unique SNPs:", len(selected_snps))

# Save
pd.DataFrame({"SNP": selected_snps}).to_csv(
    "data/selected_snps.csv",
    index=False
)

print("\nSaved: data/selected_snps.csv")