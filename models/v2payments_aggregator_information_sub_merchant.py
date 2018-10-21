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


class V2paymentsAggregatorInformationSubMerchant(object):
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
        'card_acceptor_id': 'str',
        'name': 'str',
        'address1': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'region': 'str',
        'postal_code': 'str',
        'country': 'str',
        'email': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'card_acceptor_id': 'cardAcceptorId',
        'name': 'name',
        'address1': 'address1',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'region': 'region',
        'postal_code': 'postalCode',
        'country': 'country',
        'email': 'email',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, card_acceptor_id=None, name=None, address1=None, locality=None, administrative_area=None, region=None, postal_code=None, country=None, email=None, phone_number=None):
        """
        V2paymentsAggregatorInformationSubMerchant - a model defined in Swagger
        """

        self._card_acceptor_id = None
        self._name = None
        self._address1 = None
        self._locality = None
        self._administrative_area = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._email = None
        self._phone_number = None

        if card_acceptor_id is not None:
          self.card_acceptor_id = card_acceptor_id
        if name is not None:
          self.name = name
        if address1 is not None:
          self.address1 = address1
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if region is not None:
          self.region = region
        if postal_code is not None:
          self.postal_code = postal_code
        if country is not None:
          self.country = country
        if email is not None:
          self.email = email
        if phone_number is not None:
          self.phone_number = phone_number

    @property
    def card_acceptor_id(self):
        """
        Gets the card_acceptor_id of this V2paymentsAggregatorInformationSubMerchant.
        Unique identifier assigned by the payment card company to the sub-merchant.

        :return: The card_acceptor_id of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._card_acceptor_id

    @card_acceptor_id.setter
    def card_acceptor_id(self, card_acceptor_id):
        """
        Sets the card_acceptor_id of this V2paymentsAggregatorInformationSubMerchant.
        Unique identifier assigned by the payment card company to the sub-merchant.

        :param card_acceptor_id: The card_acceptor_id of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if card_acceptor_id is not None and len(card_acceptor_id) > 15:
            raise ValueError("Invalid value for `card_acceptor_id`, length must be less than or equal to `15`")

        self._card_acceptor_id = card_acceptor_id

    @property
    def name(self):
        """
        Gets the name of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s business name.

        :return: The name of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s business name.

        :param name: The name of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if name is not None and len(name) > 37:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `37`")

        self._name = name

    @property
    def address1(self):
        """
        Gets the address1 of this V2paymentsAggregatorInformationSubMerchant.
        First line of the sub-merchantâ€™s street address.

        :return: The address1 of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this V2paymentsAggregatorInformationSubMerchant.
        First line of the sub-merchantâ€™s street address.

        :param address1: The address1 of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if address1 is not None and len(address1) > 38:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `38`")

        self._address1 = address1

    @property
    def locality(self):
        """
        Gets the locality of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s city.

        :return: The locality of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s city.

        :param locality: The locality of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if locality is not None and len(locality) > 21:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `21`")

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s state or province. Use the State, Province, and Territory Codes for the United States and Canada. 

        :return: The administrative_area of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s state or province. Use the State, Province, and Territory Codes for the United States and Canada. 

        :param administrative_area: The administrative_area of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 3:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `3`")

        self._administrative_area = administrative_area

    @property
    def region(self):
        """
        Gets the region of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s region. Example `NE` indicates that the sub-merchant is in the northeast region.

        :return: The region of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s region. Example `NE` indicates that the sub-merchant is in the northeast region.

        :param region: The region of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if region is not None and len(region) > 3:
            raise ValueError("Invalid value for `region`, length must be less than or equal to `3`")

        self._region = region

    @property
    def postal_code(self):
        """
        Gets the postal_code of this V2paymentsAggregatorInformationSubMerchant.
        Partial postal code for the sub-merchantâ€™s address.

        :return: The postal_code of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this V2paymentsAggregatorInformationSubMerchant.
        Partial postal code for the sub-merchantâ€™s address.

        :param postal_code: The postal_code of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 15:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `15`")

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s country. Use the two-character ISO Standard Country Codes.

        :return: The country of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s country. Use the two-character ISO Standard Country Codes.

        :param country: The country of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if country is not None and len(country) > 3:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `3`")

        self._country = country

    @property
    def email(self):
        """
        Gets the email of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s email address.  **Maximum length for processors**   - American Express Direct: 40  - CyberSource through VisaNet: 40  - FDC Compass: 40  - FDC Nashville Global: 19 

        :return: The email of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s email address.  **Maximum length for processors**   - American Express Direct: 40  - CyberSource through VisaNet: 40  - FDC Compass: 40  - FDC Nashville Global: 19 

        :param email: The email of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if email is not None and len(email) > 40:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `40`")

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s telephone number.  **Maximum length for procesors**   - American Express Direct: 20  - CyberSource through VisaNet: 20  - FDC Compass: 13  - FDC Nashville Global: 10 

        :return: The phone_number of this V2paymentsAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this V2paymentsAggregatorInformationSubMerchant.
        Sub-merchantâ€™s telephone number.  **Maximum length for procesors**   - American Express Direct: 20  - CyberSource through VisaNet: 20  - FDC Compass: 13  - FDC Nashville Global: 10 

        :param phone_number: The phone_number of this V2paymentsAggregatorInformationSubMerchant.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 20:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `20`")

        self._phone_number = phone_number

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
        if not isinstance(other, V2paymentsAggregatorInformationSubMerchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
