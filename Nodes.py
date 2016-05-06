# -*- coding: utf-8 -*-
from Executor import LocalExecutor

class Node:
    def send(self, command):
        return False

class BTNode(Node):
    def send(self, command):
        # if (connected):
        # result = btmanager.send(command)
        print('connecting to BT node')
        return True

class LocalNode(Node):
    def __init__(self):
        self.executor = LocalExecutor()

    def send(self, command):
        return self.executor.execute(command)
