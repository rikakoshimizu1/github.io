import random
import copy
from hexalattice.hexalattice import *
import numpy as np
from matplotlib import pyplot as plt
import os

# Fixed size of array
a = 3
b = 3

# Fixed number of iterations
t = 3

counter = 1

numGreen = 0

numberGreen = []
numberBlack = []

# Iterations n times
def iterate(array, startingAge, maxAge):
    global countGreenArray, n, m, newArray, countGreenAroundBlack, countBlackAroundGreen, counter, \
        numberBlack, numberGreen, numGreen, numBlack, countBlackNeighbors, countGreenNeighbors
    if startingAge == maxAge:
        return

    # Adult
    if startingAge <= 15:
        for i in range(0, n):
            for j in range(0, m):
                # Reset Green Count
                countGreen = 0
                # Count Number of Greens (1)
                # all the same for middle, left, and right
                countGreen = array[i][j] + array[i][(j-1) % m] + array[i][(j+1) % m]
                # If is the upper or lower edge
                if i == 0 | i == m:
                    countGreen = countGreen + array[(i-1) % m][(j-1) % m] \
                                     + array[(i-1) % m][j] + array[(i + 1) % m][(j - 1) % m] + array[(i+1) % m][j]
                # If is middle or left/right edge odd row
                if i % 2 == 1:
                    countGreen = countGreen + array[(i-1) % m][j] + array[(i-1) % m][(j+1) % m] \
                                     + array[(i+1) % m][j] + array[(i+1) % m][(j + 1) % m]
                # If is middle or left/right edge even row
                elif i % 2 == 0:
                    countGreen = countGreen + array[(i-1) % m][(j-1) % m] + array[(i-1) % m][j] \
                                     + array[(i + 1) % m][(j-1) % m] + array[(i + 1) % m][j]
                if countGreen == 0 or countGreen == 1 or countGreen == 2:
                    # If center hex is black
                    if array[i][j] == 0:
                        # Change the new array to green
                        newArray[i][j] = 1
                        # Increment count
                        countGreen = countGreen + 1
                        # 7-countGreen because there are 7 neighbors
                        # Counting just the neighbors not the center
                        countGreenNeighbors.append(countGreen - 1)
                    else:
                        # If center hex is already green
                        # Leave green
                        newArray[i][j] = 1
                        countGreenNeighbors.append(countGreen - 1)
                    countBlackAroundGreen.append(7 - countGreen)
                elif countGreen == 3:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                        # Leave at black
                        newArray[i][j] = 0
                        # 7 - (countGreen + 1) because not counting the center
                        countBlackNeighbors.append(7 - (countGreen + 1))
                    else:
                        countBlackAroundGreen.append(7 - countGreen)
                        # Leave at green
                        newArray[i][j] = 1
                        countGreenNeighbors.append(countGreen - 1)
                # 4+ count greens
                else:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                        # Leave at black
                        newArray[i][j] = 0
                        countBlackNeighbors.append(7 - (countGreen + 1))
                    else:
                        # Change to black
                        newArray[i][j] = 0
                        countGreen = countGreen - 1
                        countGreenAroundBlack.append(countGreen)
                        countBlackNeighbors.append(7 - (countGreen + 1))
                print(newArray[i][j], end="  ")
            print()
        print("\n")

        for i in range(0, n):
            for j in range(0, m):
                countGreenUpdated = 0
                # If the number of rows is odd number
                if n % 2 == 1:
                    # countGreenUpdated
                    countGreenUpdated = newArray[i][j] + newArray[i][(j-1) % m] + array[i][(j+1) % m]
                    # If is middle or left/right edge odd row
                    if i % 2 == 1:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][j] + newArray[(i - 1) % m][(j + 1) % m] \
                                     + newArray[(i + 1) % m][j] + newArray[(i + 1) % m][(j + 1) % m]
                    # If is middle or left/right edge even row
                    elif i % 2 == 0:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][(j - 1) % m] + newArray[(i - 1) % m][j] \
                                     + newArray[(i + 1) % m][(j - 1) % m] + newArray[(i + 1) % m][j]
                # If the number of rows is even number
                if n % 2 == 0:
                    # countGreenUpdated
                    countGreenUpdated = newArray[i][j] + newArray[i][(j - 1) % m] + newArray[i][(j + 1) % m]
                    # If is middle or left/right edge even row
                    if i % 2 == 1:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][j] + newArray[(i - 1) % m][
                            (j + 1) % m] \
                                            + newArray[(i + 1) % m][j] + newArray[(i + 1) % m][(j + 1) % m]
                    # If is middle or left/right edge even row
                    elif i % 2 == 0:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][(j - 1) % m] + \
                                            newArray[(i - 1) % m][j] \
                                            + newArray[(i + 1) % m][(j - 1) % m] + newArray[(i + 1) % m][j]
                countGreenArray[i][j] = countGreenUpdated

    # Adult
    else:
        for i in range(0, n):
            for j in range(0, m):
                # Reset Green Count
                countGreen = 0
                # Count Number of Greens (1)
                # all the same for middle, left, and right
                countGreen = array[i][j] + array[i][(j - 1) % m] + array[i][(j + 1) % m]
                # If is the upper or lower edge
                if i == 0 | i == m:
                    countGreen = countGreen + array[(i - 1) % m][(j - 1) % m] \
                                 + array[(i - 1) % m][j] + array[(i + 1) % m][(j - 1) % m] + array[(i + 1) % m][j]
                # If is middle or left/right edge odd row
                if i % 2 == 1:
                    countGreen = countGreen + array[(i - 1) % m][j] + array[(i - 1) % m][(j + 1) % m] \
                                 + array[(i + 1) % m][j] + array[(i + 1) % m][(j + 1) % m]
                # If is middle or left/right edge even row
                elif i % 2 == 0:
                    countGreen = countGreen + array[(i - 1) % m][(j - 1) % m] + array[(i - 1) % m][j] \
                                 + array[(i + 1) % m][(j - 1) % m] + array[(i + 1) % m][j]
                if countGreen == 0 or countGreen == 1 or countGreen == 2:
                    # If center hex is black
                    if array[i][j] == 0:
                        # Change the new array to green
                        newArray[i][j] = 1
                        # Increment count
                        countGreen = countGreen + 1
                        # 7-countGreen because there are 7 neighbors
                    else:
                        # If center hex is already green
                        # Leave green
                        newArray[i][j] = 1
                    countBlackAroundGreen.append(7 - countGreen)
                    countGreenArray[i][j] = countGreen
                elif countGreen == 3:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                        newArray[i][j] = 0
                    else:
                        countBlackAroundGreen.append(7 - countGreen)
                        newArray[i][j] = 1
                # 4+ count greens
                else:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                        newArray[i][j] = 0
                    else:
                        newArray[i][j] = 0
                        countGreen = countGreen - 1
                        countGreenAroundBlack.append(countGreen)
                    countGreenArray[i][j] = countGreen
            print(newArray[i][j], end="  ")
            print()
            print("\n")

        for i in range(0, n):
            for j in range(0, m):
                countGreenUpdated = 0
                # If the number of rows is odd number
                if n % 2 == 1:
                    # countGreenUpdated
                    countGreenUpdated = newArray[i][j] + newArray[i][(j - 1) % m] + newArray[i][(j + 1) % m]
                    # If is middle or left/right edge odd row
                    if i % 2 == 1:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][j] + newArray[(i - 1) % m][(j + 1) % m] \
                                            + newArray[(i + 1) % m][j] + newArray[(i + 1) % m][(j + 1) % m]
                    # If is middle or left/right edge even row
                    elif i % 2 == 0:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][(j - 1) % m] + newArray[(i - 1) % m][j] \
                                            + newArray[(i + 1) % m][(j - 1) % m] + newArray[(i + 1) % m][j]
                # If the number of rows is even number
                if n % 2 == 0:
                    # countGreenUpdated
                    countGreenUpdated = newArray[i][j] + newArray[i][(j - 1) % m] + newArray[i][(j + 1) % m]
                    # If is middle or left/right edge even row
                    if i % 2 == 1:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][j] + newArray[(i - 1) % m][
                            (j + 1) % m] \
                                            + newArray[(i + 1) % m][j] + newArray[(i + 1) % m][(j + 1) % m]
                    # If is middle or left/right edge even row
                    elif i % 2 == 0:
                        countGreenUpdated = countGreenUpdated + newArray[(i - 1) % m][(j - 1) % m] + \
                                            newArray[(i - 1) % m][j] \
                                            + newArray[(i + 1) % m][(j - 1) % m] + newArray[(i + 1) % m][j]
                countGreenArray[i][j] = countGreenUpdated

    print(countGreenAroundBlack)
    print(countBlackAroundGreen)

    numBlack = 0
    numGreen = 0
    # Count the number of green and black in array
    for i in range(0, n):
        for j in range(0, m):
            if newArray[i][j] == 1:
                numGreen = numGreen + 1
            else:
                numBlack = numBlack + 1

    numberBlack.append(numBlack)
    numberGreen.append(numGreen)

    # Time points vs. Number of Scales Graph
    x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    colors = np.zeros([a*b, 3])
    # CMYK color green: (0.00, 1.00, 0.00)
    # CMYK color black: (0.85, 0.85, 0.85)

    k = 0
    for i in range(0, n):
        for j in range(0, m):
            if newArray[i][j] == 1:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            elif newArray[i][j] == 0:
                colors[k, 0] = 0.85
                colors[k, 1] = 0.85
                colors[k, 2] = 0.85
            elif newArray[i][(j - 1) % m] == 1:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            elif newArray[i][(j - 1) % m] == 0:
                colors[k, 0] = 0.85
                colors[k, 1] = 0.85
                colors[k, 2] = 0.85
            elif newArray[(i + 1) % m][(j - 1) % m] == 1:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            elif newArray[(i + 1) % m][(j - 1) % m] == 0:
                colors[k, 0] = 0.85
                colors[k, 1] = 0.85
                colors[k, 2] = 0.85
            elif newArray[(i - 1) % m][j] == 1:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            elif newArray[(i - 1) % m][j] == 0:
                colors[k, 0] = 0.85
                colors[k, 1] = 0.85
                colors[k, 2] = 0.85
            elif newArray[(i + 1) % m][j] == 1:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            elif newArray[(i + 1) % m][j] == 0:
                colors[k, 0] = 0.85
                colors[k, 1] = 0.85
                colors[k, 2] = 0.85
            elif newArray[(i - 1) % m][(j + 1) % m] == 1:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            elif newArray[(i - 1) % m][(j + 1) % m] == 0:
                colors[k, 0] = 0.85
                colors[k, 1] = 0.85
                colors[k, 2] = 0.85
            elif newArray[i][(j + 1) % m] == 1:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            elif newArray[i][(j + 1) % m] == 0:
                colors[k, 0] = 0.85
                colors[k, 1] = 0.85
                colors[k, 2] = 0.85
            else:
                colors[k, 0] = 0.00
                colors[k, 1] = 1.00
                colors[k, 2] = 0.00
            k = k+1

    # For testing purposes
    #print(colors)

    hex_centers, _ = create_hex_grid(nx=a,
                                     ny=b,
                                     do_plot=True,
                                     align_to_origin=True,
                                     face_color=colors
                                     )

    x_hex_coords = hex_centers[:, 0]
    y_hex_coords = hex_centers[:, 1]

    k = 0
    for i in range(0, n):
        for j in range(0, m):
            plt.text(hex_centers[k, 0], hex_centers[k, 1], countGreenArray[i][j], fontsize=12)
            k = k+1

    # For testing purposes
    # print(x_hex_coords[0])
    #plt.show()

    # MANUALLY CHANGE
    path = 'C:/Users/shimizr/Desktop/MA497/SimulationGraphics/Testing'
    if not os.path.exists(path):
        os.makedirs(path)

    # while os.path.exists(path):
    #     i = i + 1
    plt.savefig(path + '/sim' + str(counter) + '.png')
    counter = counter+1

    plt.show()

    # Create a graph for the number of neighbors vs. frequency
    # Observed Data
    #ogy = [0, 0.04, 0.23, 0.45, 0.25, 0.06, 0, 0]
    #oby = [0, 0, 0.03, 0.23, 0.48, 0.275, 0.04, 0]

    # Count the number of 1-7 number of neighbors occur to calculate the frequency
    #gy0, gy1, gy2, gy3, gy4, gy5, gy6, gy7 = 0, 0, 0, 0, 0, 0, 0, 0
    #x = [0, 1, 2, 3, 4, 5, 6, 7]

    #by0, by1, by2, by3, by4, by5, by6, by7 = 0, 0, 0, 0, 0, 0, 0, 0
    #x = [0, 1, 2, 3, 4, 5, 6, 7]

    # Testing purposes
    #print(countBlackAroundGreen)
    #print(countGreenAroundBlack)

    # for i in countGreenAroundBlack:
    #     if i == 0:
    #         gy0 = gy0 + 1
    #     elif i == 1:
    #         gy1 = gy1 + 1
    #     elif i == 2:
    #         gy2 = gy2 + 1
    #     elif i == 3:
    #         gy3 = gy3 + 1
    #     elif i == 4:
    #         gy4 = gy4 + 1
    #     elif i == 5:
    #         gy5 = gy5 + 1
    #     elif i == 6:
    #         gy6 = gy6 + 1
    #     elif i == 7:
    #         gy7 = gy7 + 1

    # for i in countGreenAroundBlackOriginal:
    #     if i == 0:
    #         gy0 = gy0 + 1
    #     elif i == 1:
    #         gy1 = gy1 + 1
    #     elif i == 2:
    #         gy2 = gy2 + 1
    #     elif i == 3:
    #         gy3 = gy3 + 1
    #     elif i == 4:
    #         gy4 = gy4 + 1
    #     elif i == 5:
    #         gy5 = gy5 + 1
    #     elif i == 6:
    #         gy6 = gy6 + 1
    #     elif i == 7:
    #         gy7 = gy7 + 1

    # for i in countBlackAroundGreen:
    #     if i == 0:
    #         by0 = by0 + 1
    #     elif i == 1:
    #         by1 = by1 + 1
    #     elif i == 2:
    #         by2 = by2 + 1
    #     elif i == 3:
    #         by3 = by3 + 1
    #     elif i == 4:
    #         by4 = by4 + 1
    #     elif i == 5:
    #         by5 = by5 + 1
    #     elif i == 6:
    #         by6 = by6 + 1
    #     elif i == 7:
    #         by7 = by7 + 1

    # for i in countBlackAroundGreenOriginal:
    #     if i == 0:
    #         by0 = by0 + 1
    #     elif i == 1:
    #         by1 = by1 + 1
    #     elif i == 2:
    #         by2 = by2 + 1
    #     elif i == 3:
    #         by3 = by3 + 1
    #     elif i == 4:
    #         by4 = by4 + 1
    #     elif i == 5:
    #         by5 = by5 + 1
    #     elif i == 6:
    #         by6 = by6 + 1
    #     elif i == 7:
    #         by7 = by7 + 1

    # Combine length for countGreenAroundBlack and countGreenAroundBlackOriginal
    # combinedCountGreenAroundBlack = len(countGreenAroundBlack) + len(countGreenAroundBlackOriginal)
    # combinedCountBlackAroundGreen = len(countBlackAroundGreen) + len(countBlackAroundGreenOriginal)
    # ogyRelative = [0, 0.01, 0.007, 0.03, 0.08, 0.17, 0.27, 0.4]
    # obyRelative = [0, 0.007, 0.01, 0.009, 0.043, 0.13, 0.35, 0.475]

    # Calculate the frequency of occurrence
    #fgy0 = (gy0 / combinedCountGreenAroundBlack)
    #((a*b)*t) + (a*b)
    # for i in range(1, t):
    #     fgy0 = (gy0 / (a*b) * t)
    #     fgy1 = (gy1 / (a*b) * t)
    #     fgy2 = (gy2 / (a*b) * t)
    #     fgy3 = (gy3 / (a*b) * t)
    #     fgy4 = (gy4 / (a*b) * t)
    #     fgy5 = (gy5 / (a*b) * t)
    #     fgy6 = (gy6 / (a*b) * t)
    #     fgy7 = (gy7 / (a*b) * t)
    #     fby0 = (by0 / (a*b) * t)
    #     fby1 = (by1 / (a*b) * t)
    #     fby2 = (by2 / (a*b) * t)
    #     fby3 = (by3 / (a*b) * t)
    #     fby4 = (by4 / (a*b) * t)
    #     fby5 = (by5 / (a*b) * t)
    #     fby6 = (by6 / (a*b) * t)
    #     fby7 = (by7 / (a*b) * t)
    #
    # # Put calculated frequency into list
    # gy = [fgy0, fgy1, fgy2, fgy3, fgy4, fgy5, fgy6, fgy7]
    # by = [fby0, fby1, fby2, fby3, fby4, fby5, fby6, fby7]
    #
    # plt.plot(x, gy, color='green', linestyle='dashed', label='Green Around Black: Simulations')
    # plt.plot(x, by, color='black', linestyle='dashed', label='Black Around Green: Simulations')
    # plt.plot(x, ogy, color='green', label='Green Around Black: Observed')
    # plt.plot(x, oby, color='black', label='Black Around Green: Observed')
    #
    # plt.legend(loc="upper left")
    # plt.xlim([0, max(x)])
    # plt.ylim([0, max(gy) + 0.25])
    # plt.xlabel("Number of Neighbors")
    # plt.ylabel("Frequency")
    # plt.title("Number of Neighbors vs. Frequency")
    #
    # plt.show()

    iterate(newArray, startingAge + 1, maxAge)

# Create a 2D array (Original)
array = [[0 for i in range(a)] for j in range(b)]

# Create a 2D array (Count Green)
countGreenArray = [[0 for i in range(a)] for j in range(b)]
# Create a 2D array (Transformed)
newArray = [[0 for i in range(a)] for j in range(b)]

#Loop through entire 2D array
n = len(array)
m = len(array[0])
for i in range(0, n):
    for j in range(0, m):
        # Assign a character of either 0 or 1 (0 for black, 1 for green)
        array[i][j] = random.randint(0, 1)
        print(array[i][j], end="  ")
    print()

print("\n")

countGreenAroundBlackOriginal = []
countBlackAroundGreenOriginal = []
numberBlackOriginal = []
numberGreenOriginal = []
countGreenNeighbors = []
countBlackNeighbors = []

# Count the number of green around black and black around green in original 2D array

numBlack = 0
numGreen = 0

for i in range(0, n):
    for j in range(0, m):
        # Reset Green Count
        countOriginalGreen = 0
        # Count Number of Greens (1)
        # all the same for middle, left, and right
        countOriginalGreen = array[i][j] + array[i][(j - 1) % m] + array[i][(j + 1) % m]

        # If is the upper or lower edge
        if i == 0 | i == m:
            countOriginalGreen = countOriginalGreen + array[(i - 1) % m][(j - 1) % m] \
                         + array[(i - 1) % m][j] + array[(i + 1) % m][(j - 1) % m] + array[(i + 1) % m][j]
        # If is middle or left/right edge odd row
        if i % 2 == 1:
            countOriginalGreen = countOriginalGreen + array[(i - 1) % m][j] + array[(i - 1) % m][(j + 1) % m] \
                         + array[(i + 1) % m][j] + array[(i + 1) % m][(j + 1) % m]
        # If is middle or left/right edge even row
        elif i % 2 == 0:
            countOriginalGreen = countOriginalGreen + array[(i - 1) % m][(j - 1) % m] + array[(i - 1) % m][j] \
                         + array[(i + 1) % m][(j - 1) % m] + array[(i + 1) % m][j]
        # If center is not black
        if array[i][j] != 0:
            countBlackAroundGreenOriginal.append(7 - countOriginalGreen)
            numGreen = numGreen + 1
        else:
            countGreenAroundBlackOriginal.append(countOriginalGreen)
            numBlack = numBlack + 1

for i in range(0, n):
    for j in range(0, m):
        # Reset Green Count
        countOriginalGreenNeighbors = 0
        # Count Number of Greens (1)
        # all the same for middle, left, and right
        if array[i][j] == 1:
            countOriginalGreenNeighbors = array[i][(j - 1) % m] + array[i][(j + 1) % m]
        # If is the upper or lower edge
        if i == 0 | i == m:
            countOriginalGreen = countOriginalGreen + array[(i - 1) % m][(j - 1) % m] \
                                 + array[(i - 1) % m][j] + array[(i + 1) % m][(j - 1) % m] + array[(i + 1) % m][j]
        # If is middle or left/right edge odd row
        if i % 2 == 1:
            countOriginalGreen = countOriginalGreen + array[(i - 1) % m][j] + array[(i - 1) % m][(j + 1) % m] \
                                 + array[(i + 1) % m][j] + array[(i + 1) % m][(j + 1) % m]
        # If is middle or left/right edge even row
        elif i % 2 == 0:
            countOriginalGreen = countOriginalGreen + array[(i - 1) % m][(j - 1) % m] + array[(i - 1) % m][j] \
                                 + array[(i + 1) % m][(j - 1) % m] + array[(i + 1) % m][j]
        # If center is not black
        if array[i][j] != 0:
            countBlackAroundGreenOriginal.append(7 - (countOriginalGreen + 1))
            numGreen = numGreen + 1
        else:
            countGreenAroundBlackOriginal.append(countOriginalGreen)
            numBlack = numBlack + 1

# Duplicate array
countGreenArray = copy.deepcopy(array)
newArray = copy.deepcopy(array)

# Create a list
countGreenAroundBlack = []
countBlackAroundGreen = []
numberBlack = []
numberGreen = []

numberBlack.append(numBlack)
numberGreen.append(numGreen)

iterate(newArray, 0, t)

# Create a graph for the number of neighbors vs. frequency
# Observed Data
ogy = [0, 0.04, 0.23, 0.45, 0.25, 0.06, 0, 0]
oby = [0, 0, 0.03, 0.23, 0.48, 0.275, 0.04, 0]

# Count the number of 1-7 number of neighbors occur to calculate the frequency
gy0, gy1, gy2, gy3, gy4, gy5, gy6, gy7 = 0, 0, 0, 0, 0, 0, 0, 0
x = [0, 1, 2, 3, 4, 5, 6, 7]

by0, by1, by2, by3, by4, by5, by6, by7 = 0, 0, 0, 0, 0, 0, 0, 0
x = [0, 1, 2, 3, 4, 5, 6, 7]

# Testing purposes
print(countBlackAroundGreen)
print(countGreenAroundBlack)

for i in countGreenAroundBlack:
    if i == 0:
        gy0 = gy0 + 1
    elif i == 1:
        gy1 = gy1 + 1
    elif i == 2:
        gy2 = gy2 + 1
    elif i == 3:
        gy3 = gy3 + 1
    elif i == 4:
        gy4 = gy4 + 1
    elif i == 5:
        gy5 = gy5 + 1
    elif i == 6:
        gy6 = gy6 + 1
    elif i == 7:
        gy7 = gy7 + 1

for i in countGreenAroundBlackOriginal:
    if i == 0:
        gy0 = gy0 + 1
    elif i == 1:
        gy1 = gy1 + 1
    elif i == 2:
        gy2 = gy2 + 1
    elif i == 3:
        gy3 = gy3 + 1
    elif i == 4:
        gy4 = gy4 + 1
    elif i == 5:
        gy5 = gy5 + 1
    elif i == 6:
        gy6 = gy6 + 1
    elif i == 7:
        gy7 = gy7 + 1

for i in countBlackAroundGreen:
    if i == 0:
        by0 = by0 + 1
    elif i == 1:
        by1 = by1 + 1
    elif i == 2:
        by2 = by2 + 1
    elif i == 3:
        by3 = by3 + 1
    elif i == 4:
        by4 = by4 + 1
    elif i == 5:
        by5 = by5 + 1
    elif i == 6:
        by6 = by6 + 1
    elif i == 7:
        by7 = by7 + 1

for i in countBlackAroundGreenOriginal:
    if i == 0:
        by0 = by0 + 1
    elif i == 1:
        by1 = by1 + 1
    elif i == 2:
        by2 = by2 + 1
    elif i == 3:
        by3 = by3 + 1
    elif i == 4:
        by4 = by4 + 1
    elif i == 5:
        by5 = by5 + 1
    elif i == 6:
        by6 = by6 + 1
    elif i == 7:
        by7 = by7 + 1

# Combine length for countGreenAroundBlack and countGreenAroundBlackOriginal
combinedCountGreenAroundBlack = len(countGreenAroundBlack) + len(countGreenAroundBlackOriginal)
combinedCountBlackAroundGreen = len(countBlackAroundGreen) + len(countBlackAroundGreenOriginal)
ogyRelative = [0, 0.01, 0.007, 0.03, 0.08, 0.17, 0.27, 0.4]
obyRelative = [0, 0.007, 0.01, 0.009, 0.043, 0.13, 0.35, 0.475]

# Calculate the frequency of occurrence
fgy0 = (gy0 / combinedCountGreenAroundBlack)
fgy1 = (gy1 / combinedCountGreenAroundBlack)
fgy2 = (gy2 / combinedCountGreenAroundBlack)
fgy3 = (gy3 / combinedCountGreenAroundBlack)
fgy4 = (gy4 / combinedCountGreenAroundBlack)
fgy5 = (gy5 / combinedCountGreenAroundBlack)
fgy6 = (gy6 / combinedCountGreenAroundBlack)
fgy7 = (gy7 / combinedCountGreenAroundBlack)
fby0 = (by0 / combinedCountBlackAroundGreen)
fby1 = (by1 / combinedCountBlackAroundGreen)
fby2 = (by2 / combinedCountBlackAroundGreen)
fby3 = (by3 / combinedCountBlackAroundGreen)
fby4 = (by4 / combinedCountBlackAroundGreen)
fby5 = (by5 / combinedCountBlackAroundGreen)
fby6 = (by6 / combinedCountBlackAroundGreen)
fby7 = (by7 / combinedCountBlackAroundGreen)

# Put calculated frequency into list
gy = [fgy0, fgy1, fgy2, fgy3, fgy4, fgy5, fgy6, fgy7]
by = [fby0, fby1, fby2, fby3, fby4, fby5, fby6, fby7]

plt.plot(x, gy, color='green', linestyle='dashed', label='Green Around Black: Simulations')
plt.plot(x, by, color='black', linestyle='dashed', label='Black Around Green: Simulations')
plt.plot(x, ogy, color='green', label='Green Around Black: Observed')
plt.plot(x, oby, color='black', label='Black Around Green: Observed')

plt.legend(loc="upper left")
plt.xlim([0, max(x)])
plt.ylim([0, max(gy) + 0.25])
plt.xlabel("Number of Neighbors")
plt.ylabel("Frequency")
plt.title("Number of Neighbors vs. Frequency")

plt.show()

# Testing Purposes
# print(numberBlack)
# print(numberGreen)

iterations = []

for i in range(0, t+1):
    iterations.append(i)

# print(iterations)

plt.plot(iterations, numberBlack, color='black', label='Black')
plt.plot(iterations, numberGreen, color='green', label='Green')

plt.xlim([0, max(iterations)])
plt.ylim([0, max(numberBlack) + 0.25])
plt.xlabel("Time Points/Iterations")
plt.ylabel("Number of Scales")
plt.title("Time Points vs. Number of Scales")

plt.show()

# Create a graph for the number of neighbors vs. relative probability
# Observed Data
ogyRelative = [0, 0.01, 0.007, 0.03, 0.08, 0.17, 0.27, 0.4]
obyRelative = [0, 0.007, 0.01, 0.009, 0.043, 0.13, 0.35, 0.475]

x = [0, 1, 2, 3, 4, 5, 6, 7]

plt.plot(x, ogyRelative, color='green')
plt.plot(x, obyRelative, color='black')

plt.xlim([0, max(x)])
plt.ylim([0, max(obyRelative) + 0.25])
plt.xlabel("Number of Neighbors")
plt.ylabel("Relative Probability")
plt.title("Number of Neighbors vs. Relative Probability")

plt.show()