import cv2
import numpy as np
from ultralytics import YOLO


# Load YOLOv8 segmentation model
# -seg = segmentation model
model = YOLO("yolov8n-seg.pt")


# ============================================================
# WEBCAM
# ============================================================

cap = cv2.VideoCapture(0)

while True:

    # Read frame from webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO segmentation
    results = model(frame, verbose=False)

    # First result
    result = results[0]

    # Get segmentation masks
    # masks.data = pixel-level masks
    # masks.xy   = polygon coordinates outlining objects
    masks = result.masks

    if masks is not None:

        for i, polygon in enumerate(masks.xy):

            # Get class ID and class name
            class_id = int(result.boxes.cls[i])
            label = model.names[class_id]

            # Get confidence
            confidence = float(result.boxes.conf[i])

            # Convert polygon to OpenCV format
            polygon = polygon.astype(np.int32)

            # Create overlay
            overlay = frame.copy()

            # Fill the segmented region
            # Green = (B, G, R)
            cv2.fillPoly(
                overlay,
                [polygon],
                (0, 255, 0)
            )

            # Make mask transparent
            frame = cv2.addWeighted(
                frame,
                0.7,
                overlay,
                0.3,
                0
            )

            # Draw mask boundary
            cv2.polylines(
                frame,
                [polygon],
                True,
                (0, 255, 0),
                2
            )

            # Get bounding box
            x1, y1, x2, y2 = result.boxes.xyxy[i].cpu().numpy().astype(int)

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Display class + confidence
            text = f"{label} {confidence:.2f}"

            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Display result
    cv2.imshow("YOLOv8 Segmentation", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()


# ============================================================
# VIDEO
# ============================================================

video = cv2.VideoCapture(
    r"C:\Users\soham\Downloads\6387-191695740_medium.mp4"
)

while True:

    # Read frame
    ret, frame = video.read()

    if not ret:
        break

    # Run segmentation
    results = model(frame, verbose=False)
    result = results[0]

    # Get masks
    masks = result.masks

    if masks is not None:

        for i, polygon in enumerate(masks.xy):

            # Class
            class_id = int(result.boxes.cls[i])
            label = model.names[class_id]

            # Confidence
            confidence = float(result.boxes.conf[i])

            # Polygon = exact outline of object
            polygon = polygon.astype(np.int32)

            # Create mask overlay
            overlay = frame.copy()

            # Fill segmentation area
            cv2.fillPoly(
                overlay,
                [polygon],
                (0, 255, 0)
            )

            # Blend mask with original frame
            frame = cv2.addWeighted(
                frame,
                0.7,
                overlay,
                0.3,
                0
            )

            # Draw segmentation outline
            cv2.polylines(
                frame,
                [polygon],
                True,
                (0, 255, 0),
                2
            )

            # Bounding box
            x1, y1, x2, y2 = result.boxes.xyxy[i].cpu().numpy().astype(int)

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Label
            cv2.putText(
                frame,
                f"{label} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Show video
    cv2.imshow("YOLOv8 Segmentation - Video", frame)

    # Q = quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()