# coding: utf-8

"""
    trustshare API

    Welcome to the trustshare API Reference documentation. Here you can find detailed information about the endpoints we provide as well as the shape of entities within the system.  # Environments The trustshare API has two environments, __Sandbox__ and __Live__. Both environments are available under the same endpoint however API Keys and client secrets are prefixed with the environment name. - A __Sandbox__ API Key will be in the format: `sandbox_api_[0-9a-z]`. - A __Live__ API Key will be in the format: `live_api_[0-9a-z]`.  ## Sandbox Our __Sandbox__ environment endeavours to be as close to the __Live__ environment as possible, however, there are a couple of limitations and features which should be noted. - Card payments take around 7 days to settle into accounts. In __Live__ this is generally closer to 2 days. - Manual inbound payments can only be \"faked\" in __Sandbox__ when they are less-than or equal-to `250,000.00`. - Open Banking in __Sandbox__ will always use a \"Mock Bank\" UI to accept the payment.  # noqa: E501

    OpenAPI spec version: 1.0.23
    Contact: support@trustshare.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.transfers_api import TransfersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTransfersApi(unittest.TestCase):
    """TransfersApi unit test stubs"""

    def setUp(self):
        self.api = TransfersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_transfers(self):
        """Test case for create_transfers

        Create Transfers  # noqa: E501
        """
        pass

    def test_get_transfer(self):
        """Test case for get_transfer

        Get a Transfer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
