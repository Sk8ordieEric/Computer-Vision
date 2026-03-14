from pathlib import Path
import cv2

img = cv2.imread(Path("butterfly.jpg"))

img2 = cv2.resize(img, (600, 400))
print(img2.shape)
cv2.imshow("butterfly3.jpg", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(Path("butterfly3.jpg"), img2)
