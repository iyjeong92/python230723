# GridTest.py

# Define the dimensions of the grid
rows = 145
cols = 145

# Define the longitude and latitude ranges
min_longitude = 125
max_longitude = 132
min_latitude = 20
max_latitude = 50

# Calculate the intervals for longitude and latitude
longitude_interval = (max_longitude - min_longitude) / (cols - 1)
latitude_interval = (max_latitude - min_latitude) / (rows - 1)

# Create an empty grid (2D list) filled with zeros
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Fill the grid with longitude and latitude values
for i in range(rows):
    for j in range(cols):
        longitude = min_longitude + j * longitude_interval
        latitude = min_latitude + i * latitude_interval
        grid[i][j] = (longitude, latitude)

# Printing the grid (Optional)
for row in grid:
    print(' '.join(f"({cell[0]:.2f}, {cell[1]:.2f})" for cell in row))