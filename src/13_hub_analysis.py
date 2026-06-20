import json
import networkx as nx

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

ranking = sorted(
    G.degree(),
    key=lambda x: x[1],
    reverse=True
)

print("Top 10 vertices por grau")

for v,d in ranking[:10]:
    print(v,d)