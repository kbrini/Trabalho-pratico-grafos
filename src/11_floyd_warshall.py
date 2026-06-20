import json
import networkx as nx
import time
import numpy as np

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

inicio = time.perf_counter()

dist = dict(nx.floyd_warshall(G))

tempo = time.perf_counter()-inicio

valores = []

for u in dist:
    for v in dist[u]:
        if u != v:
            valores.append(dist[u][v])

print("Tempo:",tempo)
print("Menor distancia:",min(valores))
print("Maior distancia:",max(valores))
print("Media:",np.mean(valores))