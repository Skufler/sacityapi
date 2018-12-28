# -*- coding: utf-8 -*-
sensor_list = ['Lum', 'Vib', 'Gas', 'Brg', 'Tmr', 'Wet', 'Wat', 'Prk']

test_json = '[ ' \
            '{ "name" : "Lum", "data" : null },' \
            '{ "name" : "Vib", "data" : null },' \
            '{ "name" : "Gas", "data" : null },' \
            '{ "name" : "Brg", "data" : null },' \
            '{ "name" : "Tmr", "data" : null },' \
            '{ "name" : "Wet", "data" : null },' \
            '{ "name" : "Wat", "data" : null },' \
            '{ "name" : "Prk", "data" : null } ]'


def serialize_json(string):
    return str(string).strip("'<>() ").replace('\'', '\"')


def init_base_json():
    base = '[ '
    for i in sensor_list:
        base = base + "{{ \"name\" : \"{_name}\", \"data\" : 11 }},".format(_name=i,)

    base = base[:-1]
    base = base + ' ]'
    return base
