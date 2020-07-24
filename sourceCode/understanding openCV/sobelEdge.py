import cv2
import numpy as np


img = cv2.imread('C:\\Users\\ajayr\\OneDrive\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\picture.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayArray=np.array(gray)
paddedArray = np.pad(grayArray, pad_width=1, mode='constant', constant_values=0)
multipyArray=np.array([[0.111,0.111,0.111],[0.111,0.111,0.111],[0.111,0.111,0.111]])
##
finalimage=np.zeros(np.shape(gray[:,:]))
##
sobelArray=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
for i in range(len(paddedArray)-3):
    for j in range(len(paddedArray[0])-3):
        ##
        x=paddedArray[i:i+3,j:j+3]
        y=np.multiply(x,sobelArray)
        z=np.multiply(y,multipyArray)
        a=np.sum(z)
        #if(a>=0):
            #finalimage.append(a)
            #np.append(finalimage,a)
        finalimage[i,j]=abs(a)
        #elif(a<0):
            #finalimage.append(0)
            #np.append(finalimage,a)
            #finalimage[i,j]=0
#print(finalimage)
        
cv2.imshow('sobel',finalimage) 
cv2.imshow('gray',gray) 
cv2.imshow('orginal',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()





