from picamera import PiCamera
from loader import Loader
from time import sleep
import chalk
import cv2
import uuid

'''
Loads an image take from the Raspberry Pi's Camera
'''
class PiCamLoader(Loader.Loader):
	def __init__(self, config):
		super().__init__()
		self.config = config
		self.camera = PiCamera()

	def load(self):
		print(chalk.blue("[INFO] Loading Image from PiCam snapshot"))
		file = open(f'rpi-{str(uuid.uuid4())}.jpg', 'wb')
		self.camera.start_preview()
		sleep(2)
		self.camera.capture(file)
		image = cv2.imread(file)
		return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)