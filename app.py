# -*- coding: utf-8 -*-
import json

from flask import Flask
from flask import Response
from flask import jsonify

import serial
import serial.tools.list_ports

# from string_tools import sensor_list
from string_tools import init_base_json

app = Flask(__name__)

open_bridge = False


@app.route('/get/list', methods=['GET'])
def get_data_from_port():
    sensor_data = json.loads(base_json)
    try:
        ports = list(serial.tools.list_ports.comports())
        for item in ports:
            if 'Arduino' in item.description or 'Arduino' in item.manufacturer:
                port = serial.Serial(item.device, 9600)
                raw_string = port.readline()
                print(raw_string)

                # json["object"]["index"]["field"]

                if raw_string is not None:
                    raw_data = str(raw_string)

                    sensor_data = json.loads(raw_data)

                    '''
                    data_index = raw_data.find('Lum')
                    if data_index > 0:
                        sensor_data['sensors'][index]['data'] = raw_data[data_index + 4:data_index + 7:1]

                    index += 1

                    data_index = raw_data.find('Vib')
                    if data_index > 0:
                        sensor_data['sensors'][index]['data'] = int(raw_data[data_index + 4:data_index + 5:1])

                    index += 1

                    data_index = raw_data.find('Gas')
                    if data_index > 0:
                        sensor_data['sensors'][index]['data'] = int(raw_data[data_index + 4:data_index + 7:1])

                    index += 1

                    # up - 3, down - 4
                    if open_bridge is True:
                        port.write(b't')
                        sensor_data['sensors'][index]['data'] = 'true'
                    if open_bridge is False:
                        port.write(b'f')
                        sensor_data['sensors'][index]['data'] = 'false'

                    index += 1

                    data_index = raw_data.find('Tmr')
                    if data_index > 0:
                        sensor_data['sensors'][index]['data'] = int(raw_data[data_index + 3:data_index + 6:1])

                    index += 1

                    data_index = raw_data.find('Wet')
                    if data_index > 0:
                        sensor_data['sensors'][index]['data'] = int(raw_data[data_index + 4:data_index + 7:1])

                    index += 1

                    data_index = raw_data.find('Wat')
                    if data_index > 0:
                        sensor_data['sensors'][index]['data'] = int(raw_data[data_index + 4:data_index + 7:1])

                    index += 1

                    data_index = raw_data.find('Prk')
                    if data_index > 0:
                        sensor_data['sensors'][index]['data'] = int(raw_data[data_index + 4:data_index + 5:1])
                    '''

                    port.close()
    except Exception as e:
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(str(e.args))
            file.write('\n')
            return Response(505)
    return jsonify(sensor_data)


base_json = init_base_json()
app.run(host='0.0.0.0', port=80, threaded=True)
