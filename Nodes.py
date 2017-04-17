# -*- coding: utf-8 -*-
from Executor import LocalExecutor
import serial

class Node:
    def send(self, command, *args):
        return False

class BTNode(Node):
    def __init__(self, port):
        self.port = port
        self.s = serial.Serial(port=port, baudrate=9600)

    def send(self, command, *args):
        self.s.write(command)
        print self.s.readline()
        # if (connected):
        # result = btmanager.send(command)
        return True

class LocalNode(Node):
    def __init__(self):
        self.executor = LocalExecutor()

    def send(self, command, *args):
        return self.executor.execute(command, args)

node = BTNode('/dev/tty.HC-06-DevB')
node.send('on')
