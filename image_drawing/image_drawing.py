from helpful_cv_scripts import context_manager as cm
from pathlib import Path
import cv2

img_path = Path("C:/Users/Eric/PycharmProjects/PythonProject1/Computer_Vision/image_drawing/whiteboard.jpg")

with cm.cv_show_image(img_path):
    img = cv2.imread(img_path)
    # print(img.shape)
    # Drawing a line on top of the image. Arguments that are needed:
    # Image loaded into memory, first point XY coordinate, second point XY coordinate
    # Tuple defining the color of the line in current colorspace, and pixel count for line thickness
    # cv2.line(img, (200, 200), (250, 400), (255, 0, 0), 4)
    # Drawing a rectangle, arguments needed:
    # Image in memory, first point in XY is upper left corner, second point is the lower right corner
    # Tuple defining the color of the lines, and pixel count for thickness of line. If a thickness of -1
    # is used then the whole shape is filled in with color
    cv2.rectangle(img, (500, 500), (800, 200), (0, 255, 0), 3)
    # cv2.rectangle(img, (500, 500), (800, 200), (0, 255, 0), -1)
    # Drawing a circle: image in memory, a point for center of circle, radius in pixels,
    # tuple for the color, and thickness value
    cv2.circle(img, (350, 400), 50, (255, 0, 0), 3)
    # Drawing text on top of image: image in memory, string of text to draw, XY coordinates
    # to start the text, type of font to use that's in OpenCv, size of the font/font scale, color of font.
    # and the thickness of the text

    cv2.putText(img, "Testing drawing", (300, 170), cv2.FONT_HERSHEY_SIMPLEX, 3,  (0, 0, 255),
                4)
    cv2.imshow("img", img)
    cv2.waitKey(0)