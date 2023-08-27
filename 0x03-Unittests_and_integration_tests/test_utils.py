#!/usr/bin/env python3
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
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
        """TestCase for access_nested_map() method"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """TestCase for access_nested_map() method"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
