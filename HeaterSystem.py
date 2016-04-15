class HeaterSystem():

	def __init__(self, config, nodes):
		self.config = config
		self.nodes = nodes

	def start(self):
		for node in self.nodes:
			node.send('on')

	def stop():
		raise "Method stop() not implemented"
