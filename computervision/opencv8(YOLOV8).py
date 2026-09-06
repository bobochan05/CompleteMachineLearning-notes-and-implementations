import cv2
from ultralytics import YOLO


# ============================================================
# YOLO MODEL
# ============================================================

# Load pretrained YOLOv8 Nano model
model1 = YOLO("yolov8n.pt")
model2 = YOLO("yolov8m.pt") 


# ============================================================
# FILE PATHS
# ============================================================

video_path = r"C:\Users\soham\Downloads\1900-151662242_small.mp4"


# ============================================================
# 1. VIDEO WITHOUT YOLO
# ============================================================

print("1. Playing video without YOLO")
print("Press Q to quit.")

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: Could not open video.")
else:

    while True:

        # Read one frame from the video
        ret, frame = video.read()

        # Stop when video ends
        if not ret:
            break

        # Display the frame
        cv2.imshow("Video - No YOLO", frame)

        # Press Q to quit
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()


# ============================================================
# COCO DATASET
# ============================================================

"""
COCO = Common Objects in Context

COCO is a large-scale computer vision dataset used for:

    - Object detection
    - Instance segmentation
    - Image captioning
    - Keypoint detection

COCO contains 330K+ images, with 200K+ labeled images.

The commonly used COCO object-detection benchmark contains
80 object categories.

Examples of COCO classes:

    person
    bicycle
    car
    motorcycle
    airplane
    bus
    train
    truck
    boat
    traffic light
    dog
    cat
    chair
    bottle
    laptop
    cell phone
    etc.

YOLO models are commonly trained/evaluated using COCO.

Other computer vision models such as:

    - Faster R-CNN
    - Mask R-CNN
    - RetinaNet
    - DETR

are also commonly associated with COCO.

For object detection, the model essentially learns:

    Image
       ↓
    Objects
       ↓
    Bounding boxes + Classes + Confidence

For example:

    Person  → bounding box + confidence
    Car     → bounding box + confidence
    Dog     → bounding box + confidence
"""


# ============================================================
# 2. WEBCAM WITHOUT YOLO
# ============================================================

print("2. Opening webcam without YOLO")
print("Press Q to quit.")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")

else:

    # Optional: make the window resizable
    cv2.namedWindow("Webcam - No YOLO", cv2.WINDOW_NORMAL)

    while True:

        # Read frame from webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read webcam frame.")
            break

        # Display webcam frame
        cv2.imshow("Webcam - No YOLO", frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()


# ============================================================
# 3. VIDEO WITH YOLOv8
# ============================================================

print("3. Playing video with YOLOv8")
print("Press Q to quit.")

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: Could not open video.")

else:

    while True:

        # Read one frame
        ret, frame = video.read()

        if not ret:
            break

        # Run YOLO on the current frame
        results = model1(frame, verbose=False)

        # Draw bounding boxes, class names and confidence
        annotated_frame = results[0].plot()

        # Display detected frame
        cv2.imshow("Video - YOLOv8", annotated_frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()


# ============================================================
# 4. WEBCAM WITH YOLOv8
# ============================================================

print("4. Opening webcam with YOLOv8")
print("Press Q to quit.")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")

else:

    cv2.namedWindow("Webcam - YOLOv8", cv2.WINDOW_NORMAL)

    while True:

        # Read frame from webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read webcam frame.")
            break

        # Run YOLO on webcam frame
        results = model1(frame, verbose=False)

        # Draw detections
        annotated_frame = results[0].plot()

        # Display
        cv2.imshow("Webcam - YOLOv8", annotated_frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()


# ============================================================
# 3. VIDEO WITH YOLOv8 medium
# ============================================================

print("3. Playing video with YOLOv8")
print("Press Q to quit.")

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: Could not open video.")

else:

    while True:

        # Read one frame
        ret, frame = video.read()

        if not ret:
            break

        # Run YOLO on the current frame
        results = model2(frame, verbose=False)

        # Draw bounding boxes, class names and confidence
        annotated_frame = results[0].plot()

        # Display detected frame
        cv2.imshow("Video - YOLOv8", annotated_frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()


# ============================================================
# 4. WEBCAM WITH YOLOv8 medium
# ============================================================

print("4. Opening webcam with YOLOv8")
print("Press Q to quit.")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")

else:

    cv2.namedWindow("Webcam - YOLOv8", cv2.WINDOW_NORMAL)

    while True:

        # Read frame from webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read webcam frame.")
            break

        # Run YOLO on webcam frame
        results = model2(frame, verbose=False)

        # Draw detections
        annotated_frame = results[0].plot()

        # Display
        cv2.imshow("Webcam - YOLOv8", annotated_frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()