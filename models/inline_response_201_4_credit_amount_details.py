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


class InlineResponse2014CreditAmountDetails(object):
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
        'credit_amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'credit_amount': 'creditAmount',
        'currency': 'currency'
    }

    def __init__(self, credit_amount=None, currency=None):
        """
        InlineResponse2014CreditAmountDetails - a model defined in Swagger
        """

        self._credit_amount = None
        self._currency = None

        if credit_amount is not None:
          self.credit_amount = credit_amount
        if currency is not None:
          self.currency = currency

    @property
    def credit_amount(self):
        """
        Gets the credit_amount of this InlineResponse2014CreditAmountDetails.
        Total amount of the credit.

        :return: The credit_amount of this InlineResponse2014CreditAmountDetails.
        :rtype: str
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """
        Sets the credit_amount of this InlineResponse2014CreditAmountDetails.
        Total amount of the credit.

        :param credit_amount: The credit_amount of this InlineResponse2014CreditAmountDetails.
        :type: str
        """
        if credit_amount is not None and len(credit_amount) > 15:
            raise ValueError("Invalid value for `credit_amount`, length must be less than or equal to `15`")

        self._credit_amount = credit_amount

    @property
    def currency(self):
        """
        Gets the currency of this InlineResponse2014CreditAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes.  For an authorization reversal or a capture, you must use the same currency that you used in your request for Payment API. 

        :return: The currency of this InlineResponse2014CreditAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this InlineResponse2014CreditAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes.  For an authorization reversal or a capture, you must use the same currency that you used in your request for Payment API. 

        :param currency: The currency of this InlineResponse2014CreditAmountDetails.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")

        self._currency = currency

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
        if not isinstance(other, InlineResponse2014CreditAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
