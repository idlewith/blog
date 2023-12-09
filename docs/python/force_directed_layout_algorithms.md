# Force-directed layout algorithms


3 algorithms below

- Fruchterman-Reingold: classic

- Kamada-Kawai

- Force Atlas


first algorithms example code below:

```python

import numpy as np
import matplotlib.pyplot as plt


def optimize_layout(
    adjacency_matrix,
    iterations=50,
    k=0.1,
    width=1.0,
    height=1.0,
    t=0.1,
):
    """
    Functions for optimizing layout using Fruchterman-Reingold.

     parameter:
     - adjacency_matrix: adjacency matrix, which represents the connection relationship of the graph.
     - iterations: Number of optimization iterations.
     - repulsion_factor: Repulsion factor, which affects the repulsion between nodes.
     - width: canvas width.
     - height: canvas height.
     - temperature: temperature parameter that controls node movement.

     return value:
     Optimized node layout.
    """

    num_nodes = len(adjacency_matrix)
    positions = np.random.rand(num_nodes, 2)

    for _ in range(iterations):
        # Calculate repulsion
        repulsion = np.zeros((num_nodes, 2))
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    delta = positions[i] - positions[j]
                    distance = max(np.linalg.norm(delta), 0.01)
                    repulsion[i] += k * k / distance * delta / distance

        # Calculate attraction
        attraction = np.zeros((num_nodes, 2))
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j and adjacency_matrix[i][j]:
                    delta = positions[i] - positions[j]
                    distance = max(np.linalg.norm(delta), 0.01)
                    attraction[i] -= distance * distance / k * delta / distance
                    attraction[j] += distance * distance / k * delta / distance

        # Update node location
        displacement = repulsion + attraction
        positions += t * displacement

        # Limit the position of the node to the range [0, width] x [0, height]
        positions[:, 0] = np.clip(positions[:, 0], 0, width)
        positions[:, 1] = np.clip(positions[:, 1], 0, height)

    return positions


# example usage
call_relations = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

# Build node number dictionary
node_to_index = {node: i for i, node in enumerate(call_relations.keys())}

# Build adjacency matrix
num_nodes = len(call_relations)
adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
for caller, callees in call_relations.items():
    for callee in callees:
        adjacency_matrix[node_to_index[caller], node_to_index[callee]] = 1

positions = optimize_layout(
    adjacency_matrix,
    iterations=200,
    k=0.3,
    width=1.0,
    height=1.0,
    t=0.1,
)

# Draw nodes
plt.scatter(
    positions[:, 0],
    positions[:, 1],
    s=300,
    color="skyblue",
    edgecolors="black",
    linewidths=1.5,
    zorder=2,
)

# Draw edges
for i in range(adjacency_matrix.shape[0]):
    for j in range(adjacency_matrix.shape[1]):
        if adjacency_matrix[i, j]:
            plt.arrow(
                positions[i, 0],
                positions[i, 1],
                (positions[j, 0] - positions[i, 0]) * 0.9,
                (positions[j, 1] - positions[i, 1]) * 0.9,
                shape="full",
                lw=0,
                length_includes_head=True,
                head_width=0.02,
                color="black",
                zorder=1,
            )

# Mark nodes
for i, (node, index) in enumerate(node_to_index.items()):
    plt.text(
        positions[index, 0],
        positions[index, 1],
        node,
        ha="center",
        va="center",
        color="black",
        fontsize=10,
        fontweight="bold",
    )

# Remove coordinate axis
plt.axis("off")

plt.show()

```