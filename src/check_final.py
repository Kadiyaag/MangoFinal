import pandas as pd

pheno = pd.read_csv("data/phenotype_final.csv")

pheno["Accession ID"] = (
    pheno["Accession ID"]
    .replace({
        "tommyatkins": "o.p.tommyatkins"
    })
)

pheno.to_csv("data/phenotype_final.csv", index=False)

print("TommyAtkins fixed")