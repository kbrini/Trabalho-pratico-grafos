import json
import networkx as nx

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

odd = [v for v,d in G.degree() if d % 2 == 1]

print("Vertices de grau impar:", len(odd))

if len(odd) == 0:
    print("Euleriano")
elif len(odd) == 2:
    print("Semi-Euleriano")
else:
    print("Nao Euleriano")