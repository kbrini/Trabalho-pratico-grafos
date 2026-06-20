import json
import networkx as nx
import matplotlib.pyplot as plt

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

plt.figure(figsize=(12,12))

nx.draw_networkx(
    G,
    node_size=50,
    with_labels=False
)

plt.savefig("largest_graph.png",dpi=300)
plt.show()