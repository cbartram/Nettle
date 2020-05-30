from loader import Loader
import chalk

'''
Loads an image take from the Raspberry Pi's Camera
'''
class PiCamLoader(Loader.Loader):
	def __init__(self, config):
		super().__init__()
		self.config = config

	def load(self):
		print(chalk.blue("[INFO] Loading Image from PiCam snapshot"))
		# TODO will be implemented later

