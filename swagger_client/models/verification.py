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

class Verification(object):
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
        'type': 'VerificationType',
        'status': 'VerificationStatus',
        'participant': 'KnownParticipant',
        'client_secret': 'str',
        'redirect_url': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'participant': 'participant',
        'client_secret': 'client_secret',
        'redirect_url': 'redirect_url',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, type=None, status=None, participant=None, client_secret=None, redirect_url=None, metadata=None):  # noqa: E501
        """Verification - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._status = None
        self._participant = None
        self._client_secret = None
        self._redirect_url = None
        self._metadata = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if participant is not None:
            self.participant = participant
        if client_secret is not None:
            self.client_secret = client_secret
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this Verification.  # noqa: E501

        A unique ID of the verification.  A string in the format: `verification_[0-9a-z]`.  # noqa: E501

        :return: The id of this Verification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Verification.

        A unique ID of the verification.  A string in the format: `verification_[0-9a-z]`.  # noqa: E501

        :param id: The id of this Verification.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Verification.  # noqa: E501


        :return: The type of this Verification.  # noqa: E501
        :rtype: VerificationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Verification.


        :param type: The type of this Verification.  # noqa: E501
        :type: VerificationType
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this Verification.  # noqa: E501


        :return: The status of this Verification.  # noqa: E501
        :rtype: VerificationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Verification.


        :param status: The status of this Verification.  # noqa: E501
        :type: VerificationStatus
        """

        self._status = status

    @property
    def participant(self):
        """Gets the participant of this Verification.  # noqa: E501


        :return: The participant of this Verification.  # noqa: E501
        :rtype: KnownParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this Verification.


        :param participant: The participant of this Verification.  # noqa: E501
        :type: KnownParticipant
        """

        self._participant = participant

    @property
    def client_secret(self):
        """Gets the client_secret of this Verification.  # noqa: E501

        The client secret for the verification.  <Note>   This secret should __never__ be stored on a backend system and should   always be directly passed down to the expected participant's device. </Note>  # noqa: E501

        :return: The client_secret of this Verification.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this Verification.

        The client secret for the verification.  <Note>   This secret should __never__ be stored on a backend system and should   always be directly passed down to the expected participant's device. </Note>  # noqa: E501

        :param client_secret: The client_secret of this Verification.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def redirect_url(self):
        """Gets the redirect_url of this Verification.  # noqa: E501

        The redirect URL supplied at the creation of the verification.  # noqa: E501

        :return: The redirect_url of this Verification.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this Verification.

        The redirect URL supplied at the creation of the verification.  # noqa: E501

        :param redirect_url: The redirect_url of this Verification.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def metadata(self):
        """Gets the metadata of this Verification.  # noqa: E501

        The metadata that was provided at the creation of the verification.  # noqa: E501

        :return: The metadata of this Verification.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Verification.

        The metadata that was provided at the creation of the verification.  # noqa: E501

        :param metadata: The metadata of this Verification.  # noqa: E501
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
        if issubclass(Verification, dict):
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
        if not isinstance(other, Verification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
