import cv2


def extractLayer(c):
    channel = img[:,:,c]
    if(c==0):
        cv2.imshow('blue',channel)
    elif(c==1):
        cv2.imshow('green',channel)
    elif(c==2):
        cv2.imshow('red',channel)
 
    cv2.waitKey(0)

    cv2.destroyAllWindows() 
    return








img = cv2.imread('C:\\Users\\ajayr\\OneDrive\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\extractRGBComponents.png')
x=int(input("enter the number"))
extractLayer(x)





