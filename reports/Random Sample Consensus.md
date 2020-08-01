
# Random sample consensus

## What is an outlier?
Outliers are basically data points that do not resemble other data points.


![image](https://user-images.githubusercontent.com/66733698/89097093-5c796b00-d3f9-11ea-872c-f8d0b8826b6d.png)

In this image the black dots corresponds to inliers and the red dots to outliers. Similarly while dealing with data points there will be inliers and outliers , so our goal  is to reduce the outliers data points. 

# How do we reduce these outlier data points?
we can reduces by using this approach called random smaple Consensus.

# Random sample consensus
A)This is a trial and error and approach
B)This apprach is used when there is relatively high fraction of outliers
C)We split the data randomly into inliers and outliers ,we fit a model and check the accuracy . this process is repeated till the accuracy is high.


![image](https://user-images.githubusercontent.com/66733698/89105724-4f806a00-d441-11ea-9d0a-abce84cb8c3f.png)


# NUMBER OF TRIALS 

![image](https://user-images.githubusercontent.com/66733698/89105737-72128300-d441-11ea-8e86-c9a8dfb39cbd.png)