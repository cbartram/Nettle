import json
import requests

'''
Hue controller for interacting with Philips hue lights
'''
class Hue:
	def __init__(self, config):
		self.lights = None
		self.config = config
		self.bridge_user = self.config['HUE']['BridgeUser']
		self.bridge_ip = self.config['HUE']['BridgeIp']

	'''
	 Fetches all the lights available on the network
	'''
	def get_lights(self):
		response = requests.get(f'http://{self.bridge_ip}/api/{self.bridge_user}/lights')
		self.lights = response.json()
		return self.lights

	'''
	Retrieves a single lights by its sequential id (1,2,3 etc)
	:param id String id of the light to retrieve
	'''
	def get_light(self, id):
		if self.lights == None:
			self.get_lights()

		if self.lights[id] == None:
			raise Exception("There is no light with the id: " + id)

		return self.lights[id]

	'''
	 Toggles an individual light on or off
	'''
	def toggle_light(self, id, on = True):
		if self.lights[id] == None:
			raise Exception("There is no light with the id: " + id)

		payload = json.dumps({ "on": on })
		response = requests.put(f'http://{self.bridge_ip}/api/{self.bridge_user}/lights/{id}/state', data=payload)
		return response.json()


	'''
	 Sets a light with the given id to a specific color.
	 The color should be a tuple in the order: hue, sat, brightness
	'''
	def set_color(self, id, color):
		if self.lights[id] == None:
			raise Exception("There is no light with the id: " + id)

		payload = json.dumps({ "on": True, "sat": color[1], "bri": color[2], "hue": color[0] })
		response = requests.put(f'http://{self.bridge_ip}/api/{self.bridge_user}/lights/{id}/state', data=payload)
		return response.json()
