from pathlib import Path
import cv2

path = Path()
cwd = path.cwd()
img_path = cwd.parent / "image_ops/butterfly.jpg"
img = cv2.imread(img_path)
cv2.imshow("frame", img)
cv2.waitKey(0)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.imshow('image', img_rgb)
cv2.waitKey(0)

cv2.imshow("gray image", img_gray)
cv2.waitKey(0)

cv2.imshow("HSV IMAGE", img_hsv)
cv2.waitKey(0)