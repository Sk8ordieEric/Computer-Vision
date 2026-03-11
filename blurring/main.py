from pathlib import Path
import cv2

img_path = Path("freelancer.jpg")
img = cv2.imread(img_path)



k_size = 21
img_blur = cv2.blur(img, (k_size, k_size))
img_gauss_blur = cv2.GaussianBlur(img, (k_size, k_size, ), 0)
img_median_blur = cv2.medianBlur(img, k_size)
cv2.imshow("img", img)


cv2.imshow("img_blur", img_blur)
cv2.imshow("gauss blur", img_gauss_blur)
cv2.imshow("median", img_median_blur)
cv2.waitKey(0)

