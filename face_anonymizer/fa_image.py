import numpy as np
import cv2
from pathlib import Path
import mediapipe as mp



TEXT_COLOR = (255, 0, 0) # Red text color
K_SIZE = 50 # Kernel size for the anonymizer blurring

def import_model():
    # Add an input() function to input another image
    img_path = str(Path("portrait.jpg")) # needs to be a string type for FaceDetectorOptions
    model_path = str(Path("detector.tflite")) # Also needs to be a string type for FaceDetector Options
    return img_path, model_path


"""Draws bounding boxes and keypoints on the input image and return it.
Args:
image: The input RGB image.
detection_result: The list of all "Detection" entities to be visualize.
Returns:
Image with bounding boxes.
"""

def visualize(image, detection_result):
    annotated_image = image.copy()
    height, width, _ = image.shape

    for detection in detection_result.detections:
        bbox = detection.bounding_box
        start_point = bbox.origin_x, bbox.origin_y
        end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
        # cv2.rectangle(annotated_image, start_point, end_point, TEXT_COLOR, 3)
        # Uncomment the above line for a bounding box detection drawn on the image

    return annotated_image, start_point, end_point


# Create the detector configuration
def detector_config(model_path):
    BaseOptions = mp.tasks.BaseOptions
    FaceDetector = mp.tasks.vision.FaceDetector
    FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
    VisionRunningMode = mp.tasks.vision.RunningMode
    options = FaceDetectorOptions(base_options=BaseOptions(model_asset_path=model_path),
                                  running_mode=VisionRunningMode.IMAGE,
                                  min_detection_confidence=0.5)
    return FaceDetector, options

def run_detector_inference(img_path, model_path):
    face_detector, detect_options = detector_config(model_path)
    with face_detector.create_from_options(detect_options) as detector:
        try:
            mp_image = mp.Image.create_from_file(img_path)
            img = cv2.imread(img_path)
            detection_result = detector.detect(mp_image)
            if detection_result is None:
                raise TypeError
            image_copy = np.copy(mp_image.numpy_view())
            bbox_image, pt1, pt2 = visualize(image_copy, detection_result)
            rgb_bbox_img = cv2.cvtColor(bbox_image, cv2.COLOR_BGR2RGB)
            # Blurring the image by applying the blur to the face only, taking a slice of the image of the face
            # dimensions and assigning the blur to the image in the same bounding box dimension
            rgb_bbox_img[pt1[1]:pt2[1], pt1[0]:pt2[0]] = cv2.blur(rgb_bbox_img[pt1[1]:pt2[1], pt1[0]:pt2[0]],
                                                                  (K_SIZE,K_SIZE))
            cv2.imshow("face anon", rgb_bbox_img)
            cv2.imshow("original", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except TypeError as e:
            print(f"Script stopped due to {e} from a None type returned from Face Detector.\n"
                  f"Please check the image to make sure there is a human face in it.")

def main():
    img_path, model = import_model()
    run_detector_inference(img_path, model)

if __name__ == "__main__":
    main()

