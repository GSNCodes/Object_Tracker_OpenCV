

# import the necessary packages
from collections import deque
import numpy as np
import cv2



# define the lower and upper boundaries of the color of the object to be tracked.

color_in_bgr = np.uint8([[[255,0,0]]]) #here insert the bgr values which you want to convert to hsv
color_in_hsv = cv2.cvtColor(color_in_bgr, cv2.COLOR_BGR2HSV)
print(color_in_hsv)

color_lower = (int(color_in_hsv[0][0][0]-10),50,50)
color_upper = (int(color_in_hsv[0][0][0]+10),255,255)


pts = deque(maxlen=64)

cap = cv2.VideoCapture(0)

while True:
    # Get the current frame
    ret, frame = cap.read()

    if frame is None:
        break

    # frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # kernel = np.ones((5, 5), np.uint8)

    mask = cv2.inRange(hsv, color_lower, color_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, None)
    mask = cv2.dilate(mask, None, iterations=2)


    cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2:]

    center = None


    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Specify the minimum size
        if radius > 5:
            #draw the circle
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    pts.appendleft(center)

    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue

        thickness = int(np.sqrt(len(pts)/ float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    # Display the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Stop if 'q' key is pressed
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()