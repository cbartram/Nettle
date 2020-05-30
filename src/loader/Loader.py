from abc import ABC, abstractmethod

'''
Abstract Super class defining a single
method to load an image into memory
'''
class Loader(ABC):
	def __init__(self):
		# TODO Perhaps self.config could be set here instead of every constructor in the child classes
		pass

	'''
	Abstract method which is implemented by the child classes and loads the 
	image into memory
	'''
	def load(self):
		pass