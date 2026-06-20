import json
import networkx as nx
import time

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()

for u,v in graphs["481"]:
    G.add_edge(u,v,weight=1)

inicio = time.perf_counter()
mst_prim = nx.minimum_spanning_tree(G,algorithm="prim")
tempo_prim = time.perf_counter()-inicio

inicio = time.perf_counter()
mst_kruskal = nx.minimum_spanning_tree(G,algorithm="kruskal")
tempo_kruskal = time.perf_counter()-inicio

peso_prim = sum(d["weight"] for _,_,d in mst_prim.edges(data=True))
peso_kruskal = sum(d["weight"] for _,_,d in mst_kruskal.edges(data=True))

print("Prim")
print("Arestas:",mst_prim.number_of_edges())
print("Peso:",peso_prim)
print("Tempo:",tempo_prim)

print()

print("Kruskal")
print("Arestas:",mst_kruskal.number_of_edges())
print("Peso:",peso_kruskal)
print("Tempo:",tempo_kruskal)