import json
import networkx as nx
import numpy as np

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

n = G.number_of_nodes()
m = G.number_of_edges()

p = (2*m)/(n*(n-1))

ER = nx.erdos_renyi_graph(n,p,seed=42)

while not nx.is_connected(ER):
    ER = nx.erdos_renyi_graph(n,p)

L_real = nx.average_shortest_path_length(G)
C_real = nx.average_clustering(G)

L_rand = nx.average_shortest_path_length(ER)
C_rand = nx.average_clustering(ER)

print("Grafo Real")
print("L =",L_real)
print("C =",C_real)

print()

print("Erdos-Renyi")
print("L =",L_rand)
print("C =",C_rand)

print()

print("C/Crand =",C_real/C_rand if C_rand>0 else "inf")
print("L/Lrand =",L_real/L_rand)