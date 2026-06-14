import pandas as pd
import networkx as nx

similarity = pd.read_csv(
    "outputs/mango_similarity.csv",
    index_col=0
)

G = nx.Graph()

threshold = 0.95

for i in similarity.index:

    G.add_node(i)

for i in similarity.index:

    for j in similarity.columns:

        if i != j:

            score = similarity.loc[i,j]

            if score > threshold:

                G.add_edge(
                    i,
                    j,
                    weight=score
                )

nx.write_gexf(
    G,
    "outputs/mango_network.gexf"
)