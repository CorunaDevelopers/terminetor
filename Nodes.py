# -*- coding: utf-8 -*-
class Node:
    def send(command):
        return False

class BTNode(Node):
    def send(self, command):
        # if (connected):
        # result = btmanager.send(command)
        print('connecting to BT node')
        return True

class LocalNode(Node):
	def send(self, command):
		print('connecting to local node')
		return True