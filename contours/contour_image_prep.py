from helpful_cv_scripts import context_manager as cm
from pathlib import Path
import cv2
# Changing an image into a binary image to be used in contour operations
img_path = Path("C:/Users/Eric/PycharmProjects/PythonProject1/Computer_Vision/contours/bird_flock.jpg")

with cm.cv_show_image(img_path):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 63, 32)
    mean_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 11, 10)
    cv2.imshow("img", img)
    cv2.imshow("gaussian", thresh)
    cv2.imshow("mean", mean_thresh)
    binary = Path("C:/Users/Eric/PycharmProjects/PythonProject1/Computer_Vision/contours/binary.jpg")
    cv2.imwrite(binary, thresh)
    cv2.waitKey(0)