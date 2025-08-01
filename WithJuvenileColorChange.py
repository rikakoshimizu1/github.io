import random
import copy
from hexalattice.hexalattice import *
import numpy as np
from matplotlib import pyplot as plt
import os

# Fixed size of array
a = 20
b = 50

# Fixed number of iterations
t = 3

# Create a 2D array (Original)
array = [[0 for i in range(a)] for j in range(b)]

#Loop through entire 2D array
n = len(array)
m = len(array[0])

for i in range(0, n):
    for j in range(0, m):
        # Assign a character of either 2 or 3 (2 for brown, 3 for white)
        # First row is all brown
        if i == 0:
            array[i][j] = 2
            print(array[i][j], end="  ")

        # Create second row
        # Same as fourth row
        if i == 1 or i == 3 or i == 7 or i == 9 or i == 13 or i == 15 or i == 19 or i == 21 or i == 25 or i == 27 or i == 31 or i == 33 or i == 37 or i == 39 or  i == 43 or i == 45:
            if j == 3 or j == 4 or j == 9 or j == 10 or j == 15 or j == 16:
                array[i][j] = 3
                print(array[i][j], end="  ")
            else:
                array[i][j] = 2
                print(array[i][j], end="  ")

        # Create third row
        if i == 2 or i == 8 or i == 14 or i == 20 or i == 26 or i == 32 or i == 38 or i == 44:
            if j == 3 or j == 4 or j == 5 or j == 9 or j == 10 or j == 11 or j == 15 or j == 16 or j == 17:
                array[i][j] = 3
                print(array[i][j], end="  ")
            else:
                array[i][j] = 2
                print(array[i][j], end="  ")

        # Rest fill with brown
        if i == 4 or i == 5 or i == 6 or i == 10 or i == 11 or i == 12 or i == 16 or i == 17 or i == 18 or i == 22 or i == 23 or i == 24 or i == 28 or i == 29 or i == 30 or i == 34 or i == 35 or i == 36 or i == 40 or i == 41 or i == 42 or i == 46 or i == 47 or i == 48:
            array[i][j] = 2
            print(array[i][j], end="  ")
    print()

print("\n")

colors = np.zeros([a * b, 3])
# CMYK color green: (0.00, 1.00, 0.00)
# CMYK color black: (0.85, 0.85, 0.85)

k = 0
for i in range(0, n):
    for j in range(0, m):
        if array[i][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif array[i][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif array[i][(j - 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif array[i][(j - 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif array[(i + 1) % m][(j - 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif array[(i + 1) % m][(j - 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif array[(i - 1) % m][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif array[(i - 1) % m][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif array[(i + 1) % m][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif array[(i + 1) % m][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif array[(i - 1) % m][(j + 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif array[(i - 1) % m][(j + 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif array[i][(j + 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif array[i][(j + 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        else:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        k = k + 1

# For testing purposes
# print(colors)

hex_centers, _ = create_hex_grid(nx=a,
                                 ny=b,
                                 do_plot=True,
                                 align_to_origin=True,
                                 face_color=colors
                                 )

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

plt.show()

# Create Second Stage: With Black Outer Rings

# Duplicate array
newArray = [[0 for i in range(a)] for j in range(b)]
newArray = copy.deepcopy(array)

for i in range(0, n):
    for j in range(0, m):
        # Create a black ring around existing white

        # Top right corner
        #    2
        # 2  3
        if array[i][j] == 3 and array[i][j-1] == 2 and array[i-1][j] == 2:
            newArray[i][j-1] = 0
            newArray[i-1][j] = 0
            newArray[i-1][j+1] = 0
            newArray[i-1][j+2] = 0
        # Bottom right corner
        # 2  3
        #    2
        elif array[i][j] == 3 and array[i][j-1] == 2 and array[i+1][j] == 2:
            newArray[i][j-1] = 0
            newArray[i+1][j] = 0
            newArray[i+1][j+2] = 0
        # Bottom left corner
        # 3  2
        # 2
        elif array[i][j] == 3 and array[i][j+1] == 2 and array[i+1][j] == 2:
            newArray[i+1][j] = 0
            newArray[i][j+1] = 0
        elif array[i][j] == 3 and array[i][j-1] == 2:
            newArray[i][j-1] = 0
        elif array[i][j] == 3 and array[i][j+1] == 2:
            newArray[i][j+1] = 0

for i in range(0, m):
    newArray[49][i] = 2

colors = np.zeros([a * b, 3])
# CMYK color brown: (0.87, 0.65, 0.50)
# CMYK color white: (1.00, 1.00, 1.00)
# CMYK color black: (0.85, 0.85, 0.85)

k = 0
for i in range(0, n):
    for j in range(0, m):
        if newArray[i][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[i][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[i][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[i][(j - 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[i][(j - 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[i][(j - 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][(j - 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][(j - 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i + 1) % m][(j - 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i - 1) % m][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i + 1) % m][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][(j + 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][(j + 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i - 1) % m][(j + 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[i][(j + 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[i][(j + 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[i][(j + 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        else:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        k = k + 1

# For testing purposes
# print(colors)

hex_centers, _ = create_hex_grid(nx=a,
                                 ny=b,
                                 do_plot=True,
                                 align_to_origin=True,
                                 face_color=colors
                                 )

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

plt.show()

# Create random spots
n = len(array)
m = len(array[0])
for i in range(0, n):
    for j in range(0, m):
        if newArray[i][j] == 2:
            newArray[i][j] = random.choice([0, 2])

colors = np.zeros([a * b, 3])
# CMYK color brown: (0.87, 0.65, 0.50)
# CMYK color white: (1.00, 1.00, 1.00)
# CMYK color black: (0.85, 0.85, 0.85)

k = 0
for i in range(0, n):
    for j in range(0, m):
        if newArray[i][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[i][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[i][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[i][(j - 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[i][(j - 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[i][(j - 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][(j - 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][(j - 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i + 1) % m][(j - 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i - 1) % m][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][j] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][j] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i + 1) % m][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][(j + 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][(j + 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[(i - 1) % m][(j + 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[i][(j + 1) % m] == 2:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        elif newArray[i][(j + 1) % m] == 3:
            colors[k, 0] = 1.00
            colors[k, 1] = 1.00
            colors[k, 2] = 1.00
        elif newArray[i][(j + 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        else:
            colors[k, 0] = 0.87
            colors[k, 1] = 0.65
            colors[k, 2] = 0.50
        k = k + 1

# For testing purposes
# print(colors)

hex_centers, _ = create_hex_grid(nx=a,
                                 ny=b,
                                 do_plot=True,
                                 align_to_origin=True,
                                 face_color=colors
                                 )

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

plt.show()

# Change colors from brown/white to green

colors = np.zeros([a * b, 3])
# CMYK color brown: (0.87, 0.65, 0.50)
# CMYK color white: (1.00, 1.00, 1.00)
# CMYK color black: (0.85, 0.85, 0.85)

k = 0
for i in range(0, n):
    for j in range(0, m):
        if newArray[i][j] == 2:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[i][j] == 3:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[i][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[i][(j - 1) % m] == 2:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[i][(j - 1) % m] == 3:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[i][(j - 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][(j - 1) % m] == 2:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i + 1) % m][(j - 1) % m] == 3:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i + 1) % m][(j - 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][j] == 2:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i - 1) % m][j] == 3:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i - 1) % m][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i + 1) % m][j] == 2:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i + 1) % m][j] == 3:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i + 1) % m][j] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[(i - 1) % m][(j + 1) % m] == 2:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i - 1) % m][(j + 1) % m] == 3:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[(i - 1) % m][(j + 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        elif newArray[i][(j + 1) % m] == 2:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[i][(j + 1) % m] == 3:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        elif newArray[i][(j + 1) % m] == 0:
            colors[k, 0] = 0.50
            colors[k, 1] = 0.50
            colors[k, 2] = 0.50
        else:
            colors[k, 0] = 0.00
            colors[k, 1] = 1.00
            colors[k, 2] = 0.00
        k = k + 1

# For testing purposes
# print(colors)

hex_centers, _ = create_hex_grid(nx=a,
                                 ny=b,
                                 do_plot=True,
                                 align_to_origin=True,
                                 face_color=colors
                                 )

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

plt.show()

for i in range(0, n):
    for j in range(0, m):
        if newArray[i][j] == 2 or newArray[i][j] == 3:
            newArray[i][j] = 1





