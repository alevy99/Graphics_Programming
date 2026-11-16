import cv2
import matplotlib.pyplot as plt
import numpy

print ("fdsfdfsd")

imgOrig = cv2.imread('ATU.jpg',)

imgOrig = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2RGB)

# Convert to grayscale
imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)

# Display the image in a window
#cv2.imshow('ATU Grayscale Image', gray_image)

# Save the grayscale image
# cv2.imwrite('ATU_grayscale.jpg', gray_image)

# Wait for a key press before closing
#cv2.waitKey(0)
#cv2.destroyAllWindows()

nrows = 3
ncols = 4
plt.subplot(nrows, ncols,1),plt.imshow(imgOrig, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(imgGray, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])


imgOut3 = cv2.GaussianBlur(imgGray,(3, 3),0)
plt.subplot(nrows, ncols,3),plt.imshow(imgOut3, cmap = 'gray')
plt.title('Kernel 3x3'), plt.xticks([]), plt.yticks([])

imgOut5 = cv2.GaussianBlur(imgGray,(5, 5),0)
plt.subplot(nrows, ncols,4),plt.imshow(imgOut5, cmap = 'gray')
plt.title('Kernel 5x5'), plt.xticks([]), plt.yticks([])

imgOut9 = cv2.GaussianBlur(imgGray,(9, 9),0)
plt.subplot(nrows, ncols,5),plt.imshow(imgOut9, cmap = 'gray')
plt.title('Kernel 9x9'), plt.xticks([]), plt.yticks([])

imgOut13 = cv2.GaussianBlur(imgGray,(13, 13),0)
plt.subplot(nrows, ncols,6),plt.imshow(imgOut13, cmap = 'gray')
plt.title('Kernel 13x13'), plt.xticks([]), plt.yticks([])


imgForSobel = imgOut9

sobelHorizontal = cv2.Sobel(imgForSobel,cv2.CV_64F,1,0,ksize=5) # x dir
sobelVertical = cv2.Sobel(imgForSobel,cv2.CV_64F,0,1,ksize=5) # y dir

sobelTotal = sobelHorizontal + sobelVertical

plt.subplot(nrows, ncols,7),plt.imshow(sobelHorizontal, cmap = 'gray')
plt.title('Sobel horizontal'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,8),plt.imshow(sobelVertical, cmap = 'gray')
plt.title('Sobel vertical'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,9),plt.imshow(sobelTotal, cmap = 'gray')
plt.title('Sobel total'), plt.xticks([]), plt.yticks([])

sobelTotal = cv2.convertScaleAbs(sobelTotal)



canny100 = cv2.Canny(sobelTotal,100,200)


canny500 = cv2.Canny(sobelTotal,500,1000)


canny600 = cv2.Canny(sobelTotal,600,1200)

plt.subplot(nrows, ncols,10),plt.imshow(canny100, cmap = 'gray')
plt.title('canny 100'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,11),plt.imshow(canny500, cmap = 'gray')
plt.title('canny 500'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,12),plt.imshow(canny600, cmap = 'gray')
plt.title('canny 600'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
#cv2.destroyAllWindows()

