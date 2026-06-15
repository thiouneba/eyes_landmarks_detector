# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import time
import dlib
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to image")
args = vars(ap.parse_args())

print("[INFO] loading predictors...")
predictor = dlib.shape_predictor(args["shape_predictor"])

#frame = cv2.imread("PDA/PDA001-IRM_025492.png")
frame = cv2.imread(args["image"])
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

print("Frame shape")
print(frame.shape)
#rect = np.array([0,0, frame.shape[0], frame.shape[1]])

rect = dlib.rectangle(left=0, top=0, right=frame.shape[1], bottom=frame.shape[0])

shape = predictor(gray, rect)


print("SHAPE: ")
print(shape)



shape = face_utils.shape_to_np(shape)
for (sX, sY) in shape:
	cv2.circle(frame, (sX, sY), 3, (0, 0, 255), -1)
cv2.imshow("Frame", frame)
while True:
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
