import json
import networkx as nx
import time
import numpy as np
from scipy.stats import t

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

G = nx.Graph()
G.add_edges_from(graphs["481"])

REPETICOES = 30

algoritmos = {
    "BFS": lambda: list(nx.bfs_tree(G,0)),
    "DFS": lambda: list(nx.dfs_tree(G,0)),
    "PRIM": lambda: nx.minimum_spanning_tree(G,algorithm="prim"),
    "KRUSKAL": lambda: nx.minimum_spanning_tree(G,algorithm="kruskal"),
    "FLOYD": lambda: nx.floyd_warshall(G)
}

for nome, func in algoritmos.items():

    tempos = []

    for _ in range(REPETICOES):

        inicio = time.perf_counter()

        func()

        fim = time.perf_counter()

        tempos.append(fim-inicio)

    media = np.mean(tempos)
    desvio = np.std(tempos,ddof=1)

    margem = t.ppf(0.975,REPETICOES-1) * desvio / np.sqrt(REPETICOES)

    print()
    print(nome)
    print("Media:",media)
    print("Desvio:",desvio)
    print("IC95%:",(media-margem,media+margem))