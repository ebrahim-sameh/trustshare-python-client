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

class ReleaseInput(object):
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
        'settlement_id': 'str',
        'project_id': 'str',
        'amount': 'int',
        'fee_flat': 'int',
        'fee_percentage': 'float',
        'to': 'ParticipantInput',
        'release_at': 'str',
        'reference': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'settlement_id': 'settlement_id',
        'project_id': 'project_id',
        'amount': 'amount',
        'fee_flat': 'fee_flat',
        'fee_percentage': 'fee_percentage',
        'to': 'to',
        'release_at': 'release_at',
        'reference': 'reference',
        'metadata': 'metadata'
    }

    def __init__(self, settlement_id=None, project_id=None, amount=None, fee_flat=None, fee_percentage=None, to=None, release_at=None, reference=None, metadata=None):  # noqa: E501
        """ReleaseInput - a model defined in Swagger"""  # noqa: E501
        self._settlement_id = None
        self._project_id = None
        self._amount = None
        self._fee_flat = None
        self._fee_percentage = None
        self._to = None
        self._release_at = None
        self._reference = None
        self._metadata = None
        self.discriminator = None
        if settlement_id is not None:
            self.settlement_id = settlement_id
        if project_id is not None:
            self.project_id = project_id
        if amount is not None:
            self.amount = amount
        if fee_flat is not None:
            self.fee_flat = fee_flat
        if fee_percentage is not None:
            self.fee_percentage = fee_percentage
        if to is not None:
            self.to = to
        if release_at is not None:
            self.release_at = release_at
        if reference is not None:
            self.reference = reference
        if metadata is not None:
            self.metadata = metadata

    @property
    def settlement_id(self):
        """Gets the settlement_id of this ReleaseInput.  # noqa: E501

        A unique ID of the settlement to release funds from.  A string in the format: `settlement_[0-9a-z]`.  # noqa: E501

        :return: The settlement_id of this ReleaseInput.  # noqa: E501
        :rtype: str
        """
        return self._settlement_id

    @settlement_id.setter
    def settlement_id(self, settlement_id):
        """Sets the settlement_id of this ReleaseInput.

        A unique ID of the settlement to release funds from.  A string in the format: `settlement_[0-9a-z]`.  # noqa: E501

        :param settlement_id: The settlement_id of this ReleaseInput.  # noqa: E501
        :type: str
        """

        self._settlement_id = settlement_id

    @property
    def project_id(self):
        """Gets the project_id of this ReleaseInput.  # noqa: E501

        A unique ID of the project to release funds from.  A string in the format: `project_[0-9a-z]`.  # noqa: E501

        :return: The project_id of this ReleaseInput.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ReleaseInput.

        A unique ID of the project to release funds from.  A string in the format: `project_[0-9a-z]`.  # noqa: E501

        :param project_id: The project_id of this ReleaseInput.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def amount(self):
        """Gets the amount of this ReleaseInput.  # noqa: E501

        The amount to release in the currency's lowest denomination.  # noqa: E501

        :return: The amount of this ReleaseInput.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ReleaseInput.

        The amount to release in the currency's lowest denomination.  # noqa: E501

        :param amount: The amount of this ReleaseInput.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def fee_flat(self):
        """Gets the fee_flat of this ReleaseInput.  # noqa: E501

        A flat fee to charge the beneficiary Participant on successfully releasing funds.  # noqa: E501

        :return: The fee_flat of this ReleaseInput.  # noqa: E501
        :rtype: int
        """
        return self._fee_flat

    @fee_flat.setter
    def fee_flat(self, fee_flat):
        """Sets the fee_flat of this ReleaseInput.

        A flat fee to charge the beneficiary Participant on successfully releasing funds.  # noqa: E501

        :param fee_flat: The fee_flat of this ReleaseInput.  # noqa: E501
        :type: int
        """

        self._fee_flat = fee_flat

    @property
    def fee_percentage(self):
        """Gets the fee_percentage of this ReleaseInput.  # noqa: E501

        The fee percentage to charge the beneficiary Participant on successfully releasing funds.  # noqa: E501

        :return: The fee_percentage of this ReleaseInput.  # noqa: E501
        :rtype: float
        """
        return self._fee_percentage

    @fee_percentage.setter
    def fee_percentage(self, fee_percentage):
        """Sets the fee_percentage of this ReleaseInput.

        The fee percentage to charge the beneficiary Participant on successfully releasing funds.  # noqa: E501

        :param fee_percentage: The fee_percentage of this ReleaseInput.  # noqa: E501
        :type: float
        """

        self._fee_percentage = fee_percentage

    @property
    def to(self):
        """Gets the to of this ReleaseInput.  # noqa: E501


        :return: The to of this ReleaseInput.  # noqa: E501
        :rtype: ParticipantInput
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ReleaseInput.


        :param to: The to of this ReleaseInput.  # noqa: E501
        :type: ParticipantInput
        """

        self._to = to

    @property
    def release_at(self):
        """Gets the release_at of this ReleaseInput.  # noqa: E501

        A date that describes when the funds should be automatically released.  Verification will be eagerly attempted if required.  # noqa: E501

        :return: The release_at of this ReleaseInput.  # noqa: E501
        :rtype: str
        """
        return self._release_at

    @release_at.setter
    def release_at(self, release_at):
        """Sets the release_at of this ReleaseInput.

        A date that describes when the funds should be automatically released.  Verification will be eagerly attempted if required.  # noqa: E501

        :param release_at: The release_at of this ReleaseInput.  # noqa: E501
        :type: str
        """

        self._release_at = release_at

    @property
    def reference(self):
        """Gets the reference of this ReleaseInput.  # noqa: E501

        A reference that should be used for the outbound.  The reference can be up to 18 characters in length and supports `a-z`, `A-Z`, `0-9`, `-`, and space characters. This will fall back to your company name if no reference is provided.  # noqa: E501

        :return: The reference of this ReleaseInput.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ReleaseInput.

        A reference that should be used for the outbound.  The reference can be up to 18 characters in length and supports `a-z`, `A-Z`, `0-9`, `-`, and space characters. This will fall back to your company name if no reference is provided.  # noqa: E501

        :param reference: The reference of this ReleaseInput.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def metadata(self):
        """Gets the metadata of this ReleaseInput.  # noqa: E501

        A free-form metadata object that you can use to store against the outbound. This is incredibly useful for storing a correlation ID that relates to an entity on your own system.  # noqa: E501

        :return: The metadata of this ReleaseInput.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ReleaseInput.

        A free-form metadata object that you can use to store against the outbound. This is incredibly useful for storing a correlation ID that relates to an entity on your own system.  # noqa: E501

        :param metadata: The metadata of this ReleaseInput.  # noqa: E501
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
        if issubclass(ReleaseInput, dict):
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
        if not isinstance(other, ReleaseInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
