# coding: utf-8

"""
    trustshare API

    Welcome to the trustshare API Reference documentation. Here you can find detailed information about the endpoints we provide as well as the shape of entities within the system.  # Environments The trustshare API has two environments, __Sandbox__ and __Live__. Both environments are available under the same endpoint however API Keys and client secrets are prefixed with the environment name. - A __Sandbox__ API Key will be in the format: `sandbox_api_[0-9a-z]`. - A __Live__ API Key will be in the format: `live_api_[0-9a-z]`.  ## Sandbox Our __Sandbox__ environment endeavours to be as close to the __Live__ environment as possible, however, there are a couple of limitations and features which should be noted. - Card payments take around 7 days to settle into accounts. In __Live__ this is generally closer to 2 days. - Manual inbound payments can only be \"faked\" in __Sandbox__ when they are less-than or equal-to `250,000.00`. - Open Banking in __Sandbox__ will always use a \"Mock Bank\" UI to accept the payment.  # noqa: E501

    OpenAPI spec version: 1.0.23
    Contact: support@trustshare.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CollectionAccount(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'iban': 'str',
        'account_number': 'str',
        'routing_data': 'list[ProjectRoutingData]',
        'reference': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'iban': 'iban',
        'account_number': 'account_number',
        'routing_data': 'routing_data',
        'reference': 'reference',
        'metadata': 'metadata'
    }

    def __init__(self, iban=None, account_number=None, routing_data=None, reference=None, metadata=None):  # noqa: E501
        """CollectionAccount - a model defined in Swagger"""  # noqa: E501
        self._iban = None
        self._account_number = None
        self._routing_data = None
        self._reference = None
        self._metadata = None
        self.discriminator = None
        if iban is not None:
            self.iban = iban
        if account_number is not None:
            self.account_number = account_number
        if routing_data is not None:
            self.routing_data = routing_data
        if reference is not None:
            self.reference = reference
        if metadata is not None:
            self.metadata = metadata

    @property
    def iban(self):
        """Gets the iban of this CollectionAccount.  # noqa: E501

        The IBAN of the collection account.  # noqa: E501

        :return: The iban of this CollectionAccount.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this CollectionAccount.

        The IBAN of the collection account.  # noqa: E501

        :param iban: The iban of this CollectionAccount.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def account_number(self):
        """Gets the account_number of this CollectionAccount.  # noqa: E501

        The account number of the collection account. For EUR accounts, this will be `null`.  # noqa: E501

        :return: The account_number of this CollectionAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CollectionAccount.

        The account number of the collection account. For EUR accounts, this will be `null`.  # noqa: E501

        :param account_number: The account_number of this CollectionAccount.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def routing_data(self):
        """Gets the routing_data of this CollectionAccount.  # noqa: E501

        Object array containing account routing information required to make payments to the collection account. The below list describes the types of `routing_data` you can receive for each collection currency.  - `usd` - the type can be `ach`, `wire`, or `bic_swift` - `eur` - the type will be `bic_swift` - `gbp` - the type can be `sort_code`, or `bic_swift`  # noqa: E501

        :return: The routing_data of this CollectionAccount.  # noqa: E501
        :rtype: list[ProjectRoutingData]
        """
        return self._routing_data

    @routing_data.setter
    def routing_data(self, routing_data):
        """Sets the routing_data of this CollectionAccount.

        Object array containing account routing information required to make payments to the collection account. The below list describes the types of `routing_data` you can receive for each collection currency.  - `usd` - the type can be `ach`, `wire`, or `bic_swift` - `eur` - the type will be `bic_swift` - `gbp` - the type can be `sort_code`, or `bic_swift`  # noqa: E501

        :param routing_data: The routing_data of this CollectionAccount.  # noqa: E501
        :type: list[ProjectRoutingData]
        """

        self._routing_data = routing_data

    @property
    def reference(self):
        """Gets the reference of this CollectionAccount.  # noqa: E501

        The payment reference __must__ be used if defined, otherwise the payment might not be reconciled correctly.  # noqa: E501

        :return: The reference of this CollectionAccount.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this CollectionAccount.

        The payment reference __must__ be used if defined, otherwise the payment might not be reconciled correctly.  # noqa: E501

        :param reference: The reference of this CollectionAccount.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def metadata(self):
        """Gets the metadata of this CollectionAccount.  # noqa: E501

        Collection account metadata associated with sending payments, such as bank name and address.  # noqa: E501

        :return: The metadata of this CollectionAccount.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CollectionAccount.

        Collection account metadata associated with sending payments, such as bank name and address.  # noqa: E501

        :param metadata: The metadata of this CollectionAccount.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CollectionAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CollectionAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
