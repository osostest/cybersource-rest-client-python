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


class V2paymentsidcapturesProcessingInformationAuthorizationOptions(object):
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
        'auth_type': 'str',
        'verbal_auth_code': 'str',
        'verbal_auth_transaction_id': 'str'
    }

    attribute_map = {
        'auth_type': 'authType',
        'verbal_auth_code': 'verbalAuthCode',
        'verbal_auth_transaction_id': 'verbalAuthTransactionId'
    }

    def __init__(self, auth_type=None, verbal_auth_code=None, verbal_auth_transaction_id=None):
        """
        V2paymentsidcapturesProcessingInformationAuthorizationOptions - a model defined in Swagger
        """

        self._auth_type = None
        self._verbal_auth_code = None
        self._verbal_auth_transaction_id = None

        if auth_type is not None:
          self.auth_type = auth_type
        if verbal_auth_code is not None:
          self.verbal_auth_code = verbal_auth_code
        if verbal_auth_transaction_id is not None:
          self.verbal_auth_transaction_id = verbal_auth_transaction_id

    @property
    def auth_type(self):
        """
        Gets the auth_type of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization type. Possible values:   - **AUTOCAPTURE**: automatic capture.  - **STANDARDCAPTURE**: standard capture.  - **VERBAL**: forced capture. Include it in the payment request for a forced capture. Include it in the capture  request for a verbal payment.  For processor-specific information, see the auth_type field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The auth_type of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """
        Sets the auth_type of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization type. Possible values:   - **AUTOCAPTURE**: automatic capture.  - **STANDARDCAPTURE**: standard capture.  - **VERBAL**: forced capture. Include it in the payment request for a forced capture. Include it in the capture  request for a verbal payment.  For processor-specific information, see the auth_type field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param auth_type: The auth_type of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :type: str
        """
        if auth_type is not None and len(auth_type) > 15:
            raise ValueError("Invalid value for `auth_type`, length must be less than or equal to `15`")

        self._auth_type = auth_type

    @property
    def verbal_auth_code(self):
        """
        Gets the verbal_auth_code of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization code.  **Forced Capture**  Use this field to send the authorization code you received from a payment that you authorized outside the CyberSource system.  **Verbal Authorization**  Use this field in CAPTURE API to send the verbally received authorization code.  For processor-specific information, see the auth_code field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The verbal_auth_code of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :rtype: str
        """
        return self._verbal_auth_code

    @verbal_auth_code.setter
    def verbal_auth_code(self, verbal_auth_code):
        """
        Sets the verbal_auth_code of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Authorization code.  **Forced Capture**  Use this field to send the authorization code you received from a payment that you authorized outside the CyberSource system.  **Verbal Authorization**  Use this field in CAPTURE API to send the verbally received authorization code.  For processor-specific information, see the auth_code field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param verbal_auth_code: The verbal_auth_code of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :type: str
        """
        if verbal_auth_code is not None and len(verbal_auth_code) > 7:
            raise ValueError("Invalid value for `verbal_auth_code`, length must be less than or equal to `7`")

        self._verbal_auth_code = verbal_auth_code

    @property
    def verbal_auth_transaction_id(self):
        """
        Gets the verbal_auth_transaction_id of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Transaction ID (TID).

        :return: The verbal_auth_transaction_id of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :rtype: str
        """
        return self._verbal_auth_transaction_id

    @verbal_auth_transaction_id.setter
    def verbal_auth_transaction_id(self, verbal_auth_transaction_id):
        """
        Sets the verbal_auth_transaction_id of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        Transaction ID (TID).

        :param verbal_auth_transaction_id: The verbal_auth_transaction_id of this V2paymentsidcapturesProcessingInformationAuthorizationOptions.
        :type: str
        """
        if verbal_auth_transaction_id is not None and len(verbal_auth_transaction_id) > 15:
            raise ValueError("Invalid value for `verbal_auth_transaction_id`, length must be less than or equal to `15`")

        self._verbal_auth_transaction_id = verbal_auth_transaction_id

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
        if not isinstance(other, V2paymentsidcapturesProcessingInformationAuthorizationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
