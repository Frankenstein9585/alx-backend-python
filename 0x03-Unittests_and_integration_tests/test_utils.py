#!usr/bin/env python3
"""Test Suite for utils.py"""
from typing import Mapping, Sequence, Any

from parameterized import parameterized

from utils import access_nested_map

import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping, path: Sequence, result: Any):
        """Test Access Nested Map"""
        self.assertEqual(access_nested_map(nested_map, path), result)
