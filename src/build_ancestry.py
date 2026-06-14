import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("Loading SNP data...")

snp = pd.read_csv(
    "data/snp_encoded.csv"
)

# transpose
snp_t = snp.set_index(
    "rs#"
).T

similarity = cosine_similarity(
    snp_t
)

similarity_df = pd.DataFrame(
    similarity,
    index=snp_t.index,
    columns=snp_t.index
)

similarity_df.to_csv(
    "outputs/mango_similarity.csv"
)

print("Saved mango_similarity.csv")