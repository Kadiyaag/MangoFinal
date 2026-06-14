import pandas as pd

from sklearn.decomposition import PCA

snp = pd.read_csv(
    "data/snp_encoded.csv"
)

snp_t = snp.set_index(
    "rs#"
).T

pca = PCA(
    n_components=2
)

coords = pca.fit_transform(
    snp_t
)

pca_df = pd.DataFrame({
    "Accession": snp_t.index,
    "PC1": coords[:,0],
    "PC2": coords[:,1]
})

pca_df.to_csv(
    "outputs/pca_coordinates.csv",
    index=False
)