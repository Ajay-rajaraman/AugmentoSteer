import cv2

def convertImageToGray(c):
    gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return







img = cv2.imread('C:\\Users\\ajayr\\OneDrive\\Documents\\MyProjects\\AugmentoSteer\\testImages\\understanding opencv\\extractRGBComponents.png')
convertImageToGray(img)






