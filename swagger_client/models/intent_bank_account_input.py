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

class IntentBankAccountInput(object):
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
        'country': 'Country',
        'currency': 'BankAccountCurrency',
        'account_number': 'str',
        'iban': 'str',
        'aba': 'str',
        'bank_code': 'str',
        'bic_swift': 'str',
        'branch_code': 'str',
        'bsb_code': 'str',
        'clabe': 'str',
        'cnaps': 'str',
        'ifsc': 'str',
        'sort_code': 'str',
        'bank_name': 'str',
        'bank_address': 'str',
        'identification': 'str'
    }

    attribute_map = {
        'id': 'id',
        'country': 'country',
        'currency': 'currency',
        'account_number': 'account_number',
        'iban': 'iban',
        'aba': 'aba',
        'bank_code': 'bank_code',
        'bic_swift': 'bic_swift',
        'branch_code': 'branch_code',
        'bsb_code': 'bsb_code',
        'clabe': 'clabe',
        'cnaps': 'cnaps',
        'ifsc': 'ifsc',
        'sort_code': 'sort_code',
        'bank_name': 'bank_name',
        'bank_address': 'bank_address',
        'identification': 'identification'
    }

    def __init__(self, id=None, country=None, currency=None, account_number=None, iban=None, aba=None, bank_code=None, bic_swift=None, branch_code=None, bsb_code=None, clabe=None, cnaps=None, ifsc=None, sort_code=None, bank_name=None, bank_address=None, identification=None):  # noqa: E501
        """IntentBankAccountInput - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._country = None
        self._currency = None
        self._account_number = None
        self._iban = None
        self._aba = None
        self._bank_code = None
        self._bic_swift = None
        self._branch_code = None
        self._bsb_code = None
        self._clabe = None
        self._cnaps = None
        self._ifsc = None
        self._sort_code = None
        self._bank_name = None
        self._bank_address = None
        self._identification = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if country is not None:
            self.country = country
        if currency is not None:
            self.currency = currency
        if account_number is not None:
            self.account_number = account_number
        if iban is not None:
            self.iban = iban
        if aba is not None:
            self.aba = aba
        if bank_code is not None:
            self.bank_code = bank_code
        if bic_swift is not None:
            self.bic_swift = bic_swift
        if branch_code is not None:
            self.branch_code = branch_code
        if bsb_code is not None:
            self.bsb_code = bsb_code
        if clabe is not None:
            self.clabe = clabe
        if cnaps is not None:
            self.cnaps = cnaps
        if ifsc is not None:
            self.ifsc = ifsc
        if sort_code is not None:
            self.sort_code = sort_code
        if bank_name is not None:
            self.bank_name = bank_name
        if bank_address is not None:
            self.bank_address = bank_address
        if identification is not None:
            self.identification = identification

    @property
    def id(self):
        """Gets the id of this IntentBankAccountInput.  # noqa: E501

        A unique ID of a bank account to target for this intent.  A string in the format: `bank_account_[0-9a-z]`.  # noqa: E501

        :return: The id of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntentBankAccountInput.

        A unique ID of a bank account to target for this intent.  A string in the format: `bank_account_[0-9a-z]`.  # noqa: E501

        :param id: The id of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def country(self):
        """Gets the country of this IntentBankAccountInput.  # noqa: E501


        :return: The country of this IntentBankAccountInput.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IntentBankAccountInput.


        :param country: The country of this IntentBankAccountInput.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def currency(self):
        """Gets the currency of this IntentBankAccountInput.  # noqa: E501


        :return: The currency of this IntentBankAccountInput.  # noqa: E501
        :rtype: BankAccountCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IntentBankAccountInput.


        :param currency: The currency of this IntentBankAccountInput.  # noqa: E501
        :type: BankAccountCurrency
        """

        self._currency = currency

    @property
    def account_number(self):
        """Gets the account_number of this IntentBankAccountInput.  # noqa: E501

        The account number of the bank account.  # noqa: E501

        :return: The account_number of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this IntentBankAccountInput.

        The account number of the bank account.  # noqa: E501

        :param account_number: The account_number of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def iban(self):
        """Gets the iban of this IntentBankAccountInput.  # noqa: E501

        The IBAN of the bank account.  # noqa: E501

        :return: The iban of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this IntentBankAccountInput.

        The IBAN of the bank account.  # noqa: E501

        :param iban: The iban of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def aba(self):
        """Gets the aba of this IntentBankAccountInput.  # noqa: E501

        The ABA routing code of the bank account (US only).  # noqa: E501

        :return: The aba of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._aba

    @aba.setter
    def aba(self, aba):
        """Sets the aba of this IntentBankAccountInput.

        The ABA routing code of the bank account (US only).  # noqa: E501

        :param aba: The aba of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._aba = aba

    @property
    def bank_code(self):
        """Gets the bank_code of this IntentBankAccountInput.  # noqa: E501

        The Bank Code of the bank account.  # noqa: E501

        :return: The bank_code of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this IntentBankAccountInput.

        The Bank Code of the bank account.  # noqa: E501

        :param bank_code: The bank_code of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

    @property
    def bic_swift(self):
        """Gets the bic_swift of this IntentBankAccountInput.  # noqa: E501

        The Bank Identifier Code of the bank account on the SWIFT network.  # noqa: E501

        :return: The bic_swift of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._bic_swift

    @bic_swift.setter
    def bic_swift(self, bic_swift):
        """Sets the bic_swift of this IntentBankAccountInput.

        The Bank Identifier Code of the bank account on the SWIFT network.  # noqa: E501

        :param bic_swift: The bic_swift of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._bic_swift = bic_swift

    @property
    def branch_code(self):
        """Gets the branch_code of this IntentBankAccountInput.  # noqa: E501

        The Branch Code of the bank account.  # noqa: E501

        :return: The branch_code of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this IntentBankAccountInput.

        The Branch Code of the bank account.  # noqa: E501

        :param branch_code: The branch_code of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._branch_code = branch_code

    @property
    def bsb_code(self):
        """Gets the bsb_code of this IntentBankAccountInput.  # noqa: E501

        The BSB code of the bank account (AU only).  # noqa: E501

        :return: The bsb_code of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._bsb_code

    @bsb_code.setter
    def bsb_code(self, bsb_code):
        """Sets the bsb_code of this IntentBankAccountInput.

        The BSB code of the bank account (AU only).  # noqa: E501

        :param bsb_code: The bsb_code of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._bsb_code = bsb_code

    @property
    def clabe(self):
        """Gets the clabe of this IntentBankAccountInput.  # noqa: E501

        The CLABE of the bank account (MX only).  # noqa: E501

        :return: The clabe of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._clabe

    @clabe.setter
    def clabe(self, clabe):
        """Sets the clabe of this IntentBankAccountInput.

        The CLABE of the bank account (MX only).  # noqa: E501

        :param clabe: The clabe of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._clabe = clabe

    @property
    def cnaps(self):
        """Gets the cnaps of this IntentBankAccountInput.  # noqa: E501

        The CNAPS of the bank account (CN only).  # noqa: E501

        :return: The cnaps of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._cnaps

    @cnaps.setter
    def cnaps(self, cnaps):
        """Sets the cnaps of this IntentBankAccountInput.

        The CNAPS of the bank account (CN only).  # noqa: E501

        :param cnaps: The cnaps of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._cnaps = cnaps

    @property
    def ifsc(self):
        """Gets the ifsc of this IntentBankAccountInput.  # noqa: E501

        The IFSC of the bank account (IN only).  # noqa: E501

        :return: The ifsc of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._ifsc

    @ifsc.setter
    def ifsc(self, ifsc):
        """Sets the ifsc of this IntentBankAccountInput.

        The IFSC of the bank account (IN only).  # noqa: E501

        :param ifsc: The ifsc of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._ifsc = ifsc

    @property
    def sort_code(self):
        """Gets the sort_code of this IntentBankAccountInput.  # noqa: E501

        The Sort Code of the bank account (UK only).  # noqa: E501

        :return: The sort_code of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this IntentBankAccountInput.

        The Sort Code of the bank account (UK only).  # noqa: E501

        :param sort_code: The sort_code of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._sort_code = sort_code

    @property
    def bank_name(self):
        """Gets the bank_name of this IntentBankAccountInput.  # noqa: E501

        The Bank Name of the bank account.  # noqa: E501

        :return: The bank_name of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this IntentBankAccountInput.

        The Bank Name of the bank account.  # noqa: E501

        :param bank_name: The bank_name of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bank_address(self):
        """Gets the bank_address of this IntentBankAccountInput.  # noqa: E501

        The Bank Address of the bank account.  # noqa: E501

        :return: The bank_address of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._bank_address

    @bank_address.setter
    def bank_address(self, bank_address):
        """Sets the bank_address of this IntentBankAccountInput.

        The Bank Address of the bank account.  # noqa: E501

        :param bank_address: The bank_address of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._bank_address = bank_address

    @property
    def identification(self):
        """Gets the identification of this IntentBankAccountInput.  # noqa: E501

        The identification type of the bank account (MX only).  # noqa: E501

        :return: The identification of this IntentBankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this IntentBankAccountInput.

        The identification type of the bank account (MX only).  # noqa: E501

        :param identification: The identification of this IntentBankAccountInput.  # noqa: E501
        :type: str
        """

        self._identification = identification

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
        if issubclass(IntentBankAccountInput, dict):
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
        if not isinstance(other, IntentBankAccountInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
