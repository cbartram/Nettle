from abc import ABC, abstractmethod

'''
Abstract Super class defining a single
method to load an image into memory
'''
class Loader(ABC):
	def __init__(self):
		print("iNIT")

	def load(self):
		pass