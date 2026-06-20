import json
import networkx as nx
import numpy as np
import random

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

print("=== FALHA ALEATORIA ===")

print("Maior componente")
print("Media:", np.mean(largest_components))
print("Desvio:", np.std(largest_components))

print()

print("Numero de componentes")
print("Media:", np.mean(num_components))
print("Desvio:", np.std(num_components))

print()

print("Distancia media")
print("Media:", np.mean(avg_distances))
print("Desvio:", np.std(avg_distances))

print()

print("Fracao isolados")
print("Media:", np.mean(isolated_fractions))
print("Desvio:", np.std(isolated_fractions))

# Ataque direcionado

H = G.copy()

bet = nx.betweenness_centrality(H)

ranking = sorted(
    bet,
    key=bet.get,
    reverse=True
)

H.remove_nodes_from(ranking[:r])

comps = list(nx.connected_components(H))

largest = max(comps,key=len)

isolated = sum(
    1 for v in H.nodes()
    if H.degree(v)==0
)

L = H.subgraph(largest)

print("\n=== ATAQUE DIRECIONADO ===")

print("Maior componente:", len(largest))
print("Numero componentes:", len(comps))

if L.number_of_nodes()>1:
    print(
        "Distancia media:",
        nx.average_shortest_path_length(L)
    )

print(
    "Fracao isolados:",
    isolated/H.number_of_nodes()
)