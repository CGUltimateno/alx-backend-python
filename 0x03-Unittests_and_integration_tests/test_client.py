#!/usr/bin/env python3
"""
This module contains the tests for the client module.
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases.
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test GithubOrgClient.org.
        """
        gc = GithubOrgClient(org_name)
        gc.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url.
        """
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            org_name = "test"
            mock_public_repos_url.return_value = f"https://api.github.com/orgs/{org_name}/repos"
            gc = GithubOrgClient(org_name)
            self.assertEqual(gc._public_repos_url, f"https://api.github.com/orgs/{org_name}/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos.
        """
        payload = [{'name': 'google'}, {'name': 'abc'}]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            org_name = "test"
            mock_public_repos_url.return_value = f"https://api.github.com/orgs/{org_name}/repos"
            gc = GithubOrgClient(org_name)
            self.assertEqual(gc.public_repos(), ['google', 'abc'])
            mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}/repos")

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos with license.
        """
        payload = [{'name': 'google', 'license': {'key': 'my_license'}}, {'name': 'abc'}]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            org_name = "test"
            mock_public_repos_url.return_value = f"https://api.github.com/orgs/{org_name}/repos"
            gc = GithubOrgClient(org_name)
            self.assertEqual(gc.public_repos('my_license'), ['google'])
            mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}/repos")


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test cases.
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_public_repos(self, org_name):
        """
        Test GithubOrgClient.public_repos.
        """
        gc = GithubOrgClient(org_name)
        self.assertEqual(gc.public_repos(), ['google', 'abc'])

    @parameterized.expand([
        ("google", "my_license"),
        ("abc", "my_license")
    ])
    def test_public_repos_with_license(self, org_name, license):
        """
        Test GithubOrgClient.public_repos with license.
        """
        gc = GithubOrgClient(org_name)
        self.assertEqual(gc.public_repos(license), ['google'])
