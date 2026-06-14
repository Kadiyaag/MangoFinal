import joblib
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mango Genomics Dashboard",
    layout="wide"
)

st.title("🥭 Mango Genomics Dashboard")
st.write(
    "GWAS + Machine Learning Based Prediction of Mango Traits"
)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/gwas_ml_dataset.csv"
)

importance = pd.read_csv(
    "outputs/fruitweight_importance.csv"
)

multi_trait = pd.read_csv(
    "outputs/multi_trait_results.csv"
)

pca = pd.read_csv(
    "outputs/pca_coordinates.csv"
)

similarity = pd.read_csv(
    "outputs/mango_similarity.csv",
    index_col=0
)



traits = [
    "fruitWeight (g)",
    "fruitLength (mm)",
    "fruitWidth (mm)",
    "fruitThickness (mm)",
    "stoneWeight (g)",
    "stoneLength (mm)",
    "stoneWidth (mm)",
    "stoneThickness (mm)",
    "seedWeight (g)",
    "seedLength (mm)",
    "seedWidth (mm)",
    "seedThickness (mm)",
    "brix",
    "Pulp"
]

snp_cols = [
    c
    for c in df.columns
    if c.startswith("NC_")
]

# ==========================================
# ACCESSION SELECTOR
# ==========================================

st.header("Select Mango Accession")

accession = st.selectbox(
    "Choose a Mango Variety",
    sorted(df["Accession ID"].unique())
)

# ==========================================
# PREDICT BUTTON
# ==========================================

if st.button("Predict Traits"):

    row = df[
        df["Accession ID"] == accession
    ]

    X = row[snp_cols]

    predictions = {}

    for trait in traits:

        filename = (
            "models/"
            + trait.replace("/", "_")
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
            + ".pkl"
        )

        model = joblib.load(filename)

        pred = model.predict(X)[0]

        predictions[trait] = round(
            float(pred),
            2
        )

    results = pd.DataFrame({
        "Trait": predictions.keys(),
        "Predicted Value": predictions.values()
    })

    # ==========================================
    # TABLE
    # ==========================================

    st.success(
        f"Predictions for {accession}"
    )

    st.dataframe(
        results,
        use_container_width=True
    )

    # ==========================================
    # RADAR CHART
    # ==========================================

    st.header("Trait Profile")

    radar = go.Figure()

    radar.add_trace(
        go.Scatterpolar(
            r=results["Predicted Value"],
            theta=results["Trait"],
            fill="toself",
            name=accession
        )
    )

    radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            )
        ),
        showlegend=False,
        height=700
    )

    st.plotly_chart(
        radar,
        use_container_width=True
    )

    # ==========================================
    # COMPARE WITH POPULATION
    # ==========================================

    st.header(
        "Predicted vs Population Average"
    )

    avg_traits = {}

    for trait in traits:
        avg_traits[trait] = (
            df[trait].mean()
        )

    comparison = pd.DataFrame({
        "Trait": traits,
        "Prediction": results[
            "Predicted Value"
        ],
        "Population Average": [
            avg_traits[t]
            for t in traits
        ]
    })

    comparison_long = comparison.melt(
        id_vars="Trait",
        var_name="Type",
        value_name="Value"
    )

    fig = px.bar(
        comparison_long,
        x="Trait",
        y="Value",
        color="Type",
        barmode="group",
        title="Prediction vs Population Average"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# # ==========================================
# SNP IMPORTANCE
# ==========================================

st.header(
    "Top SNP Markers Influencing Fruit Weight"
)

top10 = importance.head(10)

fig2 = px.bar(
    top10,
    x="Importance",
    y="SNP",
    orientation="h",
    title="Top 10 Important SNPs"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# TRAIT PREDICTABILITY
# ==========================================

st.header(
    "Trait Predictability from GWAS SNPs"
)

fig3 = px.bar(
    multi_trait.sort_values(
        "Mean_R2"
    ),
    x="Mean_R2",
    y="Trait",
    orientation="h",
    color="Mean_R2",
    title="Cross-Validated Prediction Accuracy"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# MANGO ANCESTRY EXPLORER
# ==========================================

st.header("🌳 Mango Genetic Ancestry Explorer")

st.write(
    """
    PCA reduces 135,079 SNP markers into two dimensions.
    Mango varieties that appear close together are
    genetically more similar.
    """
)

selected_mango = st.selectbox(
    "Select Mango for Ancestry Analysis",
    sorted(pca["Accession"].unique())
)

fig4 = px.scatter(
    pca,
    x="PC1",
    y="PC2",
    hover_name="Accession",
    title="Mango Genetic Ancestry Map"
)

selected_point = pca[
    pca["Accession"] == selected_mango
]

fig4.add_scatter(
    x=selected_point["PC1"],
    y=selected_point["PC2"],
    mode="markers",
    marker=dict(
        size=18,
        symbol="star"
    ),
    name="Selected Mango"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ==========================================
# CLOSEST RELATIVES
# ==========================================

st.header("🧬 Closest Genetic Relatives")

closest = (
    similarity[selected_mango]
    .sort_values(
        ascending=False
    )
    .iloc[1:11]
)

relative_df = pd.DataFrame({
    "Relative": closest.index,
    "Similarity Score": closest.values
})

st.dataframe(
    relative_df,
    use_container_width=True
)

fig5 = px.bar(
    relative_df,
    x="Similarity Score",
    y="Relative",
    orientation="h",
    title=f"Top 10 Closest Relatives of {selected_mango}"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# ==========================================
# GENETIC NEIGHBORHOOD
# ==========================================

st.header("📍 Local Genetic Neighborhood")

top5 = relative_df.head(5)

cluster_points = pca[
    pca["Accession"].isin(
        list(top5["Relative"])
        + [selected_mango]
    )
]

fig6 = px.scatter(
    cluster_points,
    x="PC1",
    y="PC2",
    color="Accession",
    hover_name="Accession",
    title=f"Genetic Neighborhood of {selected_mango}"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

# ==========================================
# RESEARCH SUMMARY
# ==========================================

st.header("Project Findings")

best_trait = multi_trait.iloc[
    multi_trait["Mean_R2"].idxmax()
]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Best Predicted Trait",
        best_trait["Trait"]
    )

with col2:
    st.metric(
        "Best R²",
        round(
            best_trait["Mean_R2"],
            3
        )
    )

st.info(
    """
    Key Findings:

    • 135,079 SNPs were processed

    • GWAS reduced them to 260 significant SNPs

    • XGBoost was used for genomic prediction

    • Stone Length showed highest predictability

    • Fruit Weight achieved R² ≈ 0.38

    • Multiple GWAS SNPs were confirmed by machine learning

    • PCA and similarity analysis were used to explore
      genetic relationships among mango accessions
    """
)