from loader import Loader
from PIL import Image
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
		image = Image.open(self.config["DEFAULT"]["ImagePath"])
		return image