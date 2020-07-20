import cv2
import numpy as np

c=int(input("enter a number used for thresholding where\n 0 is for blue\n 1 is for green\n 2 is for red\n"))
img=cv2.imread('C:\\Users\\ajayr\\OneDrive\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\understandingThresholdingAndMasking[225].jpg')
color=np.zeros(np.shape(img[:,:,0]))
out=np.zeros(np.shape(img[:,:]))
for i in range(len(color)):
    for j in range(len(color[0])):
            if(img[i][j][c]>=250):
                color[i][j] = 1
            elif(img[i][j][c]<250):
                color[i][j]=0
out[:,:,0] = np.multiply(img[:,:,0],color)
out[:,:,1] = np.multiply(img[:,:,1],color)
out[:,:,2] = np.multiply(img[:,:,2],color)
cv2.imshow('masked',out)          
cv2.imshow('orginal',img)  
cv2.waitKey(0)

cv2.destroyAllWindows()
