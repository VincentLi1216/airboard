import cv2
import numpy as np

image = cv2.imread('./example_dir/cropped_example_30.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_green = np.array([47, 14, 82])
upper_green = np.array([110, 120, 182])
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Input', image)
cv2.imshow('Result', res)
cv2.waitKey(0)
