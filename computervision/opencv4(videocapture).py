import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(0)  # Step 1: connect to webcam (0 = default camera)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
    
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2880)

cv2.namedWindow('Webcam Feed', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Webcam Feed', 2880, 1800)

while True:                        # Step 2: keep grabbing frames forever, until we say stop
    ret, frame = cap.read()        # Step 3: grab the next frame
    # ret   = True/False -> did we successfully get a frame?
    # frame = the actual image (just like img from cv2.imread!)

    if not ret:
        print("Error: Could not read frame.")
        break                       # Step 4: if no frame came back, stop (camera disconnected/video ended)

    cv2.imshow('Webcam Feed', frame)   # Step 5: display the frame in a window

    # Step 6: this is where you'd do anything else to the frame -
    # e.g. cv2.cvtColor(frame, ...), detect faces, run a YOLO model, etc.

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break                       # Step 7: let the user press 'q' to quit the loop

cap.release()                       # Step 8: release the camera so other programs can use it
cv2.destroyAllWindows()             # Step 9: close the display window

#Run it, and a live window titled "Webcam Feed" should pop up. 
# Click into that window and press q to close it cleanly — clicking the terminal and pressing q won't work, 
# since waitKey only listens while the OpenCV window itself is focused.