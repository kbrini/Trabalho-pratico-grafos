import json
import networkx as nx

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

triangles = sum(nx.triangles(G).values()) // 3

print("Triangulos:", triangles)

graus = [d for _, d in G.degree()]

print("Grau minimo:", min(graus))