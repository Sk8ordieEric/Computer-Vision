from contextlib import contextmanager
import cv2

"""Import this module like: from helpful_cv_scripts import context manager
And run in the terminal at the project root: python -m parent_folder.script
parent_folder is the directory the script is in, script is the name of the
python script, don't put the .py extension, you want this to ran as a module
with the -m flag """
"""enter with block
     ↓
run setup
     ↓
yield → execute user code
     ↓
resume function
     ↓
run cleanup"""
@contextmanager
def cv_show_image(src):
    try:
        yield
    finally:
        cv2.destroyAllWindows()
@contextmanager
def cv_display_video(video):
    try:
        yield
    finally:
        video.release()
        cv2.destroyAllWindows()


# Test scripts for testing the context manager functions
# img_path = Path() / "./image_ops/butterfly.jpg"
#
# with cv_show_image(img_path):
#     img = cv2.imread(img_path)
#     cv2.imshow("img", img)
#     cv2.waitKey(0)
#
# vid_path = Path() / "./image_ops/city_video.mp4"
# video = cv2.VideoCapture(vid_path)
#
# with cv_display_video(video):
#     ret = True
#     while ret:
#         ret, frame = video.read()
#         if ret:
#             cv2.imshow("frame", frame)
#             cv2.waitKey(40)


