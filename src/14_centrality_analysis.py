import json
import networkx as nx

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

bet = nx.betweenness_centrality(G)

top = sorted(
    bet.items(),
    key=lambda x:x[1],
    reverse=True
)

print("Top 10 betweenness")

for v,val in top[:10]:
    print(v,round(val,4))