import json

with open(r"C:\Users\Administrador\Downloads\reddit_threads\reddit_edges.json", "r") as f:
    graphs = json.load(f)

vertex_counts = []
edge_counts = []

for edges in graphs.values():

    vertices = set()

    for u, v in edges:
        vertices.add(u)
        vertices.add(v)

    vertex_counts.append(len(vertices))
    edge_counts.append(len(edges))

n_graphs = len(graphs)

avg_vertices = sum(vertex_counts) / n_graphs
avg_edges = sum(edge_counts) / n_graphs

print("Número de grafos:", n_graphs)

print("\nVÉRTICES")
print("Média:", round(avg_vertices, 4))
print("Mínimo:", min(vertex_counts))
print("Máximo:", max(vertex_counts))

print("\nARESTAS")
print("Média:", round(avg_edges, 4))
print("Mínimo:", min(edge_counts))
print("Máximo:", max(edge_counts))