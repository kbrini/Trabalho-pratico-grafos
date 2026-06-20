import json
import networkx as nx

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

edges = graphs["481"]

G = nx.Graph()
G.add_edges_from(edges)

articulations = list(nx.articulation_points(G))
bridges = list(nx.bridges(G))

print("Pontos de articulacao:", len(articulations))
print("Pontes:", len(bridges))

print("\nPrimeiros pontos de articulacao:")
print(articulations[:20])

print("\nPrimeiras pontes:")
print(bridges[:20])