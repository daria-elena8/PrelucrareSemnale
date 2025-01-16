import cv2
import matplotlib.pyplot as plt
#matplotlib inline
# Read the original image
img = cv2.imread('nature.jpg')
# converting because opencv uses BGR as default
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)

# converting to gray scale
gray = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)
# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)
# convolute with sobel kernels
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
#Plotting images
plt.imshow(sobelx)
plt.title("Sobel-x edge detection")
plt.imshow(sobely)
plt.title("Sobel-y edge detection")