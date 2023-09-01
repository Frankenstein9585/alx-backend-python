#!/usr/bin/env python3
"""Test Suite for client.py"""
from typing import Mapping, Sequence, Any, Dict, Callable
from client import GithubOrgClient
from parameterized import parameterized

import unittest
from unittest.mock import Mock, patch

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


if __name__ == "__main__":
    unittest.main()
