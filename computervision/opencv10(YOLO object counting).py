import cv2
from ultralytics import YOLO

# Load YOLOv8 model
# yolov8m.pt = medium object detection model
model = YOLO("yolov8m.pt")

# Open video
video = cv2.VideoCapture(r"C:\Users\soham\Downloads\6387-191695740_medium.mp4")

# Set to store unique tracking IDs
# A set automatically avoids duplicates
seen_ids = set()

while True:

    # Read frame
    ret, frame = video.read()

    if not ret:
        break

    # Track people
    # classes=[0] -> only person
    # persist=True -> keep IDs consistent between frames
    results = model.track(
        frame,
        persist=True,
        verbose=False,
        classes=[0]
    )

    # Check if tracking IDs exist
    if results[0].boxes.id is not None:

        # Get all IDs in current frame
        for track_id in results[0].boxes.id:

            # Add ID to set
            seen_ids.add(int(track_id))

    # Total unique people seen so far
    total_unique_count = len(seen_ids)

    # Draw boxes, IDs and labels
    annotated_frame = results[0].plot()

    # Display total count
    cv2.putText(
        annotated_frame,
        f"Unique People: {total_unique_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show video
    cv2.imshow(
        "YOLOv8 Person Tracking",
        annotated_frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

print("Total unique people:", total_unique_count)