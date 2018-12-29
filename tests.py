# -*- coding: utf-8 -*-
import unittest

from string_tools import test_json
from string_tools import init_base_json

from serial.tools import list_ports


class TestGeneratedJSON(unittest.TestCase):

    def test_generated_equals_base(self):
        self.assertEqual(test_json, init_base_json())


class TestArduinoConnection(unittest.TestCase):

    def test_if_arduino_is_connected(self):
        ports = list(list_ports.comports())

        descriptions = [device.description for device in ports]
        manufacturers = [device.manufacturer for device in ports]

        self.assertTrue('Arduino' in descriptions or 'Arduino' in manufacturers or 'Microsoft' in manufacturers)


if __name__ == '__main__':
    unittest.main()
