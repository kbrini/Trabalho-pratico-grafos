import json
import numpy as np

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

ratios = []

for edges in graphs.values():

    vertices = set()

    for u,v in edges:
        vertices.add(u)
        vertices.add(v)

    n = len(vertices)
    m = len(edges)

    ratios.append(m/(n-1))

ratios = np.array(ratios)

print("Média de E/(V-1):", np.mean(ratios))
print("Mediana:", np.median(ratios))
print("Máximo:", np.max(ratios))