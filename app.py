# -*- coding: utf-8 -*-
import json

from flask import Flask
from flask import abort
from flask import jsonify

import serial
import serial.tools.list_ports

from string_tools import init_base_json

app = Flask(__name__)
# 1 - open
# 0 - closed
bridge_state = False


def get_data_from_port():
    sensor_data = None
    try:
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if 'Arduino' in port.description or 'Arduino' in port.manufacturer or 'Microsoft' in port.manufacturer:
                port = serial.Serial(port.device, 9600)
                raw_data = port.readline()

                if raw_data is not None:
                    sensor_data = json.loads(raw_data[:-2])

                port.close()
    except Exception as e:
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(str(e.args))
            file.write('\n')
    return sensor_data if sensor_data is not None else base_json


def send_data_to_port(data, sensor):
    pass


@app.route('/get/list', methods=['GET'])
def get_sensor_list():
    # get_data_from_port()
    return get_data_from_port()


@app.route('/get/<int:_id>', methods=['GET'])
def get_sensor_by_id(_id):
    try:
        return get_data_from_port()[int(_id)]
    except (TypeError, IndexError):
        return abort(404)


@app.route('/bridge/open', methods=['GET'])
def open_bridge():
    if bridge_state:
        return
    else:
        pass


@app.route('/bridge/close', methods=['GET'])
def close_bridge():
    pass


if __name__ == '__main__':
    base_json = init_base_json()
    app.run()
