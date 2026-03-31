import cv2
from PIL import Image
import numpy as np

def get_limits(color):
    c = np.uint8([[color]]) #passing the color as a 1x1 pixel as numpy array
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) #converting BGR color to HSV

    low_limit = hsvC[0][0][0] - 10, 100, 100 #setting the low end range for the HSV colorspace
    up_limit = hsvC[0][0][0] + 10, 255, 255 #setting the upper end range for the HSV colorspace

    return low_limit, up_limit

def main():

    blue = (255, 0, 0)

    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_limit, upper_limit = get_limits(color=blue)
        lower_limit = np.array(lower_limit, dtype=np.uint8)
        upper_limit = np.array(upper_limit, dtype=np.uint8)
        mask = cv2.inRange(hsv_img,lower_limit, upper_limit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.imshow("video", frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()