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

class IdConfirmBody(object):
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
        'session_id': 'str',
        'type': 'PaymentType',
        'credit': 'CreditPaymentInput'
    }

    attribute_map = {
        'session_id': 'session_id',
        'type': 'type',
        'credit': 'credit'
    }

    def __init__(self, session_id=None, type=None, credit=None):  # noqa: E501
        """IdConfirmBody - a model defined in Swagger"""  # noqa: E501
        self._session_id = None
        self._type = None
        self._credit = None
        self.discriminator = None
        self.session_id = session_id
        self.type = type
        if credit is not None:
            self.credit = credit

    @property
    def session_id(self):
        """Gets the session_id of this IdConfirmBody.  # noqa: E501

        A unique ID of an existing session created by a setup intent.  A string in the format: `session_[0-9a-z]`  # noqa: E501

        :return: The session_id of this IdConfirmBody.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this IdConfirmBody.

        A unique ID of an existing session created by a setup intent.  A string in the format: `session_[0-9a-z]`  # noqa: E501

        :param session_id: The session_id of this IdConfirmBody.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def type(self):
        """Gets the type of this IdConfirmBody.  # noqa: E501


        :return: The type of this IdConfirmBody.  # noqa: E501
        :rtype: PaymentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdConfirmBody.


        :param type: The type of this IdConfirmBody.  # noqa: E501
        :type: PaymentType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def credit(self):
        """Gets the credit of this IdConfirmBody.  # noqa: E501


        :return: The credit of this IdConfirmBody.  # noqa: E501
        :rtype: CreditPaymentInput
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this IdConfirmBody.


        :param credit: The credit of this IdConfirmBody.  # noqa: E501
        :type: CreditPaymentInput
        """

        self._credit = credit

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
        if issubclass(IdConfirmBody, dict):
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
        if not isinstance(other, IdConfirmBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
