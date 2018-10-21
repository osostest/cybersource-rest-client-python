# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PaymentinstrumentsCard(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'issue_number': 'str',
        'start_month': 'str',
        'start_year': 'str',
        'use_as': 'str'
    }

    attribute_map = {
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'issue_number': 'issueNumber',
        'start_month': 'startMonth',
        'start_year': 'startYear',
        'use_as': 'useAs'
    }

    def __init__(self, expiration_month=None, expiration_year=None, type=None, issue_number=None, start_month=None, start_year=None, use_as=None):
        """
        PaymentinstrumentsCard - a model defined in Swagger
        """

        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._issue_number = None
        self._start_month = None
        self._start_year = None
        self._use_as = None

        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if type is not None:
          self.type = type
        if issue_number is not None:
          self.issue_number = issue_number
        if start_month is not None:
          self.start_month = start_month
        if start_year is not None:
          self.start_year = start_year
        if use_as is not None:
          self.use_as = use_as

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this PaymentinstrumentsCard.
        Credit card expiration month.

        :return: The expiration_month of this PaymentinstrumentsCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this PaymentinstrumentsCard.
        Credit card expiration month.

        :param expiration_month: The expiration_month of this PaymentinstrumentsCard.
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this PaymentinstrumentsCard.
        Credit card expiration year.

        :return: The expiration_year of this PaymentinstrumentsCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this PaymentinstrumentsCard.
        Credit card expiration year.

        :param expiration_year: The expiration_year of this PaymentinstrumentsCard.
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this PaymentinstrumentsCard.
        Credit card brand.

        :return: The type of this PaymentinstrumentsCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PaymentinstrumentsCard.
        Credit card brand.

        :param type: The type of this PaymentinstrumentsCard.
        :type: str
        """
        allowed_values = ["visa", "mastercard", "american express", "discover", "diners club", "carte blanche", "jcb", "optima", "twinpay credit", "twinpay debit", "walmart", "enroute", "lowes consumer", "home depot consumer", "mbna", "dicks sportswear", "casual corner", "sears", "jal", "disney", "maestro uk domestic", "sams club consumer", "sams club business", "nicos", "bill me later", "bebe", "restoration hardware", "delta online", "solo", "visa electron", "dankort", "laser", "carte bleue", "carta si", "pinless debit", "encoded account", "uatp", "household", "maestro international", "ge money uk", "korean cards", "style", "jcrew", "payease china processing ewallet", "payease china processing bank transfer", "meijer private label", "hipercard", "aura", "redecard", "orico", "elo", "capital one private label", "synchrony private label", "china union pay"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def issue_number(self):
        """
        Gets the issue_number of this PaymentinstrumentsCard.
        Credit card issue number.

        :return: The issue_number of this PaymentinstrumentsCard.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """
        Sets the issue_number of this PaymentinstrumentsCard.
        Credit card issue number.

        :param issue_number: The issue_number of this PaymentinstrumentsCard.
        :type: str
        """

        self._issue_number = issue_number

    @property
    def start_month(self):
        """
        Gets the start_month of this PaymentinstrumentsCard.
        Credit card start month.

        :return: The start_month of this PaymentinstrumentsCard.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """
        Sets the start_month of this PaymentinstrumentsCard.
        Credit card start month.

        :param start_month: The start_month of this PaymentinstrumentsCard.
        :type: str
        """

        self._start_month = start_month

    @property
    def start_year(self):
        """
        Gets the start_year of this PaymentinstrumentsCard.
        Credit card start year.

        :return: The start_year of this PaymentinstrumentsCard.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this PaymentinstrumentsCard.
        Credit card start year.

        :param start_year: The start_year of this PaymentinstrumentsCard.
        :type: str
        """

        self._start_year = start_year

    @property
    def use_as(self):
        """
        Gets the use_as of this PaymentinstrumentsCard.
        Card Use As Field. Supported value of \"pinless debit\" only. Only for use with Pinless Debit tokens.

        :return: The use_as of this PaymentinstrumentsCard.
        :rtype: str
        """
        return self._use_as

    @use_as.setter
    def use_as(self, use_as):
        """
        Sets the use_as of this PaymentinstrumentsCard.
        Card Use As Field. Supported value of \"pinless debit\" only. Only for use with Pinless Debit tokens.

        :param use_as: The use_as of this PaymentinstrumentsCard.
        :type: str
        """

        self._use_as = use_as

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PaymentinstrumentsCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
