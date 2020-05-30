from loader import Loader

class LocalLoader(Loader.Loader):
	def __init__(self):
		pass

	def load(self):
		print("Loading Image from Local Filesystem")