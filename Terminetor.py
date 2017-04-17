from HeaterSystem import HeaterSystem
from Nodes import LocalNode
from Nodes import BTNode

from flask import Flask
app = Flask(__name__)
heaterSystem = HeaterSystem('config', [LocalNode(), BTNode()])
displaySystem = DisplaySystem('config', [LocalNode()])

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/start')
def start():
    heaterSystem.start()
    return 'OK'

@app.route('/refresh')
def refresh():
    temp = heaterSystem.read_temp()
    displaySystem.update_temp(temp)

    return 'OK'    

if __name__ == '__main__':
    app.run(debug = True)
