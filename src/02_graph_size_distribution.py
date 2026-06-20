import json
import numpy as np

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json","r") as f:
    graphs = json.load(f)

sizes = []

for edges in graphs.values():

    vertices = set()

    for u,v in edges:
        vertices.add(u)
        vertices.add(v)

    sizes.append(len(vertices))

sizes = np.array(sizes)

print("Q1:", np.percentile(sizes,25))
print("Mediana:", np.percentile(sizes,50))
print("Q3:", np.percentile(sizes,75))
print("Percentil 90:", np.percentile(sizes,90))
print("Percentil 95:", np.percentile(sizes,95))
print("Percentil 99:", np.percentile(sizes,99))