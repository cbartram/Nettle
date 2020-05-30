from loader import Loader

class S3Loader(Loader.Loader):
	def __init__(self):
		pass

	def load(self):
		print("Loading Image from S3")