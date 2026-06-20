import json
import numpy as np
import matplotlib.pyplot as plt
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

x = np.array(sorted(freq.keys()))
y = np.array([freq[k] for k in x])

plt.figure(figsize=(8,6))
plt.loglog(x,y,'o')
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Degree Distribution (Log-Log)")
plt.grid(True)
plt.savefig("power_law.png")
plt.show()