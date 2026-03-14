import cv2
from pathlib import Path

img_path = Path("bear.jpg")

img = cv2.imread(img_path)
# Need to convert the image to grayscale before making a threshold/binary image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# threshold method returns a tuple of two values: threshold float value and the
# new threshold applied image in the usual pixel array format
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
# removing the noise/fuzziness with blur function
filtered_thresh = cv2.medianBlur(thresh, 5)
print(ret)
cv2.imshow("img", img)
cv2.imshow("gray", img_gray)
cv2.imshow("thresh", thresh)
cv2.imshow("filtered", filtered_thresh)
cv2.waitKey(0)

