# -*- coding: utf-8 -*-
import unittest

from string_tools import test_json
from string_tools import init_base_json


class TestGeneratedJSON(unittest.TestCase):

    def test_generated_equals_pattern(self):
        self.assertEqual(test_json, init_base_json())


if __name__ == '__main__':
    unittest.main()
