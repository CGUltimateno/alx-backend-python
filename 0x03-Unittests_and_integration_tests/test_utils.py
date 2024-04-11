#!/usr/bin/env python3
"""
This module contains the tests for the utils module.
"""
import unittest
from unittest.mock import patch, Mock

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, keys, expected):
        """ Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, keys), expected)

        @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b",)),
        ])
        def test_access_nested_map_exception(self, nested_map, nested_key):
            """Test KeyError"""
            with self.assertRaises(KeyError):
                self.assertEqual(access_nested_map(nested_map, nested_key), expected)


class TestGetJson(unittest.TestCase):
    """Test Cases"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload,):
        """
        Test get_json function.
        """
        mock = Mock()
        mock.json.return_value = payload

        with patch("requests.get", return_value=mock) as magic_mock:
            response = get_json(url)
            magic_mock.assert_called_once_with(url)
            self.assertEqual(response, payload)
