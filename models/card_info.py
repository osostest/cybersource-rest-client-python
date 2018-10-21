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


class CardInfo(object):
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
        'card_number': 'str',
        'card_expiration_month': 'str',
        'card_expiration_year': 'str',
        'card_type': 'str'
    }

    attribute_map = {
        'card_number': 'cardNumber',
        'card_expiration_month': 'cardExpirationMonth',
        'card_expiration_year': 'cardExpirationYear',
        'card_type': 'cardType'
    }

    def __init__(self, card_number=None, card_expiration_month=None, card_expiration_year=None, card_type=None):
        """
        CardInfo - a model defined in Swagger
        """

        self._card_number = None
        self._card_expiration_month = None
        self._card_expiration_year = None
        self._card_type = None

        if card_number is not None:
          self.card_number = card_number
        if card_expiration_month is not None:
          self.card_expiration_month = card_expiration_month
        if card_expiration_year is not None:
          self.card_expiration_year = card_expiration_year
        if card_type is not None:
          self.card_type = card_type

    @property
    def card_number(self):
        """
        Gets the card_number of this CardInfo.
        Encrypted or plain text card number. If the encryption type of “None” was used in the Generate Key request, this value can be set to the plaintext card number/Personal Account Number (PAN). If the encryption type of RsaOaep256 was used in the Generate Key request, this value needs to be the RSA OAEP 256 encrypted card number. The card number should be encrypted on the cardholders’ device. The [WebCrypto API] (https://github.com/CyberSource/cybersource-flex-samples/blob/master/java/spring-boot/src/main/resources/public/flex.js) can be used with the JWK obtained in the Generate Key request.

        :return: The card_number of this CardInfo.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """
        Sets the card_number of this CardInfo.
        Encrypted or plain text card number. If the encryption type of “None” was used in the Generate Key request, this value can be set to the plaintext card number/Personal Account Number (PAN). If the encryption type of RsaOaep256 was used in the Generate Key request, this value needs to be the RSA OAEP 256 encrypted card number. The card number should be encrypted on the cardholders’ device. The [WebCrypto API] (https://github.com/CyberSource/cybersource-flex-samples/blob/master/java/spring-boot/src/main/resources/public/flex.js) can be used with the JWK obtained in the Generate Key request.

        :param card_number: The card_number of this CardInfo.
        :type: str
        """

        self._card_number = card_number

    @property
    def card_expiration_month(self):
        """
        Gets the card_expiration_month of this CardInfo.
        Two digit expiration month

        :return: The card_expiration_month of this CardInfo.
        :rtype: str
        """
        return self._card_expiration_month

    @card_expiration_month.setter
    def card_expiration_month(self, card_expiration_month):
        """
        Sets the card_expiration_month of this CardInfo.
        Two digit expiration month

        :param card_expiration_month: The card_expiration_month of this CardInfo.
        :type: str
        """

        self._card_expiration_month = card_expiration_month

    @property
    def card_expiration_year(self):
        """
        Gets the card_expiration_year of this CardInfo.
        Four digit expiration year

        :return: The card_expiration_year of this CardInfo.
        :rtype: str
        """
        return self._card_expiration_year

    @card_expiration_year.setter
    def card_expiration_year(self, card_expiration_year):
        """
        Sets the card_expiration_year of this CardInfo.
        Four digit expiration year

        :param card_expiration_year: The card_expiration_year of this CardInfo.
        :type: str
        """

        self._card_expiration_year = card_expiration_year

    @property
    def card_type(self):
        """
        Gets the card_type of this CardInfo.
        Card Type. This field is required. Refer to the CyberSource Credit Card Services documentation for supported card types.

        :return: The card_type of this CardInfo.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this CardInfo.
        Card Type. This field is required. Refer to the CyberSource Credit Card Services documentation for supported card types.

        :param card_type: The card_type of this CardInfo.
        :type: str
        """

        self._card_type = card_type

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
        if not isinstance(other, CardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
