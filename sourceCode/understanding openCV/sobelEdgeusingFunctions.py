import cv2 
import numpy as np

img = cv2.imread('C:\\Users\\ajayr\\OneDrive\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\pictures.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayArray=np.array(gray)
stepsize=int(input("enter the stepsize"))
kernelsize=int(input("enter the kernel size"))
paddedArray = np.pad(grayArray, pad_width=int(kernelsize/2), mode='constant', constant_values=0)


l=np.shape(grayArray[:,:])
finalimage=np.zeros((int(l[0]/stepsize),int(l[1]/stepsize)))
if(kernelsize==3):
    multipyArray=np.array([[0.111,0.111,0.111],[0.111,0.111,0.111],[0.111,0.111,0.111]])
elif(kernelsize==5):
    multipyArray=np.array([[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04]])
if(kernelsize==3):
    sobelArray=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    #sobelArray=np.array([[1,1,1],[1,1,1],[1,1,1]])
elif(kernelsize==5):
    #sobelArray=np.array([[2,1,0,-1,-2],[2,1,0,-1,-2],[4,2,0,-2,-4],[2,1,0,-1,-2],[2,1,0,-1,-2]])
    sobelArray=np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
for i in range(0,int((len(paddedArray)-kernelsize)/stepsize)):
    for j in range(0,int((len(paddedArray[0])-kernelsize)/stepsize)):
        
        x=paddedArray[i:i+kernelsize,j:j+kernelsize]
        y=np.multiply(x,sobelArray)
        z=np.multiply(y,multipyArray)
        a=np.sum(z)
       
        finalimage[i,j]=abs(a)
        
cv2.imwrite('output.jpg',finalimage)  
cv2.imshow('sobel',finalimage) 
cv2.waitKey(0)
cv2.destroyAllWindows()
