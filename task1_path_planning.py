import numpy as np
import matplotlib.pyplot as plt
from queue import Queue

# Making a 5x5 grid 
grid = np.zeros((5, 5), dtype=int)
obstacles = [(1, 2), (2, 3), (3, 1), (3, 4)]
for obstacle in obstacles:
    grid[obstacle] = 2  # Mark obstacles as 2

# start and end points
start = (4, 0)
end = (0, 4)

#BFS(Breadth-First Search Algorithm) for finding the shortest path.#
def bfs(grid, start, end):
    queue = Queue()
    queue.put([start]) 
    visited = set([start])

    while not queue.empty():
        path = queue.get()
        x, y = path[-1]

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Directions to move
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] != 2 and (nx, ny) not in visited:
                queue.put(path + [(nx, ny)])
                visited.add((nx, ny))

    return None

# Finding the path
path = bfs(grid, start, end)

# Visualization with better color differentiation
grid_visual = grid.copy()
for x, y in path:
    grid_visual[x, y] = 1  # Mark the path with 1


plt.imshow(grid_visual, cmap='Greens', interpolation='nearest')

# Mark the start and end points
plt.scatter(*start[::-1], color='blue', label='Start', s=100)  
plt.scatter(*end[::-1], color='red', label='End', s=100)  

plt.legend()
plt.grid(True)
plt.show()