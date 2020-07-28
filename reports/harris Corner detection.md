# Harris Corner Detection


## What do you mean by a Corner?
The corners of an image are basically identified as the regions in which there are variations in large intensity of the gradient in all possible dimensions and directions

## Mathematical representation of Harris Corner detection:
1) change in intensity is represented by:

![image](https://user-images.githubusercontent.com/66733698/88562246-0fd70e00-d04e-11ea-9d2a-b067ddf1c666.png)

where I(x+u,y+v) is shifted intensity and I(x,y) is original intensity
where the expansion is done using taylor's series expansion and is as follows:



2) In matrix form it can be written like this:

![image](https://user-images.githubusercontent.com/66733698/88562777-bf13e500-d04e-11ea-8e45-6de49d827e45.png)

this in turn can be written as 

![image](https://user-images.githubusercontent.com/66733698/88564854-609c3600-d051-11ea-98d3-5640b8e47d2b.png)

where M is:

![image](https://user-images.githubusercontent.com/66733698/88564942-83c6e580-d051-11ea-86c6-fd32c0e5d7f0.png)

W is windowing function

3) We can Find R using M :(R value tells whether it is a corner or edge)


![image](https://user-images.githubusercontent.com/66733698/88565071-bbce2880-d051-11ea-98a6-8bb22f68a2dd.png)

where K is imperically determined constant
Lambda1 and lambda2 are eign values 

### How to know if its Corner or not?
a) R value predicts if it is corner or edge
b) If it is a corner R value will be positive and large
c) If it is a edge R value will be negative 
d) modulus os R will be small in flat reigons