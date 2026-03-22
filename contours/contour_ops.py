from helpful_cv_scripts import context_manager as cm
import cv2
from pathlib import Path

img_path = Path("C:/Users/Eric/PycharmProjects/PythonProject1/Computer_Vision/contours/binary.jpg")

with cm.cv_show_image(img_path):
    img = cv2.imread(img_path)
    bin_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(bin_image, 127, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        if cv2.contourArea(cont) > 200: # Trying to remove the noise, so findContours returns only actual contours
            x, y, w, h = cv2.boundingRect(cont) # Getting the XY upper left corner, and width/height for the bounding box
                                                  # of each contour
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) # Drawing the bounding box over each contour
    cv2.imshow("img", img)

    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)