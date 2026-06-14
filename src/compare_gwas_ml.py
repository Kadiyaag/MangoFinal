import pandas as pd

imp = pd.read_csv("outputs/fruitweight_importance.csv")

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

farm.columns = farm.columns.str.strip()
glm.columns = glm.columns.str.strip()

top20 = imp.head(20)

farm_snps = set(farm["SNP"].astype(str))
glm_snps = set(glm["SNP"].astype(str))

count = 0

for snp in top20["SNP"]:
    if snp in farm_snps or snp in glm_snps:
        count += 1

print("Confirmed SNPs:", count)
print("Percentage:", count / 20 * 100)