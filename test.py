import cv2
from helpful_cv_scripts.context_manager import cv_show_image as si
from pathlib import Path

"""def cv_show_image(src):
    try:
        yield
    finally:
        cv2.destroyAllWindows()"""

img_path = Path("./image_ops/butterfly.jpg")

with si(img_path):
    img = cv2.imread(img_path)
    cv2.imshow("img", img)
    cv2.waitKey(0)

