# CANNY EDGE DETECTION:


![image](https://user-images.githubusercontent.com/66733698/88287375-d336aa00-cd0f-11ea-96d0-16d6c8016698.png)


canny edge detection algorithm is proved to be one of the best edge detection algorithm that provides good and reliable detection.
## Process of Canny edge detection algorithm

### The Process of Canny edge detection algorithm can be broken down to 5 different steps:
1)apply gaussian filter(used for smoothening the image and noise
2)find the intensity gradients of the image
3)apply non-maximum suppression(to get edge detection)
4)apply double threshold to determine potential edges
5)track edge by hysteresis

# PREWITT EDGE DETECTION:
# Vertical Direction:
![image](https://user-images.githubusercontent.com/66733698/88299909-84ddd700-cd20-11ea-8968-6f9742f05894.png)


Above mask will find the edges in vertical direction and it is because the zeros column in the vertical direction. When you will convolve this mask on an image, it will give you the vertical edges in an image.


# Horizontal Direction:
![image](https://user-images.githubusercontent.com/66733698/88300181-d2f2da80-cd20-11ea-9c6e-fae617568af8.png)

Above mask will find edges in horizontal direction and it is because that zeros column is in horizontal direction. When you will convolve this mask onto an image it would prominent horizontal edges in the image.

