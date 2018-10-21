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


class V2paymentsBuyerInformation(object):
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
        'merchant_customer_id': 'str',
        'date_of_birth': 'str',
        'vat_registration_number': 'str',
        'personal_identification': 'list[V2paymentsBuyerInformationPersonalIdentification]',
        'hashed_password': 'str'
    }

    attribute_map = {
        'merchant_customer_id': 'merchantCustomerId',
        'date_of_birth': 'dateOfBirth',
        'vat_registration_number': 'vatRegistrationNumber',
        'personal_identification': 'personalIdentification',
        'hashed_password': 'hashedPassword'
    }

    def __init__(self, merchant_customer_id=None, date_of_birth=None, vat_registration_number=None, personal_identification=None, hashed_password=None):
        """
        V2paymentsBuyerInformation - a model defined in Swagger
        """

        self._merchant_customer_id = None
        self._date_of_birth = None
        self._vat_registration_number = None
        self._personal_identification = None
        self._hashed_password = None

        if merchant_customer_id is not None:
          self.merchant_customer_id = merchant_customer_id
        if date_of_birth is not None:
          self.date_of_birth = date_of_birth
        if vat_registration_number is not None:
          self.vat_registration_number = vat_registration_number
        if personal_identification is not None:
          self.personal_identification = personal_identification
        if hashed_password is not None:
          self.hashed_password = hashed_password

    @property
    def merchant_customer_id(self):
        """
        Gets the merchant_customer_id of this V2paymentsBuyerInformation.
        Your identifier for the customer.  For processor-specific information, see the customer_account_id field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The merchant_customer_id of this V2paymentsBuyerInformation.
        :rtype: str
        """
        return self._merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, merchant_customer_id):
        """
        Sets the merchant_customer_id of this V2paymentsBuyerInformation.
        Your identifier for the customer.  For processor-specific information, see the customer_account_id field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param merchant_customer_id: The merchant_customer_id of this V2paymentsBuyerInformation.
        :type: str
        """
        if merchant_customer_id is not None and len(merchant_customer_id) > 100:
            raise ValueError("Invalid value for `merchant_customer_id`, length must be less than or equal to `100`")

        self._merchant_customer_id = merchant_customer_id

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this V2paymentsBuyerInformation.
        Recipientâ€™s date of birth. **Format**: `YYYYMMDD`.  This field is a pass-through, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor. 

        :return: The date_of_birth of this V2paymentsBuyerInformation.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this V2paymentsBuyerInformation.
        Recipientâ€™s date of birth. **Format**: `YYYYMMDD`.  This field is a pass-through, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor. 

        :param date_of_birth: The date_of_birth of this V2paymentsBuyerInformation.
        :type: str
        """
        if date_of_birth is not None and len(date_of_birth) > 8:
            raise ValueError("Invalid value for `date_of_birth`, length must be less than or equal to `8`")

        self._date_of_birth = date_of_birth

    @property
    def vat_registration_number(self):
        """
        Gets the vat_registration_number of this V2paymentsBuyerInformation.
        Customerâ€™s government-assigned tax identification number.  For processor-specific information, see the purchaser_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The vat_registration_number of this V2paymentsBuyerInformation.
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """
        Sets the vat_registration_number of this V2paymentsBuyerInformation.
        Customerâ€™s government-assigned tax identification number.  For processor-specific information, see the purchaser_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param vat_registration_number: The vat_registration_number of this V2paymentsBuyerInformation.
        :type: str
        """
        if vat_registration_number is not None and len(vat_registration_number) > 20:
            raise ValueError("Invalid value for `vat_registration_number`, length must be less than or equal to `20`")

        self._vat_registration_number = vat_registration_number

    @property
    def personal_identification(self):
        """
        Gets the personal_identification of this V2paymentsBuyerInformation.

        :return: The personal_identification of this V2paymentsBuyerInformation.
        :rtype: list[V2paymentsBuyerInformationPersonalIdentification]
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """
        Sets the personal_identification of this V2paymentsBuyerInformation.

        :param personal_identification: The personal_identification of this V2paymentsBuyerInformation.
        :type: list[V2paymentsBuyerInformationPersonalIdentification]
        """

        self._personal_identification = personal_identification

    @property
    def hashed_password(self):
        """
        Gets the hashed_password of this V2paymentsBuyerInformation.
        TODO 

        :return: The hashed_password of this V2paymentsBuyerInformation.
        :rtype: str
        """
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, hashed_password):
        """
        Sets the hashed_password of this V2paymentsBuyerInformation.
        TODO 

        :param hashed_password: The hashed_password of this V2paymentsBuyerInformation.
        :type: str
        """
        if hashed_password is not None and len(hashed_password) > 100:
            raise ValueError("Invalid value for `hashed_password`, length must be less than or equal to `100`")

        self._hashed_password = hashed_password

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
        if not isinstance(other, V2paymentsBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
