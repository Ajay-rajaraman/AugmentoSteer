# AUGMENTED STEERING THROUGH COMPUTER VISION
Steering an in game character using real world objects
## PROBLEM STATEMENTS
The user guides a game character(block) by using a paper with a red arrow printed on it as a steering wheel. The game and the computer vision algorithm required to capture and steer the block are to be developed in-house using only open source libraries and tools such as OpenCV.
## PROJECT REQUIRMENTS
1. Intermediate knowledge of Python for algorithm development.
2. Basic knowledge of classical computer vision algorithms for extraction of the arrow from an input source such as a webcam. (Can be learnt)
3. Advanced knowledge in Mathematics to extract the direction of the arrow from the image and the direction in which the arrow has been turned in the respective frames
4. Basic knowledge of Threading in python applications (Can be learnt) to run the game and the computer vision algorithm together
5. Basic knowledge of version control software, such as Git, to manage the project. (Can be learnt)
## THE GAME:
The game comprises of 3 major components:
- The background
-  The obstacles
-  The player (Block)
The objective of the game is simple. Guide the player (The block) through a road with three lanes in which there are obstacles on at least one lane of the road. The player turns the steering wheel to move the block in the right direction to avoid collision. The player remains static and can just shift between the lanes, while the obstacles move towards the player to give the illusion of movement on a road. The obstacles move at a speed that can be altered (should be a function variable to the program that generates the frame) to give the illusion of speeding up of the player over time. If the player collides with an obstacle, the game ends and the time in seconds is stored as the score.


![gameExplanation-01 223](https://user-images.githubusercontent.com/66733698/87847883-df2e0080-c8f8-11ea-9a40-a54482de3c90.png)
## THE VISION ALGORITHM:
As mentioned earlier, the steering of the block is done using a camera input (probably a webcam) in which the user rotates a printed arrow to steer the block in a direction. The angle at which the arrow is rotated is calculated between two consecutive frames sampled at a lower sampling rate than the traditional camera interface initially (to reduce computational cost and provide synchronization with the movement in the game). If the difference in the angle is larger than 50 degrees, the user is pushed to the corner lanes in the direction that the steering sheet is turned. If the difference in the angle is greater than 10 degrees, but less than 50 degrees, the block is pushed one lane in the direction that it is steered.


![gameExplanation-02 222](https://user-images.githubusercontent.com/66733698/87847890-fff65600-c8f8-11ea-88eb-bb335206bd84.png)

## TIMELINE
![duration](https://user-images.githubusercontent.com/66733698/87852400-4c548c80-c91f-11ea-8710-3565a0f40928.jpg)
