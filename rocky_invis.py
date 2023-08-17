import cv2
import numpy as np

# Load the image with the black object and the background image
black_object = cv2.imread('IMG_0463.jpg')
background = cv2.imread('IMG_0464.jpg')

# Define the black color range in grayscale
lower_black = np.array([0])
upper_black = np.array([50])

# Convert the images to grayscale
black_object_gray = cv2.cvtColor(black_object, cv2.COLOR_BGR2GRAY)

# Create a mask that identifies the black object
mask = cv2.inRange(black_object_gray, lower_black, upper_black)

# Invert the mask
inverted_mask = cv2.bitwise_not(mask)

# Apply the mask to the black object and the inverted mask to the background
invisible_object = cv2.bitwise_and(black_object, black_object, mask=inverted_mask)
visible_background = cv2.bitwise_and(background, background, mask=mask)

# Combine the two images to create the final result
final_image = cv2.add(invisible_object, visible_background)

# Display the final result
cv2.imshow('Invisibility Effect', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()