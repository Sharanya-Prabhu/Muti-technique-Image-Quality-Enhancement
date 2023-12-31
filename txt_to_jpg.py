import cv2
import numpy as np
import sys

# Read the image dimensions from the file
with open('output.txt', 'r') as f:
    width, height = map(int, f.readline().split())

# Read the pixel values from the file
pixels = []
with open('output.txt', 'r') as f:
    next(f)  # Skip the first line (image dimensions)
    for line in f:
        r, g, b = map(int, line.split())
        pixels.append((r, g, b))  

# Convert the pixel values to a NumPy array
arr = np.array(pixels, dtype=np.uint8).reshape(height, width, 3)

# Save the image as a JPEG file
cv2.imwrite(sys.argv[1], arr)
