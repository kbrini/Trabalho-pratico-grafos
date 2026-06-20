import json
import networkx as nx
import numpy as np

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

edges = graphs["481"]

G = nx.Graph()
G.add_edges_from(edges)

print("Vertices:", G.number_of_nodes())
print("Arestas:", G.number_of_edges())

print("Componentes:", nx.number_connected_components(G))

largest_cc = max(nx.connected_components(G), key=len)

H = G.subgraph(largest_cc).copy()

print("Maior componente:", H.number_of_nodes())

print("Diametro:", nx.diameter(H))
print("Raio:", nx.radius(H))

print("Distancia media:",
      nx.average_shortest_path_length(H))

print("Clusterizacao media:",
      nx.average_clustering(H))

degrees = dict(H.degree())

max_node = max(degrees, key=degrees.get)

print("Maior grau:", degrees[max_node])
print("Vertice:", max_node)