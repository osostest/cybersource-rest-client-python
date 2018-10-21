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


class V2paymentsPaymentInformationCard(object):
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
        'number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'use_as': 'str',
        'source_account_type': 'str',
        'security_code': 'str',
        'security_code_indicator': 'str',
        'account_encoder_id': 'str',
        'issue_number': 'str',
        'start_month': 'str',
        'start_year': 'str'
    }

    attribute_map = {
        'number': 'number',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'use_as': 'useAs',
        'source_account_type': 'sourceAccountType',
        'security_code': 'securityCode',
        'security_code_indicator': 'securityCodeIndicator',
        'account_encoder_id': 'accountEncoderId',
        'issue_number': 'issueNumber',
        'start_month': 'startMonth',
        'start_year': 'startYear'
    }

    def __init__(self, number=None, expiration_month=None, expiration_year=None, type=None, use_as=None, source_account_type=None, security_code=None, security_code_indicator=None, account_encoder_id=None, issue_number=None, start_month=None, start_year=None):
        """
        V2paymentsPaymentInformationCard - a model defined in Swagger
        """

        self._number = None
        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._use_as = None
        self._source_account_type = None
        self._security_code = None
        self._security_code_indicator = None
        self._account_encoder_id = None
        self._issue_number = None
        self._start_month = None
        self._start_year = None

        if number is not None:
          self.number = number
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if type is not None:
          self.type = type
        if use_as is not None:
          self.use_as = use_as
        if source_account_type is not None:
          self.source_account_type = source_account_type
        if security_code is not None:
          self.security_code = security_code
        if security_code_indicator is not None:
          self.security_code_indicator = security_code_indicator
        if account_encoder_id is not None:
          self.account_encoder_id = account_encoder_id
        if issue_number is not None:
          self.issue_number = issue_number
        if start_month is not None:
          self.start_month = start_month
        if start_year is not None:
          self.start_year = start_year

    @property
    def number(self):
        """
        Gets the number of this V2paymentsPaymentInformationCard.
        Customerâ€™s credit card number. Encoded Account Numbers when processing encoded account numbers, use this field for the encoded account number.  For processor-specific information, see the customer_cc_number field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The number of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this V2paymentsPaymentInformationCard.
        Customerâ€™s credit card number. Encoded Account Numbers when processing encoded account numbers, use this field for the encoded account number.  For processor-specific information, see the customer_cc_number field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param number: The number of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if number is not None and len(number) > 20:
            raise ValueError("Invalid value for `number`, length must be less than or equal to `20`")

        self._number = number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this V2paymentsPaymentInformationCard.
        Two-digit month in which the credit card expires. `Format: MM`. Possible values: 01 through 12.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 12.  For processor-specific information, see the customer_cc_expmo field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_month of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this V2paymentsPaymentInformationCard.
        Two-digit month in which the credit card expires. `Format: MM`. Possible values: 01 through 12.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 12.  For processor-specific information, see the customer_cc_expmo field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_month: The expiration_month of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this V2paymentsPaymentInformationCard.
        Four-digit year in which the credit card expires. `Format: YYYY`.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 2021.  For processor-specific information, see the customer_cc_expyr field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_year of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this V2paymentsPaymentInformationCard.
        Four-digit year in which the credit card expires. `Format: YYYY`.  **Encoded Account Numbers**  For encoded account numbers (_type_=039), if there is no expiration date on the card, use 2021.  For processor-specific information, see the customer_cc_expyr field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_year: The expiration_year of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this V2paymentsPaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :return: The type of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V2paymentsPaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :param type: The type of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if type is not None and len(type) > 3:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `3`")

        self._type = type

    @property
    def use_as(self):
        """
        Gets the use_as of this V2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process.  **Cielo** and **Comercio Latino**  Possible values:   - CREDIT: Credit card  - DEBIT: Debit card  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet. 

        :return: The use_as of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._use_as

    @use_as.setter
    def use_as(self, use_as):
        """
        Sets the use_as of this V2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process.  **Cielo** and **Comercio Latino**  Possible values:   - CREDIT: Credit card  - DEBIT: Debit card  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet. 

        :param use_as: The use_as of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if use_as is not None and len(use_as) > 2:
            raise ValueError("Invalid value for `use_as`, length must be less than or equal to `2`")

        self._use_as = use_as

    @property
    def source_account_type(self):
        """
        Gets the source_account_type of this V2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process. This field is required in the following cases.   - Debit transactions on Cielo and Comercio Latino.   - Transactions with Brazilian-issued cards on CyberSource through VisaNet.   - Applicable only for CTV.      **Note** Combo cards in Brazil contain credit and debit functionality in a single card. Visa systems use a credit bank identification number (BIN) for this type of card. Using the BIN to determine whether a card is debit or credit can cause transactions with these cards to be processed incorrectly. CyberSource strongly recommends that you include this field for combo card transactions.  Possible values include the following.   - CHECKING: Checking account  - CREDIT: Credit card account  - SAVING: Saving account  - LINE_OF_CREDIT: Line of credit  - PREPAID: Prepaid card account  - UNIVERSAL: Universal account 

        :return: The source_account_type of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._source_account_type

    @source_account_type.setter
    def source_account_type(self, source_account_type):
        """
        Sets the source_account_type of this V2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card. The cardholder provides this information during the payment process. This field is required in the following cases.   - Debit transactions on Cielo and Comercio Latino.   - Transactions with Brazilian-issued cards on CyberSource through VisaNet.   - Applicable only for CTV.      **Note** Combo cards in Brazil contain credit and debit functionality in a single card. Visa systems use a credit bank identification number (BIN) for this type of card. Using the BIN to determine whether a card is debit or credit can cause transactions with these cards to be processed incorrectly. CyberSource strongly recommends that you include this field for combo card transactions.  Possible values include the following.   - CHECKING: Checking account  - CREDIT: Credit card account  - SAVING: Saving account  - LINE_OF_CREDIT: Line of credit  - PREPAID: Prepaid card account  - UNIVERSAL: Universal account 

        :param source_account_type: The source_account_type of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if source_account_type is not None and len(source_account_type) > 2:
            raise ValueError("Invalid value for `source_account_type`, length must be less than or equal to `2`")

        self._source_account_type = source_account_type

    @property
    def security_code(self):
        """
        Gets the security_code of this V2paymentsPaymentInformationCard.
        Card Verification Number.

        :return: The security_code of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """
        Sets the security_code of this V2paymentsPaymentInformationCard.
        Card Verification Number.

        :param security_code: The security_code of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if security_code is not None and len(security_code) > 4:
            raise ValueError("Invalid value for `security_code`, length must be less than or equal to `4`")

        self._security_code = security_code

    @property
    def security_code_indicator(self):
        """
        Gets the security_code_indicator of this V2paymentsPaymentInformationCard.
        Flag that indicates whether a CVN code was sent. Possible values:   - 0 (default): CVN service not requested. CyberSource uses this default value when you do not include      _securityCode_ in the request.  - 1 (default): CVN service requested and supported. CyberSource uses this default value when you include      _securityCode_ in the request.  - 2: CVN on credit card is illegible.  - 9: CVN was not imprinted on credit card. 

        :return: The security_code_indicator of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._security_code_indicator

    @security_code_indicator.setter
    def security_code_indicator(self, security_code_indicator):
        """
        Sets the security_code_indicator of this V2paymentsPaymentInformationCard.
        Flag that indicates whether a CVN code was sent. Possible values:   - 0 (default): CVN service not requested. CyberSource uses this default value when you do not include      _securityCode_ in the request.  - 1 (default): CVN service requested and supported. CyberSource uses this default value when you include      _securityCode_ in the request.  - 2: CVN on credit card is illegible.  - 9: CVN was not imprinted on credit card. 

        :param security_code_indicator: The security_code_indicator of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if security_code_indicator is not None and len(security_code_indicator) > 1:
            raise ValueError("Invalid value for `security_code_indicator`, length must be less than or equal to `1`")

        self._security_code_indicator = security_code_indicator

    @property
    def account_encoder_id(self):
        """
        Gets the account_encoder_id of this V2paymentsPaymentInformationCard.
        Identifier for the issuing bank that provided the customerâ€™s encoded account number. Contact your processor for the bankâ€™s ID. 

        :return: The account_encoder_id of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._account_encoder_id

    @account_encoder_id.setter
    def account_encoder_id(self, account_encoder_id):
        """
        Sets the account_encoder_id of this V2paymentsPaymentInformationCard.
        Identifier for the issuing bank that provided the customerâ€™s encoded account number. Contact your processor for the bankâ€™s ID. 

        :param account_encoder_id: The account_encoder_id of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if account_encoder_id is not None and len(account_encoder_id) > 3:
            raise ValueError("Invalid value for `account_encoder_id`, length must be less than or equal to `3`")

        self._account_encoder_id = account_encoder_id

    @property
    def issue_number(self):
        """
        Gets the issue_number of this V2paymentsPaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  The issue number is not required for Maestro (UK Domestic) transactions. 

        :return: The issue_number of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """
        Sets the issue_number of this V2paymentsPaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  The issue number is not required for Maestro (UK Domestic) transactions. 

        :param issue_number: The issue_number of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if issue_number is not None and len(issue_number) > 5:
            raise ValueError("Invalid value for `issue_number`, length must be less than or equal to `5`")

        self._issue_number = issue_number

    @property
    def start_month(self):
        """
        Gets the start_month of this V2paymentsPaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_month of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """
        Sets the start_month of this V2paymentsPaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_month: The start_month of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if start_month is not None and len(start_month) > 2:
            raise ValueError("Invalid value for `start_month`, length must be less than or equal to `2`")

        self._start_month = start_month

    @property
    def start_year(self):
        """
        Gets the start_year of this V2paymentsPaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_year of this V2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this V2paymentsPaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_year: The start_year of this V2paymentsPaymentInformationCard.
        :type: str
        """
        if start_year is not None and len(start_year) > 4:
            raise ValueError("Invalid value for `start_year`, length must be less than or equal to `4`")

        self._start_year = start_year

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
        if not isinstance(other, V2paymentsPaymentInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
