'''
What is color quantization?

👉 Reducing the number of colors in an image
while keeping it visually similar.

Example:
Original image → ~16 million colors
After quantization → K colors (e.g., 8, 16, 32)
This is used for:
Image compression , Style effects , Faster image processing , computer vision preprocessing

'''

'''
1.Treat every pixel's color as a data point and cluster similar colors together.
Each cluster becomes one final color.

2.Step 1: Pixels → points in color space

An image pixel has color:(R, G, B)
So the image becomes a dataset like:
[255, 0, 0]   # red
[254, 2, 1]   # almost red
[0, 255, 0]   # green
[0, 0, 255]   # blue

3.Step 2: Choose K (number of colors)
You decide: K = 5   → image will have only 5 colors

4.Step 3: Initialize K centroids
KMeans places K random colors in RGB space:
C1 = [120, 30, 200]
C2 = [250, 10, 10]
C3 = [20, 240, 50]

5.Step 4: Assign each pixel to nearest centroid

For each pixel:
Compute distance to all centroids
Assign it to the closest color

6.Step 5: Update centroids (average color)

For each cluster:
Take all assigned pixels
Compute their mean color

7.Step 6: Repeat until convergence

Steps 4 & 5 repeat until: Centroids stop changing , Or max_iter is reached

This minimizes inertia (color error).

8.Step 7: Replace pixels with centroid colors

Final step:
Every pixel → replaced by its cluster centroid

'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.image as mpimg 

#creating array of image , 'imread()' helps us read the image in array format 
image=mpimg.imread("C:\\Users\\soham\\Downloads\\DATA\\palm_trees.jpg")
print(image)
print(image.shape)
plt.figure(dpi=200)
plt.imshow(image)# 'imshow()' helps us see the image . the image is not always at the highest no of pixels 

#now we have to convert the array into 2D : (H,W,C)-->(H*W,C)
#storing the information in a tuple - 
(h,w,c)=image.shape
print(h) 
print(w)
print(c)
#reshaping 
image2d=image.reshape(h*w,c)
print(image2d.shape)

#making the model 
from sklearn.cluster import KMeans
model=KMeans(n_clusters=100)
labels = model.fit_predict(image2d)
print(labels)
print(model.cluster_centers_)#these are the 6 centers of our clusters
rgbcodes=model.cluster_centers_.round(0).astype(int)
print(rgbcodes)
quantized_image = np.reshape(rgbcodes[labels], (h, w, c))
#rgbcodes[labels] : This is advanced NumPy indexing.
#“For each pixel, replace its label with the RGB color of its cluster centroid.”
#“This line replaces each pixel with its cluster’s centroid color and reshapes the result back into the original image format.”
plt.figure()
plt.imshow(quantized_image)
plt.show()
'''
“Color quantization reduces the number of unique colors, not the image dimensions.
File size reduces only after saving the image using compression formats like PNG or JPEG.”
'''