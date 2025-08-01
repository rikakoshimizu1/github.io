import random
import copy
from hexalattice.hexalattice import *
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2
from PIL import Image

# Fixed size of array
a = 20
b = 20

# Fixed number of iterations
t = 10

counter = 1

# Iterations n times
def iterate(array, startingAge, maxAge):
    global countGreenArray, n, m, newArray, countGreenAroundBlack, countBlackAroundGreen, counter
    if startingAge == maxAge:
        return

    # Juvenile
    if startingAge <= 15:
        for i in range(0, n):
            for j in range(0, m):
                # Reset Green Count
                countGreen = 0
                # Count Number of Greens (1)
                countGreen = array[i][j] + array[i][(j - 1) % m] + array[(i + 1) % m][(j - 1) % m] + array[(i - 1) % m][j] + array[(i + 1) % m][j] + array[(i - 1) % m][(j + 1) % m] + array[i][(j + 1) % m]
                if countGreen == 0 or countGreen == 1 or countGreen == 2:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                        newArray[i][j] = 1
                        countGreen += 1
                    else:
                        # 7-countGreen because there are 7 neighbors
                        countBlackAroundGreen.append(7-countGreen)
                        if array[i][(j - 1) % m] == 0:
                            newArray[i][(j - 1) % m] = 1
                        elif array[(i + 1) % m][(j - 1) % m] == 0:
                            newArray[(i + 1) % m][(j - 1) % m] = 1
                        elif array[(i - 1) % m][j] == 0:
                            newArray[(i - 1) % m][j] = 1
                        elif array[(i + 1) % m][j] == 0:
                            newArray[(i + 1) % m][j] = 1
                        elif array[(i - 1) % m][(j + 1) % m] == 0:
                            newArray[(i - 1) % m][(j + 1) % m] = 1
                        else:
                            newArray[i][(j + 1) % m] = 1
                        countGreen += 1
                    countGreenArray[i][j] = countGreen
                elif countGreen == 3:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                    else:
                        countBlackAroundGreen.append(7-countGreen)
                    countGreenArray[i][j] = countGreen
                    newArray[i][j] = 0
                else:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                    else:
                        countBlackAroundGreen.append(7-countGreen)
                    countGreenArray[i][j] = countGreen
                    newArray[i][j] = 0
                print(newArray[i][j], end="  ")
            print()
        print("\n")

    # Adult
    else:
        for i in range(0, n):
            for j in range(0, m):
                # Count Number of Greens (1)
                # Reset Green Count
                countGreen = 0
                countGreen = array[i][j] + array[i][(j - 1) % m] + array[(i + 1) % m][(j - 1) % m] + array[(i - 1) % m][j] + array[(i + 1) % m][j] + array[(i - 1) % m][(j + 1) % m] + array[i][(j + 1) % m]
                if countGreen == 0 or countGreen == 1 or countGreen == 2:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                    else:
                        countBlackAroundGreen.append(7-countGreen)
                        if array[i][(j - 1) % m] == 0:
                            newArray[i][(j - 1) % m] = 1
                        elif array[(i + 1) % m][(j - 1) % m] == 0:
                            newArray[(i + 1) % m][(j - 1) % m] = 1
                        elif array[(i - 1) % m][j] == 0:
                            newArray[(i - 1) % m][j] = 1
                        elif array[(i + 1) % m][j] == 0:
                            newArray[(i + 1) % m][j] = 1
                        elif array[(i - 1) % m][(j + 1) % m] == 0:
                            newArray[(i - 1) % m][(j + 1) % m] = 1
                        else:
                            newArray[i][(j + 1) % m] = 1
                        countGreen += 1
                    countGreenArray[i][j] = countGreen
                    newArray[i][j] = 1
                elif countGreen == 3:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                    else:
                        countBlackAroundGreen.append(7-countGreen)
                    countGreenArray[i][j] = countGreen
                else:
                    # If center hex is black
                    if array[i][j] == 0:
                        countGreenAroundBlack.append(countGreen)
                    else:
                        countBlackAroundGreen.append(7-countGreen)
                    countGreenArray[i][j] = countGreen
                    newArray[i][j] = 0
                print(newArray[i][j], end="  ")
            print()
        print("\n")

    colors = np.zeros([a*b, 3])
    # CMYK color green: (0.00, 1.00, 0.00)
    # CMYK color black: (0.85, 0.85, 0.85)

    k=0
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
                                     align_to_origin = True,
                                     face_color = colors
                                     )

    x_hex_coords = hex_centers[:, 0]
    y_hex_coords = hex_centers[:, 1]

    # For testing purposes
    # print(x_hex_coords[0])
    #plt.show()

    # MANUALLY CHANGE
    path = 'C:/Users/shimizr/Desktop/MA497/SimulationGraphics/Simulation20x50_10'
    if not os.path.exists(path):
        os.makedirs(path)

    # while os.path.exists(path):
    #     i = i + 1
    plt.savefig(path + '/sim' + str(counter) + '.png')
    counter = counter+1

    plt.show()
    #plt.close()

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

# Duplicate array
countGreenArray = copy.deepcopy(array)
newArray = copy.deepcopy(array)

# Create a list
countGreenAroundBlack = []
countBlackAroundGreen = []

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

# Calculate the frequency of occurrence
fgy0 = (gy0 / len(countGreenAroundBlack))
fgy1 = (gy1 / len(countGreenAroundBlack))
fgy2 = (gy2 / len(countGreenAroundBlack))
fgy3 = (gy3 / len(countGreenAroundBlack))
fgy4 = (gy4 / len(countGreenAroundBlack))
fgy5 = (gy5 / len(countGreenAroundBlack))
fgy6 = (gy6 / len(countGreenAroundBlack))
fgy7 = (gy7 / len(countGreenAroundBlack))
fby0 = (by0 / len(countBlackAroundGreen))
fby1 = (by1 / len(countBlackAroundGreen))
fby2 = (by2 / len(countBlackAroundGreen))
fby3 = (by3 / len(countBlackAroundGreen))
fby4 = (by4 / len(countBlackAroundGreen))
fby5 = (by5 / len(countBlackAroundGreen))
fby6 = (by6 / len(countBlackAroundGreen))
fby7 = (by7 / len(countBlackAroundGreen))

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

# Simulation Video Generator
# MANUALLY CHANGE
# path = 'C:/Users/shimizr/Desktop/MA497/SimulationGraphics/Simulation5x5_10'
# os.chdir('C:/Users/shimizr/Desktop/MA497/SimulationGraphics/Videos')
#
# mean_height = 0
# mean_width = 0
#
# num_of_images = len(os.listdir('.'))
#
# for file in os.listdir('.'):
#     im = Image.open(os.path.join(path, file))
#     width, height = im.size
#     mean_width += width
#     mean_height += height
#
# mean_width = int(mean_width/num_of_images)
# mean_height = int(mean_height/num_of_images)

# for file in os.listdir('.'):
#     if file.endswith(".png") or file.endswith("png"):
#         im=Image.open(os.path.join(path,file))
#
#         width,height = im.size
#         print(width,height)
#
#         imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
#         imResize.save( file, 'PNG', quality=95)

# def generate_video():
#     # MANUALLY CHANGE
#     image_folder = 'C:/Users/shimizr/Desktop/MA497/SimulationGraphics/Simulation5x5_10'
#     video_name = "Simulation5x5_10"
#     os.chdir('C:/Users/shimizr/Desktop/MA497/SimulationGraphics/Videos')
#
#     images = [img for img in os.listdir(image_folder)
#               if img.endswith("png") or
#               img.endswith(".png")]
#
#     frame = cv2.imread(os.path.join(image_folder, images[0]))
#
#     height,width,layers = frame.shape
#
#     video = cv2.VideoWriter(video_name, 0, 1, (width, height))
#
#     for image in images:
#         video.write(cv2.imread(os.path.join(image_folder, image)))
#
#     cv2.destroyAllWindows()
#     video.release()
#
# generate_video()

# video_name = 'Simulations5x5_10.avi'
#
# images = [img for img in os.listdir(image_folder)]
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape
#
# video = cv2.VideoWriter(video_name, 0, 1, (width, height))
#
# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))
#
# cv2.destroyAllWindows()
# video.release()



