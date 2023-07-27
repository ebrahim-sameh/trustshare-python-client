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

class Settlement(object):
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
        'currency': 'Currency',
        'status': 'SettlementStatus',
        'type': 'SettlementType',
        'project_id': 'str',
        '_from': 'KnownParticipant',
        'to': 'KnownParticipant',
        'amount': 'int',
        'description': 'str',
        'summary': 'str',
        'balance': 'int',
        'fee_flat': 'int',
        'fee_percentage': 'float',
        'tax_flat': 'int',
        'tax_percentage': 'float',
        'required_by': 'str',
        'release_at': 'str',
        'reference': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'currency': 'currency',
        'status': 'status',
        'type': 'type',
        'project_id': 'project_id',
        '_from': 'from',
        'to': 'to',
        'amount': 'amount',
        'description': 'description',
        'summary': 'summary',
        'balance': 'balance',
        'fee_flat': 'fee_flat',
        'fee_percentage': 'fee_percentage',
        'tax_flat': 'tax_flat',
        'tax_percentage': 'tax_percentage',
        'required_by': 'required_by',
        'release_at': 'release_at',
        'reference': 'reference',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, currency=None, status=None, type=None, project_id=None, _from=None, to=None, amount=None, description=None, summary=None, balance=None, fee_flat=None, fee_percentage=None, tax_flat=None, tax_percentage=None, required_by=None, release_at=None, reference=None, metadata=None):  # noqa: E501
        """Settlement - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._currency = None
        self._status = None
        self._type = None
        self._project_id = None
        self.__from = None
        self._to = None
        self._amount = None
        self._description = None
        self._summary = None
        self._balance = None
        self._fee_flat = None
        self._fee_percentage = None
        self._tax_flat = None
        self._tax_percentage = None
        self._required_by = None
        self._release_at = None
        self._reference = None
        self._metadata = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if currency is not None:
            self.currency = currency
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if project_id is not None:
            self.project_id = project_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if summary is not None:
            self.summary = summary
        if balance is not None:
            self.balance = balance
        if fee_flat is not None:
            self.fee_flat = fee_flat
        if fee_percentage is not None:
            self.fee_percentage = fee_percentage
        if tax_flat is not None:
            self.tax_flat = tax_flat
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if required_by is not None:
            self.required_by = required_by
        if release_at is not None:
            self.release_at = release_at
        if reference is not None:
            self.reference = reference
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this Settlement.  # noqa: E501

        A unique ID for the settlement.  A string in the format `settlement_[0-9a-z]`.  # noqa: E501

        :return: The id of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Settlement.

        A unique ID for the settlement.  A string in the format `settlement_[0-9a-z]`.  # noqa: E501

        :param id: The id of this Settlement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Settlement.  # noqa: E501

        The date the settlement was created.  # noqa: E501

        :return: The created_at of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Settlement.

        The date the settlement was created.  # noqa: E501

        :param created_at: The created_at of this Settlement.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Settlement.  # noqa: E501

        The date the settlement was last updated.  # noqa: E501

        :return: The updated_at of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Settlement.

        The date the settlement was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Settlement.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def currency(self):
        """Gets the currency of this Settlement.  # noqa: E501


        :return: The currency of this Settlement.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Settlement.


        :param currency: The currency of this Settlement.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def status(self):
        """Gets the status of this Settlement.  # noqa: E501


        :return: The status of this Settlement.  # noqa: E501
        :rtype: SettlementStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Settlement.


        :param status: The status of this Settlement.  # noqa: E501
        :type: SettlementStatus
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this Settlement.  # noqa: E501


        :return: The type of this Settlement.  # noqa: E501
        :rtype: SettlementType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Settlement.


        :param type: The type of this Settlement.  # noqa: E501
        :type: SettlementType
        """

        self._type = type

    @property
    def project_id(self):
        """Gets the project_id of this Settlement.  # noqa: E501

        The unique ID of the project which this settlement belongs to.  # noqa: E501

        :return: The project_id of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Settlement.

        The unique ID of the project which this settlement belongs to.  # noqa: E501

        :param project_id: The project_id of this Settlement.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def _from(self):
        """Gets the _from of this Settlement.  # noqa: E501


        :return: The _from of this Settlement.  # noqa: E501
        :rtype: KnownParticipant
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Settlement.


        :param _from: The _from of this Settlement.  # noqa: E501
        :type: KnownParticipant
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this Settlement.  # noqa: E501


        :return: The to of this Settlement.  # noqa: E501
        :rtype: KnownParticipant
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Settlement.


        :param to: The to of this Settlement.  # noqa: E501
        :type: KnownParticipant
        """

        self._to = to

    @property
    def amount(self):
        """Gets the amount of this Settlement.  # noqa: E501

        The amount of the settlement.  # noqa: E501

        :return: The amount of this Settlement.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Settlement.

        The amount of the settlement.  # noqa: E501

        :param amount: The amount of this Settlement.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this Settlement.  # noqa: E501

        The provided description of the settlement.  # noqa: E501

        :return: The description of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Settlement.

        The provided description of the settlement.  # noqa: E501

        :param description: The description of this Settlement.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def summary(self):
        """Gets the summary of this Settlement.  # noqa: E501

        The provided summary of the settlement.  # noqa: E501

        :return: The summary of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Settlement.

        The provided summary of the settlement.  # noqa: E501

        :param summary: The summary of this Settlement.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def balance(self):
        """Gets the balance of this Settlement.  # noqa: E501

        The current balance of the settlement. The balance for a settlement is calculated in the following way:  `balance` = `received` - (`released` + `refunded`)  A negative balance infers that funds have been released however we are still waiting for funds to reconcile into the settlement.  # noqa: E501

        :return: The balance of this Settlement.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Settlement.

        The current balance of the settlement. The balance for a settlement is calculated in the following way:  `balance` = `received` - (`released` + `refunded`)  A negative balance infers that funds have been released however we are still waiting for funds to reconcile into the settlement.  # noqa: E501

        :param balance: The balance of this Settlement.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def fee_flat(self):
        """Gets the fee_flat of this Settlement.  # noqa: E501

        The flat fee to charge the beneficiary Participant on successfully releasing funds from the settlement.  # noqa: E501

        :return: The fee_flat of this Settlement.  # noqa: E501
        :rtype: int
        """
        return self._fee_flat

    @fee_flat.setter
    def fee_flat(self, fee_flat):
        """Sets the fee_flat of this Settlement.

        The flat fee to charge the beneficiary Participant on successfully releasing funds from the settlement.  # noqa: E501

        :param fee_flat: The fee_flat of this Settlement.  # noqa: E501
        :type: int
        """

        self._fee_flat = fee_flat

    @property
    def fee_percentage(self):
        """Gets the fee_percentage of this Settlement.  # noqa: E501

        The fee percentage to charge the beneficiary Participant on successfully releasing funds from the settlement.  # noqa: E501

        :return: The fee_percentage of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._fee_percentage

    @fee_percentage.setter
    def fee_percentage(self, fee_percentage):
        """Sets the fee_percentage of this Settlement.

        The fee percentage to charge the beneficiary Participant on successfully releasing funds from the settlement.  # noqa: E501

        :param fee_percentage: The fee_percentage of this Settlement.  # noqa: E501
        :type: float
        """

        self._fee_percentage = fee_percentage

    @property
    def tax_flat(self):
        """Gets the tax_flat of this Settlement.  # noqa: E501

        The pre-computed flat tax charge that has been added to the value of the settlement. The settlement amount is inclusive of this value.  # noqa: E501

        :return: The tax_flat of this Settlement.  # noqa: E501
        :rtype: int
        """
        return self._tax_flat

    @tax_flat.setter
    def tax_flat(self, tax_flat):
        """Sets the tax_flat of this Settlement.

        The pre-computed flat tax charge that has been added to the value of the settlement. The settlement amount is inclusive of this value.  # noqa: E501

        :param tax_flat: The tax_flat of this Settlement.  # noqa: E501
        :type: int
        """

        self._tax_flat = tax_flat

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this Settlement.  # noqa: E501

        The tax charge that has been added to the value of the settlement, expressed as a percentage. The settlement amount is inclusive of the computed percentage amount.  # noqa: E501

        :return: The tax_percentage of this Settlement.  # noqa: E501
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this Settlement.

        The tax charge that has been added to the value of the settlement, expressed as a percentage. The settlement amount is inclusive of the computed percentage amount.  # noqa: E501

        :param tax_percentage: The tax_percentage of this Settlement.  # noqa: E501
        :type: float
        """

        self._tax_percentage = tax_percentage

    @property
    def required_by(self):
        """Gets the required_by of this Settlement.  # noqa: E501

        The date that describes when the funds are required.  # noqa: E501

        :return: The required_by of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._required_by

    @required_by.setter
    def required_by(self, required_by):
        """Sets the required_by of this Settlement.

        The date that describes when the funds are required.  # noqa: E501

        :param required_by: The required_by of this Settlement.  # noqa: E501
        :type: str
        """

        self._required_by = required_by

    @property
    def release_at(self):
        """Gets the release_at of this Settlement.  # noqa: E501

        The date that describes when the funds will be automatically released.  Verification will be eagerly attempted if required.  # noqa: E501

        :return: The release_at of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._release_at

    @release_at.setter
    def release_at(self, release_at):
        """Sets the release_at of this Settlement.

        The date that describes when the funds will be automatically released.  Verification will be eagerly attempted if required.  # noqa: E501

        :param release_at: The release_at of this Settlement.  # noqa: E501
        :type: str
        """

        self._release_at = release_at

    @property
    def reference(self):
        """Gets the reference of this Settlement.  # noqa: E501

        The reference that will be used for releases from this settlement.  # noqa: E501

        :return: The reference of this Settlement.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Settlement.

        The reference that will be used for releases from this settlement.  # noqa: E501

        :param reference: The reference of this Settlement.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def metadata(self):
        """Gets the metadata of this Settlement.  # noqa: E501

        The metadata that was provided at the creation of the underlying settlement intent.  # noqa: E501

        :return: The metadata of this Settlement.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Settlement.

        The metadata that was provided at the creation of the underlying settlement intent.  # noqa: E501

        :param metadata: The metadata of this Settlement.  # noqa: E501
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
        if issubclass(Settlement, dict):
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
        if not isinstance(other, Settlement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other