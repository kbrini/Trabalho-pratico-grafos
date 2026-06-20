import json
import numpy as np

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json", "r") as f:
    graphs = json.load(f)

densities = []

for edges in graphs.values():

    vertices = set()

    for u, v in edges:
        vertices.add(u)
        vertices.add(v)

    n = len(vertices)
    m = len(edges)

    density = (2*m)/(n*(n-1))
    densities.append(density)

densities = np.array(densities)

print("Densidade média:", np.mean(densities))
print("Densidade mínima:", np.min(densities))
print("Densidade máxima:", np.max(densities))