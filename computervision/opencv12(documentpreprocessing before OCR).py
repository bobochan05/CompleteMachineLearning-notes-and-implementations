import cv2
import numpy as np


# ============================================================
# LOAD BOTH IMAGES
# ============================================================

image1 = cv2.imread(
    r"C:\Users\soham\Downloads\F921G4IIJX58MRB.LARGE_.jpg"
)

image2 = cv2.imread(
    r"C:\Users\soham\Downloads\save_text_ocr.jpg"
)


# Check if images loaded
if image1 is None:
    print("Image 1 not found. Check the path.")

if image2 is None:
    print("Image 2 not found. Check the path.")


# ============================================================
# IMAGE 1 - GRAYSCALE
# ============================================================

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)


# ============================================================
# IMAGE 1 - BINARIZATION
# ============================================================

_, binary1 = cv2.threshold(
    gray1,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)




# ============================================================
# IMAGE 1 - DESKEW
# ============================================================

coords1 = np.column_stack(np.where(binary1 > 0))

angle1 = cv2.minAreaRect(coords1)[-1]

if angle1 < -45:
    angle1 = -(90 + angle1)
else:
    angle1 = -angle1

(h1, w1) = binary1.shape

center1 = (w1 // 2, h1 // 2)

M1 = cv2.getRotationMatrix2D(
    center1,
    angle1,
    1.0
)

deskewed1 = cv2.warpAffine(
    binary1,
    M1,
    (w1, h1),
    flags=cv2.INTER_CUBIC,
    borderMode=cv2.BORDER_REPLICATE
)


# ============================================================
# IMAGE 2 - GRAYSCALE
# ============================================================

gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


# ============================================================
# IMAGE 2 - BINARIZATION
# ============================================================

_, binary2 = cv2.threshold(
    gray2,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)




# ============================================================
# IMAGE 2 - DESKEW
# ============================================================

coords2 = np.column_stack(np.where(binary2 > 0))

angle2 = cv2.minAreaRect(coords2)[-1]

if angle2 < -45:
    angle2 = -(90 + angle2)
else:
    angle2 = -angle2

(h2, w2) = binary2.shape

center2 = (w2 // 2, h2 // 2)

M2 = cv2.getRotationMatrix2D(
    center2,
    angle2,
    1.0
)

deskewed2 = cv2.warpAffine(
    binary2,
    M2,
    (w2, h2),
    flags=cv2.INTER_CUBIC,
    borderMode=cv2.BORDER_REPLICATE
)


# ============================================================
# DISPLAY IMAGE 1
# ============================================================

cv2.imshow("Image 1 - Original", image1)
cv2.imshow("Image 1 - Grayscale", gray1)
cv2.imshow("Image 1 - Binary", binary1)
cv2.imshow("Image 1 - Deskewed", deskewed1)

print("Image 1 detected angle:", angle1)


# ============================================================
# DISPLAY IMAGE 2
# ============================================================

cv2.imshow("Image 2 - Original", image2)
cv2.imshow("Image 2 - Grayscale", gray2)
cv2.imshow("Image 2 - Binary", binary2)
cv2.imshow("Image 2 - Deskewed", deskewed2)

print("Image 2 detected angle:", angle2)


# ============================================================
# WAIT AND CLOSE
# ============================================================
cv2.waitKey(0)
cv2.destroyAllWindows()

#using EasyOCR for deskewed images
import easyocr
reader = easyocr.Reader(['en'])

result1=reader.readtext(deskewed1)
result2=reader.readtext(deskewed2)

for detection in result1:

    # detection contains:
    # [bounding_box, detected_text, confidence]

    box = detection[0]
    text = detection[1]
    confidence = detection[2]

    print("Text:", text)
    print("Confidence:", confidence)
    print("Bounding Box:", box)
    print("-" * 50)
    
    
    
for detection in result2:

    # detection contains:
    # [bounding_box, detected_text, confidence]

    box = detection[0]
    text = detection[1]
    confidence = detection[2]

    print("Text:", text)
    print("Confidence:", confidence)
    print("Bounding Box:", box)
    print("-" * 50)
    
