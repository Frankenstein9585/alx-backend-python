#!/usr/bin/env python3
"""Test Suite for utils.py"""
from typing import Mapping, Sequence, Any, Dict

from parameterized import parameterized

import unittest
from unittest.mock import Mock, patch

from utils import access_nested_map, get_json, memoize


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
    @patch('utils.requests.get')
    def test_get_json(self, url: str, payload: Dict, mock_get) -> None:
        """TestCase for get_json method()"""
        mock_get.return_value.json.return_value = payload
        # mock_get.return_value.json.return_value = payload
        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """Tests the memoize() method"""

    def test_memoize(self):
        """TestCase for the memoize method"""

        class TestClass:
            """Test Class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as memoize_mock:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            memoize_mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
