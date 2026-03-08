from pathlib import Path
import cv2

img_path = Path("butterfly2.jpg")
img = cv2.imread(img_path)
cv2.imshow("frame", img)
cv2.waitKey(0)
cropped_img = img[120:570, 100:400]

cv2.imshow("image", cropped_img)
cv2.waitKey(0)