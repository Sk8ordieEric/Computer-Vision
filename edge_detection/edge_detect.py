import cv2

from helpful_cv_scripts import context_manager as cm
from pathlib import Path
import numpy as np

img_path = Path("C:/Users/Eric/PycharmProjects/PythonProject1/Computer_Vision/edge_detection/basketball_player.jpg")
kernel = np.ones((3, 3),dtype=np.uint8)
with cm.cv_show_image(img_path):
    img = cv2.imread(img_path)
    edge = cv2.Canny(img, 100, 250)
    dilated = cv2.dilate(edge, kernel)
    eroded = cv2.erode(dilated, kernel)
    cv2.imshow("img", img)
    cv2.imshow("edge", edge)
    cv2.imshow("dilated", dilated)
    cv2.imshow("erode", eroded)
    cv2.waitKey(0)