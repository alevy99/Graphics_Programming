import cv2
import matplotlib.pyplot as plt
import numpy

print ("fdsfdfsd")

image = cv2.imread('ATU.jpg',)

if image is None:
    print("Error: Image not found. Check the file path.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the image in a window
    # cv2.imshow('ATU Grayscale Image', gray_image)
    
    nrows = 1
    ncols = 2
    plt.subplot(nrows, ncols,1),plt.imshow(imgOrig, cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(nrows, ncols,2),plt.imshow(imgGray, cmap = 'gray')
    plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

    # Save the grayscale image
    #cv2.imwrite('ATU_grayscale.jpg', gray_image)

    # Wait for a key press before closing
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Grayscale image saved successfully!")

