import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from queue import PriorityQueue

# Terrain data
terrain = np.array([
    [1, 1, 2, 2, 1],
    [1, 2, 2, 3, 2],
    [2, 2, 3, 3, 2],
    [1, 2, 3, 3, 3],
    [1, 1, 2, 2, 2]
])

# Start and end points
start = (4, 0)
end = (0, 4)

def heuristic(a, b):
    """Calculate the heuristic distance between points a and b, including elevation."""
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2) + abs(terrain[x1, y1] - terrain[x2, y2])

def a_star_search(terrain, start, end):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == end:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_pos = (current[0] + dx, current[1] + dy)
            if 0 <= next_pos[0] < terrain.shape[0] and 0 <= next_pos[1] < terrain.shape[1]:
                new_cost = cost_so_far[current] + 1 + abs(terrain[current] - terrain[next_pos])
                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + heuristic(end, next_pos)
                    frontier.put((priority, next_pos))
                    came_from[next_pos] = current

    # Reconstruct the path
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

path = a_star_search(terrain, start, end)

# Create a custom color map
cmap = ListedColormap(['green', 'yellow', 'red'])

# Visualization with custom color mapping for terrain costs
plt.figure(figsize=(8, 8))
plt.imshow(terrain, cmap=cmap)  # Apply the custom colormap

# Plot path
for point in path:
    plt.scatter(point[1], point[0], color='black', s=100, marker='*')  # Path points in black

# Annotate start and end points
plt.scatter(start[1], start[0], color='blue', s=100, label='Start')  # Start point
plt.scatter(end[1], end[0], color='red', s=100, label='End')  # End point

# Add legend and titles
plt.legend()
plt.title('A* Path Planning on Terrain with Cost Visualization')
plt.grid(True)
plt.show()
