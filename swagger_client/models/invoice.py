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

class Invoice(object):
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
        'created_at': 'str',
        'updated_at': 'str',
        'status': 'InvoiceStatus',
        'currency': 'Currency',
        'intent_id': 'str',
        'project_id': 'str',
        'participant': 'KnownParticipant',
        'settlements': 'list[Settlement]',
        'collect': 'Collect',
        'reference': 'str',
        'subtotal': 'int',
        'fee': 'int',
        'total': 'int',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'currency': 'currency',
        'intent_id': 'intent_id',
        'project_id': 'project_id',
        'participant': 'participant',
        'settlements': 'settlements',
        'collect': 'collect',
        'reference': 'reference',
        'subtotal': 'subtotal',
        'fee': 'fee',
        'total': 'total',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, status=None, currency=None, intent_id=None, project_id=None, participant=None, settlements=None, collect=None, reference=None, subtotal=None, fee=None, total=None, metadata=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._currency = None
        self._intent_id = None
        self._project_id = None
        self._participant = None
        self._settlements = None
        self._collect = None
        self._reference = None
        self._subtotal = None
        self._fee = None
        self._total = None
        self._metadata = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if currency is not None:
            self.currency = currency
        if intent_id is not None:
            self.intent_id = intent_id
        if project_id is not None:
            self.project_id = project_id
        if participant is not None:
            self.participant = participant
        if settlements is not None:
            self.settlements = settlements
        if collect is not None:
            self.collect = collect
        if reference is not None:
            self.reference = reference
        if subtotal is not None:
            self.subtotal = subtotal
        if fee is not None:
            self.fee = fee
        if total is not None:
            self.total = total
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this Invoice.  # noqa: E501

        A unique ID for the invoice.  A string in the format `invoice_[0-9a-z]`.  # noqa: E501

        :return: The id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invoice.

        A unique ID for the invoice.  A string in the format `invoice_[0-9a-z]`.  # noqa: E501

        :param id: The id of this Invoice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Invoice.  # noqa: E501

        The date the invoice was created.  # noqa: E501

        :return: The created_at of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Invoice.

        The date the invoice was created.  # noqa: E501

        :param created_at: The created_at of this Invoice.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Invoice.  # noqa: E501

        The date the invoice was last updated.  # noqa: E501

        :return: The updated_at of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Invoice.

        The date the invoice was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Invoice.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501


        :return: The status of this Invoice.  # noqa: E501
        :rtype: InvoiceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.  # noqa: E501
        :type: InvoiceStatus
        """

        self._status = status

    @property
    def currency(self):
        """Gets the currency of this Invoice.  # noqa: E501


        :return: The currency of this Invoice.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Invoice.


        :param currency: The currency of this Invoice.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def intent_id(self):
        """Gets the intent_id of this Invoice.  # noqa: E501

        The unique ID of the intent which caused the invoice to be created.  # noqa: E501

        :return: The intent_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._intent_id

    @intent_id.setter
    def intent_id(self, intent_id):
        """Sets the intent_id of this Invoice.

        The unique ID of the intent which caused the invoice to be created.  # noqa: E501

        :param intent_id: The intent_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._intent_id = intent_id

    @property
    def project_id(self):
        """Gets the project_id of this Invoice.  # noqa: E501

        The project ID the invoice was created against.  # noqa: E501

        :return: The project_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Invoice.

        The project ID the invoice was created against.  # noqa: E501

        :param project_id: The project_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def participant(self):
        """Gets the participant of this Invoice.  # noqa: E501


        :return: The participant of this Invoice.  # noqa: E501
        :rtype: KnownParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this Invoice.


        :param participant: The participant of this Invoice.  # noqa: E501
        :type: KnownParticipant
        """

        self._participant = participant

    @property
    def settlements(self):
        """Gets the settlements of this Invoice.  # noqa: E501

        A list of settlements against the invoice.  # noqa: E501

        :return: The settlements of this Invoice.  # noqa: E501
        :rtype: list[Settlement]
        """
        return self._settlements

    @settlements.setter
    def settlements(self, settlements):
        """Sets the settlements of this Invoice.

        A list of settlements against the invoice.  # noqa: E501

        :param settlements: The settlements of this Invoice.  # noqa: E501
        :type: list[Settlement]
        """

        self._settlements = settlements

    @property
    def collect(self):
        """Gets the collect of this Invoice.  # noqa: E501


        :return: The collect of this Invoice.  # noqa: E501
        :rtype: Collect
        """
        return self._collect

    @collect.setter
    def collect(self, collect):
        """Sets the collect of this Invoice.


        :param collect: The collect of this Invoice.  # noqa: E501
        :type: Collect
        """

        self._collect = collect

    @property
    def reference(self):
        """Gets the reference of this Invoice.  # noqa: E501

        The unique reference for the invoice. This should be used for all bank transfers targeting this invoice.  # noqa: E501

        :return: The reference of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Invoice.

        The unique reference for the invoice. This should be used for all bank transfers targeting this invoice.  # noqa: E501

        :param reference: The reference of this Invoice.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def subtotal(self):
        """Gets the subtotal of this Invoice.  # noqa: E501

        The invoice value denominated in the smallest unit for the currency. E.g. pence and cents.  # noqa: E501

        :return: The subtotal of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this Invoice.

        The invoice value denominated in the smallest unit for the currency. E.g. pence and cents.  # noqa: E501

        :param subtotal: The subtotal of this Invoice.  # noqa: E501
        :type: int
        """

        self._subtotal = subtotal

    @property
    def fee(self):
        """Gets the fee of this Invoice.  # noqa: E501

        The buyer fees specified for the invoice intent, denominated in the smallest unit for the currency. E.g. pence and cents.  # noqa: E501

        :return: The fee of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this Invoice.

        The buyer fees specified for the invoice intent, denominated in the smallest unit for the currency. E.g. pence and cents.  # noqa: E501

        :param fee: The fee of this Invoice.  # noqa: E501
        :type: int
        """

        self._fee = fee

    @property
    def total(self):
        """Gets the total of this Invoice.  # noqa: E501

        The full payable amount for the invoice (subtotal + fee), denominated in the smallest unit for the currency. E.g. pence and cents.  # noqa: E501

        :return: The total of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Invoice.

        The full payable amount for the invoice (subtotal + fee), denominated in the smallest unit for the currency. E.g. pence and cents.  # noqa: E501

        :param total: The total of this Invoice.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def metadata(self):
        """Gets the metadata of this Invoice.  # noqa: E501

        The metadata that was provided at the creation of the payment intent that caused this invoice.  # noqa: E501

        :return: The metadata of this Invoice.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Invoice.

        The metadata that was provided at the creation of the payment intent that caused this invoice.  # noqa: E501

        :param metadata: The metadata of this Invoice.  # noqa: E501
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
        if issubclass(Invoice, dict):
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
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
