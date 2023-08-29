#!/usr/bin/env python3
"""Test Suite for utils.py"""
from typing import Mapping, Sequence, Any

from parameterized import parameterized

import unittest
from unittest.mock import Mock, patch

from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """Tests the get_json method()"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """TestCase for get_json method()"""
        with patch('utils.requests.get') as mock_get:
            # mock_response = Mock()
            # mock_response.json.return_value = payload
            mock_get.return_value.json.return_value = payload
            mock_get.assert_called_once_with(url)
            self.assertEqual(get_json(url), payload)


if __name__ == "__main__":
    unittest.main()
