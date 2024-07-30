from threading import Thread
import cv2 as cv

class ThreadedVideo:
	stopping = False
	name = ""
	
	def __init__(self, camera=0, name="video_stream"):
		# This will mostly just be used for the thread name
		self.name = name
		# Camera could change depending on what I'm using 
		self.video = cv.VideoCapture(camera)
		
	def start_thread(self):
		new_thread = Thread(name=self.name, target=self.next_frame, daemon=True)
		new_thread.start()
		return self
		
	def next_frame(self):
		# This function is started when the thread is created
		while True:
			_, self.frame = self.video.read()
	
	def read(self):
		return (self.frame)