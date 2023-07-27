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

class Confirmation(object):
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
        'checkout_id': 'str',
        'project_id': 'str',
        'invoice_id': 'str'
    }

    attribute_map = {
        'checkout_id': 'checkout_id',
        'project_id': 'project_id',
        'invoice_id': 'invoice_id'
    }

    def __init__(self, checkout_id=None, project_id=None, invoice_id=None):  # noqa: E501
        """Confirmation - a model defined in Swagger"""  # noqa: E501
        self._checkout_id = None
        self._project_id = None
        self._invoice_id = None
        self.discriminator = None
        if checkout_id is not None:
            self.checkout_id = checkout_id
        if project_id is not None:
            self.project_id = project_id
        if invoice_id is not None:
            self.invoice_id = invoice_id

    @property
    def checkout_id(self):
        """Gets the checkout_id of this Confirmation.  # noqa: E501

        The unique ID of the checkout that was created as a result of the confirmation.  A string in the format: `checkout_[0-9a-z]`  # noqa: E501

        :return: The checkout_id of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._checkout_id

    @checkout_id.setter
    def checkout_id(self, checkout_id):
        """Sets the checkout_id of this Confirmation.

        The unique ID of the checkout that was created as a result of the confirmation.  A string in the format: `checkout_[0-9a-z]`  # noqa: E501

        :param checkout_id: The checkout_id of this Confirmation.  # noqa: E501
        :type: str
        """

        self._checkout_id = checkout_id

    @property
    def project_id(self):
        """Gets the project_id of this Confirmation.  # noqa: E501

        The unique ID of the project that was targeted as a result of the confirmation.  A string in the format: `project_[0-9a-z]`  # noqa: E501

        :return: The project_id of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Confirmation.

        The unique ID of the project that was targeted as a result of the confirmation.  A string in the format: `project_[0-9a-z]`  # noqa: E501

        :param project_id: The project_id of this Confirmation.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this Confirmation.  # noqa: E501

        The unique ID of the invoice that was created as a result of the confirmation.  A string in the format: `invoice_[0-9a-z]`  # noqa: E501

        :return: The invoice_id of this Confirmation.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this Confirmation.

        The unique ID of the invoice that was created as a result of the confirmation.  A string in the format: `invoice_[0-9a-z]`  # noqa: E501

        :param invoice_id: The invoice_id of this Confirmation.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

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
        if issubclass(Confirmation, dict):
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
        if not isinstance(other, Confirmation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other