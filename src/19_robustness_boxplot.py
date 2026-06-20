import json
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

n = G.number_of_nodes()
r = int(0.05 * n)

T = 50

largest_components = []
num_components = []
avg_distances = []
isolated_fractions = []

for _ in range(T):

    H = G.copy()

    removed = random.sample(list(H.nodes()), r)

    H.remove_nodes_from(removed)

    comps = list(nx.connected_components(H))

    largest = max(comps, key=len)

    largest_components.append(len(largest))

    num_components.append(len(comps))

    isolated = sum(
        1 for v in H.nodes()
        if H.degree(v) == 0
    )

    isolated_fractions.append(
        isolated / H.number_of_nodes()
    )

    L = H.subgraph(largest).copy()

    if L.number_of_nodes() > 1:
        avg_distances.append(
            nx.average_shortest_path_length(L)
        )
    else:
        avg_distances.append(0)

plt.figure(figsize=(10,6))

plt.boxplot([
    largest_components,
    num_components,
    avg_distances,
    isolated_fractions
])

plt.xticks(
    [1,2,3,4],
    [
        "Largest\nComponent",
        "Components",
        "Avg\nDistance",
        "Isolated\nFraction"
    ]
)

plt.title("Robustness under Random Removal (5%)")

plt.tight_layout()

plt.savefig("robustness_boxplot.png", dpi=300)

print("Arquivo salvo: robustness_boxplot.png")