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


class InlineResponse200(object):
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
        'key_id': 'str',
        'der': 'InlineResponse200Der',
        'jwk': 'InlineResponse200Jwk'
    }

    attribute_map = {
        'key_id': 'keyId',
        'der': 'der',
        'jwk': 'jwk'
    }

    def __init__(self, key_id=None, der=None, jwk=None):
        """
        InlineResponse200 - a model defined in Swagger
        """

        self._key_id = None
        self._der = None
        self._jwk = None

        if key_id is not None:
          self.key_id = key_id
        if der is not None:
          self.der = der
        if jwk is not None:
          self.jwk = jwk

    @property
    def key_id(self):
        """
        Gets the key_id of this InlineResponse200.
        Unique identifier for the generated token. Used in the subsequent Tokenize Card request from your customer’s device or browser.

        :return: The key_id of this InlineResponse200.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this InlineResponse200.
        Unique identifier for the generated token. Used in the subsequent Tokenize Card request from your customer’s device or browser.

        :param key_id: The key_id of this InlineResponse200.
        :type: str
        """

        self._key_id = key_id

    @property
    def der(self):
        """
        Gets the der of this InlineResponse200.

        :return: The der of this InlineResponse200.
        :rtype: InlineResponse200Der
        """
        return self._der

    @der.setter
    def der(self, der):
        """
        Sets the der of this InlineResponse200.

        :param der: The der of this InlineResponse200.
        :type: InlineResponse200Der
        """

        self._der = der

    @property
    def jwk(self):
        """
        Gets the jwk of this InlineResponse200.

        :return: The jwk of this InlineResponse200.
        :rtype: InlineResponse200Jwk
        """
        return self._jwk

    @jwk.setter
    def jwk(self, jwk):
        """
        Sets the jwk of this InlineResponse200.

        :param jwk: The jwk of this InlineResponse200.
        :type: InlineResponse200Jwk
        """

        self._jwk = jwk

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
