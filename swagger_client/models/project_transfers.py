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

class ProjectTransfers(object):
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
        '_in': 'list[ProjectTransferIn]',
        'out': 'list[ProjectTransferOut]'
    }

    attribute_map = {
        '_in': 'in',
        'out': 'out'
    }

    def __init__(self, _in=None, out=None):  # noqa: E501
        """ProjectTransfers - a model defined in Swagger"""  # noqa: E501
        self.__in = None
        self._out = None
        self.discriminator = None
        if _in is not None:
            self._in = _in
        if out is not None:
            self.out = out

    @property
    def _in(self):
        """Gets the _in of this ProjectTransfers.  # noqa: E501

        A list of transfers that have caused funds to enter this project.  # noqa: E501

        :return: The _in of this ProjectTransfers.  # noqa: E501
        :rtype: list[ProjectTransferIn]
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this ProjectTransfers.

        A list of transfers that have caused funds to enter this project.  # noqa: E501

        :param _in: The _in of this ProjectTransfers.  # noqa: E501
        :type: list[ProjectTransferIn]
        """

        self.__in = _in

    @property
    def out(self):
        """Gets the out of this ProjectTransfers.  # noqa: E501

        A list of transfers that have caused funds to leave this project.  # noqa: E501

        :return: The out of this ProjectTransfers.  # noqa: E501
        :rtype: list[ProjectTransferOut]
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this ProjectTransfers.

        A list of transfers that have caused funds to leave this project.  # noqa: E501

        :param out: The out of this ProjectTransfers.  # noqa: E501
        :type: list[ProjectTransferOut]
        """

        self._out = out

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
        if issubclass(ProjectTransfers, dict):
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
        if not isinstance(other, ProjectTransfers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
