from vidopt import ThreadedVideo
import cv2 as cv
import pytesseract
import time

# Establish a new threaded video object for webcam use.
# This should hopefully increase the FPS and decrease the latency of our camera!
video_feed = ThreadedVideo(name="Webcam Feed")
video_feed.start_thread()
# Let the camera boot
time.sleep(2)


while True:
	image = video_feed.read()
	(h, w) = image.shape[:2]
	
	# Code for recognizing here.
	
	cv.imshow("frame", image)
	if cv.waitKey(20) % 0xFF == ord("s"):
		break