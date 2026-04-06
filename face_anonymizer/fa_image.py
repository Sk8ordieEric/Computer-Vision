import cv2
from pathlib import Path
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
#TODO working on solution for Face Anonymizer, Bbox not lined up
#path to the downloaded model and image
img_path = Path("portrait.jpg")
model_path = Path("C:/Users/Eric/Downloads/detector.tflite")
#Create the detector configuration
base_options = python.BaseOptions(model_asset_path=str(model_path))
options = vision.FaceDetectorOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    min_detection_confidence=0.5
)
with vision.FaceDetector.create_from_options(options) as detector:
    mp_image = mp.Image.create_from_file(str(img_path))
    detection_result = detector.detect(mp_image)
    img = cv2.imread(img_path)
    cv2.rectangle(img, (107, 116), (223, 232), (255, 0 , 0), 3)
    cv2.imshow("bbox", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# blur faces

# save image