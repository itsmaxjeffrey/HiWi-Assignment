import numpy as np
import matplotlib.pyplot as plt
from queue import Queue

# Making a 5x5 grid 
grid = np.zeros((5, 5), dtype=int)
obstacles = [(1, 2), (2, 3), (3, 1), (3, 4)]
for obstacle in obstacles:
    grid[obstacle] = 2  # Mark obstacles as 2

# Defining start, end and waypoints
start = (4, 0)
end = (0, 4)
waypoints = [(2, 2), (1, 4)]
all_points = [start] + waypoints + [end]

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

def bfs_with_waypoints(grid, all_points):
    """Pathfinding that includes waypoints."""
    final_path = []
    for i in range(len(all_points) - 1):
        part_path = bfs(grid, all_points[i], all_points[i + 1])
        final_path.extend(part_path[:-1])  # Exclude last point to avoid duplication
    final_path.append(all_points[-1])  # Add the final destination
    return final_path

path = bfs_with_waypoints(grid, all_points)

# Visualization
grid_visual = grid.copy()
for x, y in path:
    grid_visual[x, y] = 1  # Mark the path

plt.imshow(grid_visual, cmap='Greens', interpolation='nearest')

# Annotate start, end points, and waypoints
plt.scatter(*start[::-1], color='blue', label='Start', s=100)  # Start point
plt.scatter(*end[::-1], color='red', label='End', s=100)  # End point
for waypoint in waypoints:
    plt.scatter(*waypoint[::-1], color='yellow', label='Waypoint', s=100)  # Waypoints

#show the plot
plt.legend()
plt.grid(True)
plt.show()