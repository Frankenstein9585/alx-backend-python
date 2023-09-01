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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Tests the public_repos() method"""
        payload = [
            {'id': 1, "name": "some_file1"},
            {'id': 2, "name": "some_file2"},
            {'id': 3, "name": "some_file3"}
        ]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = \
                "https://api.github.com/orgs/bcj/repos"
            repos_list = [repo['name'] for repo in payload]
            client = GithubOrgClient('bcj')
            self.assertEqual(client.public_repos(), repos_list)
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         key: str, result: bool) -> None:
        """Tests the has_license() method"""
        has_license = GithubOrgClient.has_license(repo, key)
        self.assertEqual(has_license, result)


if __name__ == "__main__":
    unittest.main()
