import cv2
import PIL
import numpy as np
from matplotlib import pyplot as plt
import copy

img = cv2.imread('pacman.png',0)
edges = cv2.Canny(img,100,200, True)

image_pil = PIL.Image.fromarray(np.uint8(plt.cm.gist_earth(edges)*255))
image_pil = image_pil.convert('1')

width, height = image_pil.size

p = image_pil.load()


def edgePaint(pixels):
    points = []
    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 255:
                newPoint = [x,y]
                newEdge, pixels = recurse([newPoint], pixels)
                points += [newEdge]
    return points

# check if any surrounding pixels are of the same color value
def counterclockwiseSearch(point, pixels):
    if(pixels[point[0] - 1, point[1] + 1] == 255):
        return [point[0] - 1, point[1] + 1]
    elif(pixels[point[0], point[1] + 1] == 255):
        return [point[0], point[1] + 1]
    elif(pixels[point[0] + 1, point[1] + 1] == 255):
        return [point[0] + 1, point[1] + 1]
    elif(pixels[point[0] + 1, point[1]] == 255):
        return [point[0] + 1, point[1]]
    else:
        return None

def recurse(points, pixels):
    if (not(counterclockwiseSearch(points[-1], pixels) == None)):
        newPoint = counterclockwiseSearch(points[-1], pixels)
        # hide the pixels that have already been accounted for
        pixels[newPoint[0], newPoint[1]] = 0
        return recurse(points + [newPoint], pixels)
    else:
        print("adding points")
        return points, pixels

print(edgePaint(p))

def test_repeated_points():
    points = edgePaint(p)
    seen = set()
    uniq = []
    for x in points:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
    assert seen
