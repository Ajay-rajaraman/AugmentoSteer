import cv2
img = cv2.imread('C:\\Users\\ajayr\\OneDrive\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\extractRGBComponents.png')
#cv2.imshow('image',img)
red_channel = img[:,:,2]
cv2.imshow('red',red_channel) 


green_channel = img[:,:,1]
cv2.imshow('green',green_channel) 

blue_channel = img[:,:,0]
cv2.imshow('blue',blue_channel) 
cv2.waitKey(0)

cv2.destroyAllWindows()