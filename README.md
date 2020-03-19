# Object_Tracker_OpenCV
An object tracking algorithm using OpenCV.


## Overview of Working
This is an object tracking algorithm which uses the color of the object to continuously keep a tab on it.

The code is pretty simple. We get the video from our webcam (with slight modifications we can also make it compatible with video files)
frame by frame and analyze the image for an object of our specified color. We apply some masks to obtain a somewhat accurate picture with
less noise. We then find the contours of the object and plot it too(You can see a small circle around the object).

The tracked points are stored in a queue which we update regularly. These points help us in drawing a line as the object moves.
The red line you see is the trail of the path that the object has left behind.


### Libraries Used
* cv2
* collections
* numpy

### Output
<img src="https://github.com/GSNCodes/Object_Tracker_OpenCV/edit/master/output.gif">


If you have any queries, let me know !

### Happy Learning People ! Keep chasing your dreams ! :star:
