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


class InlineResponse2013RefundAmountDetails(object):
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
        'refund_amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'refund_amount': 'refundAmount',
        'currency': 'currency'
    }

    def __init__(self, refund_amount=None, currency=None):
        """
        InlineResponse2013RefundAmountDetails - a model defined in Swagger
        """

        self._refund_amount = None
        self._currency = None

        if refund_amount is not None:
          self.refund_amount = refund_amount
        if currency is not None:
          self.currency = currency

    @property
    def refund_amount(self):
        """
        Gets the refund_amount of this InlineResponse2013RefundAmountDetails.
        Total amount of the refund.

        :return: The refund_amount of this InlineResponse2013RefundAmountDetails.
        :rtype: str
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """
        Sets the refund_amount of this InlineResponse2013RefundAmountDetails.
        Total amount of the refund.

        :param refund_amount: The refund_amount of this InlineResponse2013RefundAmountDetails.
        :type: str
        """
        if refund_amount is not None and len(refund_amount) > 15:
            raise ValueError("Invalid value for `refund_amount`, length must be less than or equal to `15`")

        self._refund_amount = refund_amount

    @property
    def currency(self):
        """
        Gets the currency of this InlineResponse2013RefundAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes.  For an authorization reversal or a capture, you must use the same currency that you used in your request for Payment API. 

        :return: The currency of this InlineResponse2013RefundAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this InlineResponse2013RefundAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes.  For an authorization reversal or a capture, you must use the same currency that you used in your request for Payment API. 

        :param currency: The currency of this InlineResponse2013RefundAmountDetails.
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
        if not isinstance(other, InlineResponse2013RefundAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
