import chalk
from loader.S3Loader import S3Loader
from loader.LocalLoader import LocalLoader
from loader.PiCamLoader import PiCamLoader

'''
Factory class which instantiates the correct
type of image loader depending on the configuration passed in
'''
class LoaderFactory:

	loadS3 = False
	loadLocal = False
	loadPi = False

	def __init__(self, config):
		self.config = config
		if config['DEFAULT']['LoadImage'] == 'True':
			print(chalk.blue(f'[INFO] Loading Image from: {config["DEFAULT"]["ImageSource"]}'))
			if config['DEFAULT']['ImageSource'].upper() == "S3":
				self.loadS3 = True
			else:
				self.loadLocal = True
		else:
			print(chalk.blue("[INFO] Using Raspberry Pi Camera module."))
			self.loadPi = True

	'''
	Creates a new image loader
	'''
	def createLoader(self):
		if self.loadS3:
			return S3Loader(self.config)
		elif self.loadLocal:
			return LocalLoader(self.config)
		else:
			return PiCamLoader(self.config)

