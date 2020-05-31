# from picamera import PiCamera
from loader import Loader
from time import sleep
from PIL import Image
import chalk
import uuid

'''
Loads an image take from the Raspberry Pi's Camera
'''
class PiCamLoader(Loader.Loader):
	def __init__(self, config):
		super().__init__()
		self.config = config
		# self.camera = PiCamera()

	def load(self):
		print(chalk.blue("[INFO] Loading Image from PiCam snapshot"))
		file = open(f'rpi-{str(uuid.uuid4())}.jpg', 'wb')
		self.camera.start_preview()
		sleep(2)
		self.camera.capture(file)
		image = Image.open(file)
		return image