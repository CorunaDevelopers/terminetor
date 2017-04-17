class DisplaySystem():

	def __init__(self, config, nodes):
		self.config = config
		self.nodes = nodes

	def update_temp(temp):
		for node in self.nodes:
			node.send('show_temp', temp)

