import numpy as np
import matplotlib.pyplot as plt

# Configuration
num_points = 20
heights = np.random.randint(0, 101, size=num_points)

print("Generated Heights:", heights)

# Find the highest peaks to the left and right
max_left = np.maximum.accumulate(heights)
max_right = np.maximum.accumulate(heights[::-1])[::-1]

# Water surface level is determined by the lower of the two surrounding peaks
water_level = np.minimum(max_left, max_right)
depths = water_level - heights

# Identify the deepest point
deepest_idx = np.argmax(depths)
max_depth = depths[deepest_idx]

# Find the boundaries of this specific deepest lake
# Expand left until depth is 0
left_border = deepest_idx
while left_border > 0 and depths[left_border] > 0:
    left_border -= 1

# Expand right until depth is 0
right_border = deepest_idx
while right_border < num_points - 1 and depths[right_border] > 0:
    right_border += 1

# Visualization
plt.figure(figsize=(10, 5))

# Plot the entire landscape as a background
plt.plot(heights, linestyle='-', color='blue', alpha=0.3, label='Landscape')

# Slice the data to plot ONLY the deepest lake curves
lake_indices = range(left_border, right_border + 1)
lake_values = heights[left_border : right_border + 1]
# Highlight the deepest lake in red
plt.plot(lake_indices, lake_values, linestyle='-', color='red', linewidth=3, label='Deepest Lake')

# Paint lines to show the water level and depth
plt.axhline(y= heights[deepest_idx] + max_depth, color='cyan', linestyle='--', label='Water Level')
plt.axhline(y= heights[deepest_idx], color='orange', linestyle='--', label='Lake Surface')

# Formatting the plot
plt.title(f'Deepest Lake (Max Depth: {max_depth})')
plt.xlabel('Index')
plt.ylabel('Height / Depth')
plt.grid(True, alpha=0.2)

plt.show()