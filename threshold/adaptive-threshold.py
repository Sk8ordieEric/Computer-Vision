from pathlib import Path
import cv2

img_path = Path("handwritten.jpg")
img = cv2.imread(img_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Example of the global threshold that doesn't work to help create a clear image
# in this case
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
# Now trying the adaptive threshold method in CV2
adapt_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv2.THRESH_BINARY, 21, 30)

cv2.imshow("img", img)
# cv2.imshow("gray", img_gray)
cv2.imshow("global thresh", thresh)
cv2.imshow("adaptive", adapt_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()