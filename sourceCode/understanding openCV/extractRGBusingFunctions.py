import cv2


def extractLayer(b,c,d):
    channel = b[:,:,c]
    cv2.imshow(d[c] ,channel)
    
 
    cv2.waitKey(0)

    cv2.destroyAllWindows() 
    return








img = cv2.imread('C:\\Users\\ajayr\\OneDrive\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\extractRGBComponents.png')
x=int(input("enter the number"))
t={0:'blue',1:'green',2:'red'}
extractLayer(img,x,t)





