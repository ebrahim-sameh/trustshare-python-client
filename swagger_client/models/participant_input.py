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

class ParticipantInput(object):
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
        'id': 'str',
        'email': 'str',
        'type': 'ParticipantType',
        'name': 'str',
        'address': 'AddressInput',
        'bank_account': 'IntentBankAccountInput',
        'business': 'BusinessInput',
        'individual': 'IndividualInput',
        'organisation': 'OrganisationInput',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'type': 'type',
        'name': 'name',
        'address': 'address',
        'bank_account': 'bank_account',
        'business': 'business',
        'individual': 'individual',
        'organisation': 'organisation',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, email=None, type=None, name=None, address=None, bank_account=None, business=None, individual=None, organisation=None, metadata=None):  # noqa: E501
        """ParticipantInput - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._email = None
        self._type = None
        self._name = None
        self._address = None
        self._bank_account = None
        self._business = None
        self._individual = None
        self._organisation = None
        self._metadata = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if bank_account is not None:
            self.bank_account = bank_account
        if business is not None:
            self.business = business
        if individual is not None:
            self.individual = individual
        if organisation is not None:
            self.organisation = organisation
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this ParticipantInput.  # noqa: E501

        A unique ID of a participant that already exists on the system.  A string in the format: `participant_[0-9a-z]`.  # noqa: E501

        :return: The id of this ParticipantInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParticipantInput.

        A unique ID of a participant that already exists on the system.  A string in the format: `participant_[0-9a-z]`.  # noqa: E501

        :param id: The id of this ParticipantInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this ParticipantInput.  # noqa: E501

        The email address of the participant.  # noqa: E501

        :return: The email of this ParticipantInput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ParticipantInput.

        The email address of the participant.  # noqa: E501

        :param email: The email of this ParticipantInput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def type(self):
        """Gets the type of this ParticipantInput.  # noqa: E501


        :return: The type of this ParticipantInput.  # noqa: E501
        :rtype: ParticipantType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ParticipantInput.


        :param type: The type of this ParticipantInput.  # noqa: E501
        :type: ParticipantType
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this ParticipantInput.  # noqa: E501

        The participant's name.  # noqa: E501

        :return: The name of this ParticipantInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParticipantInput.

        The participant's name.  # noqa: E501

        :param name: The name of this ParticipantInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this ParticipantInput.  # noqa: E501


        :return: The address of this ParticipantInput.  # noqa: E501
        :rtype: AddressInput
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ParticipantInput.


        :param address: The address of this ParticipantInput.  # noqa: E501
        :type: AddressInput
        """

        self._address = address

    @property
    def bank_account(self):
        """Gets the bank_account of this ParticipantInput.  # noqa: E501


        :return: The bank_account of this ParticipantInput.  # noqa: E501
        :rtype: IntentBankAccountInput
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """Sets the bank_account of this ParticipantInput.


        :param bank_account: The bank_account of this ParticipantInput.  # noqa: E501
        :type: IntentBankAccountInput
        """

        self._bank_account = bank_account

    @property
    def business(self):
        """Gets the business of this ParticipantInput.  # noqa: E501


        :return: The business of this ParticipantInput.  # noqa: E501
        :rtype: BusinessInput
        """
        return self._business

    @business.setter
    def business(self, business):
        """Sets the business of this ParticipantInput.


        :param business: The business of this ParticipantInput.  # noqa: E501
        :type: BusinessInput
        """

        self._business = business

    @property
    def individual(self):
        """Gets the individual of this ParticipantInput.  # noqa: E501


        :return: The individual of this ParticipantInput.  # noqa: E501
        :rtype: IndividualInput
        """
        return self._individual

    @individual.setter
    def individual(self, individual):
        """Sets the individual of this ParticipantInput.


        :param individual: The individual of this ParticipantInput.  # noqa: E501
        :type: IndividualInput
        """

        self._individual = individual

    @property
    def organisation(self):
        """Gets the organisation of this ParticipantInput.  # noqa: E501


        :return: The organisation of this ParticipantInput.  # noqa: E501
        :rtype: OrganisationInput
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this ParticipantInput.


        :param organisation: The organisation of this ParticipantInput.  # noqa: E501
        :type: OrganisationInput
        """

        self._organisation = organisation

    @property
    def metadata(self):
        """Gets the metadata of this ParticipantInput.  # noqa: E501

        A free-form metadata object that you can use to store against the participant. This is incredibly useful for storing a correlation ID that relates to an entity on your own system.  # noqa: E501

        :return: The metadata of this ParticipantInput.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ParticipantInput.

        A free-form metadata object that you can use to store against the participant. This is incredibly useful for storing a correlation ID that relates to an entity on your own system.  # noqa: E501

        :param metadata: The metadata of this ParticipantInput.  # noqa: E501
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
        if issubclass(ParticipantInput, dict):
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
        if not isinstance(other, ParticipantInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
