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

class OutboundsReleasesBody(object):
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
        'releases': 'list[ReleaseInput]'
    }

    attribute_map = {
        'releases': 'releases'
    }

    def __init__(self, releases=None):  # noqa: E501
        """OutboundsReleasesBody - a model defined in Swagger"""  # noqa: E501
        self._releases = None
        self.discriminator = None
        self.releases = releases

    @property
    def releases(self):
        """Gets the releases of this OutboundsReleasesBody.  # noqa: E501

        A list of releases to create.  # noqa: E501

        :return: The releases of this OutboundsReleasesBody.  # noqa: E501
        :rtype: list[ReleaseInput]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this OutboundsReleasesBody.

        A list of releases to create.  # noqa: E501

        :param releases: The releases of this OutboundsReleasesBody.  # noqa: E501
        :type: list[ReleaseInput]
        """
        if releases is None:
            raise ValueError("Invalid value for `releases`, must not be `None`")  # noqa: E501

        self._releases = releases

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
        if issubclass(OutboundsReleasesBody, dict):
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
        if not isinstance(other, OutboundsReleasesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
