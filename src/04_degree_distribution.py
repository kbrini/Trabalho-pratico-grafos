import json
import numpy as np
from collections import Counter

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

degrees = []

for edges in graphs.values():

    deg = {}

    for u,v in edges:
        deg[u] = deg.get(u,0)+1
        deg[v] = deg.get(v,0)+1

    degrees.extend(deg.values())

freq = Counter(degrees)

total = len(degrees)

for k in range(1,11):
    pct = 100*freq[k]/total
    print(f"Grau {k}: {pct:.2f}%")