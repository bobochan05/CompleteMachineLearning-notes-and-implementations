import cv2
import os
from ultralytics import YOLO


# ============================================================
# SETTINGS
# ============================================================

video_path = r"C:\Users\soham\Downloads\6387-191695740_medium.mp4"

model_path = "yolov8n.pt"


# ============================================================
# 1. MOTION-BASED TRACKING
#    BYTE TRACK
# ============================================================

print("Starting ByteTrack - Motion Based Tracking")

video = cv2.VideoCapture(video_path)

model = YOLO(model_path)

while True:

    ret, frame = video.read()

    if not ret:
        break

    # ByteTrack
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False
    )

    # Draw tracking results
    annotated_frame = results[0].plot()

    cv2.imshow(
        "ByteTrack - Motion Based",
        annotated_frame
    )

    key = cv2.waitKey(20) & 0xFF

    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()


# ============================================================
# 2. CREATE BoT-SORT CONFIG WITH ReID
#    MOTION + APPEARANCE
# ============================================================

botsort_config = """
tracker_type: botsort

track_high_thresh: 0.5
track_low_thresh: 0.1
new_track_thresh: 0.6
track_buffer: 30
match_thresh: 0.8

fuse_score: True

gmc_method: sparseOptFlow

proximity_thresh: 0.5
appearance_thresh: 0.8

with_reid: True
model: auto
"""

with open("botsort_reid.yaml", "w") as file:
    file.write(botsort_config)


# ============================================================
# 3. APPEARANCE-BASED TRACKING
#    BoT-SORT + ReID
# ============================================================

print("Starting BoT-SORT - Motion + Appearance Tracking")

video = cv2.VideoCapture(video_path)

model = YOLO(model_path)

while True:

    ret, frame = video.read()

    if not ret:
        break

    # BoT-SORT + ReID
    results = model.track(
        frame,
        persist=True,
        tracker="botsort_reid.yaml",
        verbose=False
    )

    # Draw tracking results
    annotated_frame = results[0].plot()

    cv2.imshow(
        "BoT-SORT - Motion + Appearance",
        annotated_frame
    )

    key = cv2.waitKey(20) & 0xFF

    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()