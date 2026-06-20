import json
import networkx as nx
import time

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

origem = 0

inicio = time.perf_counter()
bfs = list(nx.bfs_tree(G,origem))
tempo_bfs = time.perf_counter()-inicio

inicio = time.perf_counter()
dfs = list(nx.dfs_tree(G,origem))
tempo_dfs = time.perf_counter()-inicio

print("BFS")
print("Visitados:",len(bfs))
print("Tempo:",tempo_bfs)

print()

print("DFS")
print("Visitados:",len(dfs))
print("Tempo:",tempo_dfs)