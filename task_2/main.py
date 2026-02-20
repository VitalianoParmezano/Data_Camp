import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Initialize the 20x20 grid
size = 20
grid = np.random.choice([0, 1], size=(size, size))

def get_next_step(current_grid):
    new_grid = current_grid.copy()
    for i in range(size):
        for j in range(size):
            # Calculate neighbors using a 3x3 slice
            neighbors_sum = np.sum(current_grid[max(0, i-1):min(size, i+2), 
                                               max(0, j-1):min(size, j+2)]) - current_grid[i, j]
            
            if current_grid[i, j] == 1:
                # Life continues with 2 or 3 neighbors
                if neighbors_sum < 2 or neighbors_sum > 3:
                    new_grid[i, j] = 0
            else:
                # Rule: New life starts with exactly 3 neighbors
                if neighbors_sum == 3:
                    new_grid[i, j] = 1
    return new_grid

def on_key(event):
    # Update the grid and visualization when 'n' is pressed
    global grid
    if event.key == 'n':
        grid = get_next_step(grid)
        img.set_data(grid)
        plt.title('Game of Life - Press "n" for next step')
        fig.canvas.draw()

# Setup the visualization
fig, ax = plt.subplots(figsize=(6, 6))
custom_cmap = ListedColormap(['lightgrey', 'green'])
img = ax.imshow(grid, cmap=custom_cmap)

ax.set_axis_off()
plt.title('Game of Life - Press "n" for next step')

# Connect the event handler
fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()