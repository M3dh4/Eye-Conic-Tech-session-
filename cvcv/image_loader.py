import cv2
img = cv2.imread("cvcv/_ (2).jpeg")          # loads your image
cv2.imshow("Image is loaded!", img)       # shows it in a popup window
cv2.waitKey(0)                       # waits till you press any key
cv2.destroyAllWindows()             
