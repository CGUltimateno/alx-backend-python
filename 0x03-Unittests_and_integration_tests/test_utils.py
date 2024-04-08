#!/usr/bin/env python3
"""
This module contains the tests for the utils module.
"""
import unittest
from unittest.mock import patch, Mock

import parameterized
from utils import get_random_number, get_random_number_v2, get_random_number_v3


class TestAccessNestedMap (unittest.TestCase):
    """
    Test cases.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, keys, expected):
        """
        Test access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, keys), expected)

        @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ])
        def test_access_nested_map_exception(self, nested_map, nested_key):
            """Test KeyError"""
            with self.assertRaises(KeyError):
                access_nested_map(nested_map, nested_key)


class TestGetJson(unittest.TestCase):
    """
    Test cases.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, mock_get):
        """
        Test get_json function.
        """
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = payload

        self.assertEqual(get_json(url), payload)
