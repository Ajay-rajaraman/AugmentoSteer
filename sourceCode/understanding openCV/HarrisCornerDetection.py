import cv2
import numpy as np

img = cv2.imread('C:\\Users\\ajayr\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\chess.jfif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mY=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
mX=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
paddedArray = np.pad(gray, pad_width=1, mode='constant', constant_values=0)
finalImage=np.zeros((len((paddedArray)-4),len((paddedArray[0])-4)))
for i in range(len(paddedArray)-3):
    for j in range(len(paddedArray[0])-3):
        
        x=paddedArray[i:i+3,j:j+3]
        WindowX=np.multiply(x,mX)
        WindowY=np.multiply(x,mY)
        WindowXX=WindowX.dot(WindowX)
        sXX=np.sum(WindowXX)
        WindowYY=WindowY.dot(WindowY)
        sYY=np.sum(WindowYY)
        WindowXY=WindowX.dot(WindowY)
        sXY=np.sum(WindowXY)
        Det = (sXX*sYY)-(sXY**2)
        Trace = (sXX+sYY)
        k=0.04
        R = Det-(k*(Trace**2))
        if(R>0):
            finalImage[i,j]=R
        if(R<=0):
            finalImage[i,j]=0
cv2.imshow('final',finalImage)
cv2.imshow('original',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

