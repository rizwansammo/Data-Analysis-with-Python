import cv2
import numpy as np

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with the actual path of your image
original_image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key event and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
