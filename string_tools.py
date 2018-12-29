# -*- coding: utf-8 -*-
sensor_list = ['luminosity', 'vibration', 'gas', 'bridge', 'temperature', 'wetness', 'water', 'parking']

test_json = '[ ' \
            '{ "id" : 0, "name" : "luminosity", "data" : null },' \
            '{ "id" : 1, "name" : "vibration", "data" : null },' \
            '{ "id" : 2, "name" : "gas", "data" : null },' \
            '{ "id" : 3, "name" : "bridge", "data" : null },' \
            '{ "id" : 4, "name" : "temperature", "data" : null },' \
            '{ "id" : 5, "name" : "wetness", "data" : null },' \
            '{ "id" : 6, "name" : "water", "data" : null },' \
            '{ "id" : 7, "name" : "parking", "data" : null } ]'


def init_base_json():
    base = '[ '
    for i, j in enumerate(sensor_list):
        base = base + "{{ \"id\" : {id}, \"name\" : \"{name}\", \"data\" : null }},".format(id=i, name=j)

    base = base[:-1]
    base = base + ' ]'
    return base
