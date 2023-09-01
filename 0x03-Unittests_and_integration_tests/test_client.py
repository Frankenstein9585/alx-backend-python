#!/usr/bin/env python3
"""Test Suite for client.py"""
from typing import Mapping, Sequence, Any, Dict, Callable
from client import GithubOrgClient
from parameterized import parameterized

import unittest
from unittest.mock import Mock, patch, PropertyMock

from utils import access_nested_map, get_json, memoize


class TestGithubOrgClient(unittest.TestCase):
    """Tests that GithubOrgClient.org returns the right value"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """Tests the org() method"""
        github_org_client = GithubOrgClient(org)

        github_org_client.org()

        mock_get_json.assert_called_once_with(
            github_org_client.ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """Tests the public_repos_url() method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_client:
            mock_client.return_value = \
                {"repos_url": "https://api.github.com/orgs/abc/repos"}
            github_org_client = GithubOrgClient('abc')
            result = github_org_client.org['repos_url']
            self.assertEqual(result, "https://api.github.com/orgs/abc/repos")


if __name__ == "__main__":
    unittest.main()
