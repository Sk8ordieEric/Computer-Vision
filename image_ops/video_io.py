import cv2
from pathlib import Path

# read video
video_path = Path() / "city_video.mp4"

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow("frame", frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()