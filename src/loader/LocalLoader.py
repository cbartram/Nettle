from loader import Loader
import cv2
import chalk

'''
Loads an image from a local filesystem path
'''
class LocalLoader(Loader.Loader):
	def __init__(self, config):
		super().__init__()
		self.config = config

	def load(self):
		print(chalk.blue(f'[INFO] Loading Image from Local Filesystem: {self.config["DEFAULT"]["ImagePath"]}'))
		image = cv2.imread(self.config["DEFAULT"]["ImagePath"])
		return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)