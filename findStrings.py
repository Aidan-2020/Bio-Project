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
tesseract_path = "tesseract/tesseract.exe"

while True:
	# Get the image from the webcam to analyze
	image = video_feed.read()
	(h, w) = image.shape[:2]
	pytesseract.pytesseract.tesseract_cmd = tesseract_path
	
	# Code for recognizing here.
	if cv.waitKey(20) % 0xFF == ord("p"):
		gray_conversion = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
		
		#_, threshold = cv.threshold(gray_conversion, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)

		cv.imshow("caught", gray_conversion)
		print(pytesseract.image_to_string(gray_conversion))
	
	cv.imshow("frame", image)
	if cv.waitKey(20) % 0xFF == ord("s"):
		break