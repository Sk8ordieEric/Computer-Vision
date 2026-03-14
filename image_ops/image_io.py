import cv2

from pathlib import Path

# read image
image_path = "butterfly.jpg"
img = cv2.imread(image_path)

resized = cv2.resize(img, (300, 200))


# write image
# img_write_path = Path(".") / "new_image.jpg"
cv2.imwrite("butterfly.jpg", resized)

# visualize image
img2 = cv2.imread("butterfly.jpg")
cv2.imshow('image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()