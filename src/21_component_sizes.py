import json
import networkx as nx

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

sizes = sorted(
    [len(c) for c in nx.connected_components(G)],
    reverse=True
)

print("Tamanhos:", sizes)