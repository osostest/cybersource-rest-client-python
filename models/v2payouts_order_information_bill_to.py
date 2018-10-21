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


class V2payoutsOrderInformationBillTo(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'address1': 'str',
        'address2': 'str',
        'country': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'phone_number': 'str',
        'phone_type': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'address1': 'address1',
        'address2': 'address2',
        'country': 'country',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'phone_number': 'phoneNumber',
        'phone_type': 'phoneType'
    }

    def __init__(self, first_name=None, last_name=None, address1=None, address2=None, country=None, locality=None, administrative_area=None, postal_code=None, phone_number=None, phone_type=None):
        """
        V2payoutsOrderInformationBillTo - a model defined in Swagger
        """

        self._first_name = None
        self._last_name = None
        self._address1 = None
        self._address2 = None
        self._country = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._phone_number = None
        self._phone_type = None

        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if country is not None:
          self.country = country
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if phone_number is not None:
          self.phone_number = phone_number
        if phone_type is not None:
          self.phone_type = phone_type

    @property
    def first_name(self):
        """
        Gets the first_name of this V2payoutsOrderInformationBillTo.
        Customerâ€™s first name. This name must be the same as the name on the card.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the customer_firstname field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The first_name of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this V2payoutsOrderInformationBillTo.
        Customerâ€™s first name. This name must be the same as the name on the card.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the customer_firstname field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param first_name: The first_name of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if first_name is not None and len(first_name) > 60:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `60`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this V2payoutsOrderInformationBillTo.
        Customerâ€™s last name. This name must be the same as the name on the card.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the customer_lastname field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The last_name of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this V2payoutsOrderInformationBillTo.
        Customerâ€™s last name. This name must be the same as the name on the card.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the customer_lastname field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param last_name: The last_name of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if last_name is not None and len(last_name) > 60:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `60`")

        self._last_name = last_name

    @property
    def address1(self):
        """
        Gets the address1 of this V2payoutsOrderInformationBillTo.
        First line of the billing street address as it appears on the credit card issuerâ€™s records.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_address1 field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The address1 of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this V2payoutsOrderInformationBillTo.
        First line of the billing street address as it appears on the credit card issuerâ€™s records.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_address1 field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param address1: The address1 of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if address1 is not None and len(address1) > 60:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `60`")

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this V2payoutsOrderInformationBillTo.
        Additional address information.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_address2 field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The address2 of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this V2payoutsOrderInformationBillTo.
        Additional address information.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_address2 field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param address2: The address2 of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if address2 is not None and len(address2) > 60:
            raise ValueError("Invalid value for `address2`, length must be less than or equal to `60`")

        self._address2 = address2

    @property
    def country(self):
        """
        Gets the country of this V2payoutsOrderInformationBillTo.
        Country of the billing address. Use the two-character ISO Standard Country Codes.  For processor-specific information, see the bill_country field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The country of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this V2payoutsOrderInformationBillTo.
        Country of the billing address. Use the two-character ISO Standard Country Codes.  For processor-specific information, see the bill_country field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param country: The country of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")

        self._country = country

    @property
    def locality(self):
        """
        Gets the locality of this V2payoutsOrderInformationBillTo.
        City of the billing address.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_city field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The locality of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this V2payoutsOrderInformationBillTo.
        City of the billing address.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_city field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param locality: The locality of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if locality is not None and len(locality) > 50:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `50`")

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this V2payoutsOrderInformationBillTo.
        State or province of the billing address. Use the State, Province, and Territory Codes for the United States and Canada.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_state field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The administrative_area of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this V2payoutsOrderInformationBillTo.
        State or province of the billing address. Use the State, Province, and Territory Codes for the United States and Canada.  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_state field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param administrative_area: The administrative_area of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 2:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `2`")

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this V2payoutsOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_zip field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The postal_code of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this V2payoutsOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  For Payouts: This field may be sent only for FDC Compass.  For processor-specific information, see the bill_zip field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param postal_code: The postal_code of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 10:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `10`")

        self._postal_code = postal_code

    @property
    def phone_number(self):
        """
        Gets the phone_number of this V2payoutsOrderInformationBillTo.
        Customerâ€™s phone number.  For Payouts: This field may be sent only for FDC Compass.  CyberSource recommends that you include the country code when the order is from outside the U.S.  For processor-specific information, see the customer_phone field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The phone_number of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this V2payoutsOrderInformationBillTo.
        Customerâ€™s phone number.  For Payouts: This field may be sent only for FDC Compass.  CyberSource recommends that you include the country code when the order is from outside the U.S.  For processor-specific information, see the customer_phone field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param phone_number: The phone_number of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 15:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `15`")

        self._phone_number = phone_number

    @property
    def phone_type(self):
        """
        Gets the phone_type of this V2payoutsOrderInformationBillTo.
        Customer's phone number type.  For Payouts: This field may be sent only for FDC Compass.  Possible Values -  * day * home * night * work 

        :return: The phone_type of this V2payoutsOrderInformationBillTo.
        :rtype: str
        """
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        """
        Sets the phone_type of this V2payoutsOrderInformationBillTo.
        Customer's phone number type.  For Payouts: This field may be sent only for FDC Compass.  Possible Values -  * day * home * night * work 

        :param phone_type: The phone_type of this V2payoutsOrderInformationBillTo.
        :type: str
        """
        allowed_values = ["day", "home", "night", "work"]
        if phone_type not in allowed_values:
            raise ValueError(
                "Invalid value for `phone_type` ({0}), must be one of {1}"
                .format(phone_type, allowed_values)
            )

        self._phone_type = phone_type

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
        if not isinstance(other, V2payoutsOrderInformationBillTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
