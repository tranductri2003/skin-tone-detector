import cv2
import skin_detector

img_path = input("Please Enter Image Path")
image = cv2.imread(img_path)
mask = skin_detector.process(image)
cv2.imshow("input", image)
cv2.imshow("mask", mask)
cv2.waitKey(0)