def water_jug_dfs(capacity1, capacity2, target):
    visited = set()
    path = []

    def dfs(jug1, jug2):
        if (jug1, jug2) in visited:
            return False
        
        visited.add((jug1, jug2))
        path.append((jug1, jug2))

        # Check if the target is achieved
        if jug1 == target or jug2 == target:
            return True

        # Fill jug 1
        if dfs(capacity1, jug2):
            return True

        # Fill jug 2
        if dfs(jug1, capacity2):
            return True

        # Empty jug 1
        if dfs(0, jug2):
            return True

        # Empty jug 2
        if dfs(jug1, 0):
            return True

        # Pour jug 1 into jug 2
        if dfs(max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug1 + jug2)):
            return True

        # Pour jug 2 into jug 1
        if dfs(min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1))):
            return True

        path.pop()
        return False

    if dfs(0, 0):
        return path
        
    return []

# Example Usage
capacity1 = 3
capacity2 = 5
target = 4

solution = water_jug_dfs(capacity1, capacity2, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

import matplotlib.pyplot as plt
import networkx as nx

# Visualize the DFS solution path
def visualize_dfs_solution(solution):
    G = nx.DiGraph()

    for i in range(len(solution) - 1):
        G.add_edge(solution[i], solution[i + 1])

    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 6))

    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()), edge_color='blue', width=2)

    plt.title("Water Jug Problem - DFS Solution Path")
    plt.show()

if solution:
    visualize_dfs_solution(solution)



