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


class V2creditsPointOfSaleInformationEmv(object):
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
        'tags': 'str',
        'fallback': 'bool',
        'fallback_condition': 'float'
    }

    attribute_map = {
        'tags': 'tags',
        'fallback': 'fallback',
        'fallback_condition': 'fallbackCondition'
    }

    def __init__(self, tags=None, fallback=False, fallback_condition=None):
        """
        V2creditsPointOfSaleInformationEmv - a model defined in Swagger
        """

        self._tags = None
        self._fallback = None
        self._fallback_condition = None

        if tags is not None:
          self.tags = tags
        if fallback is not None:
          self.fallback = fallback
        if fallback_condition is not None:
          self.fallback_condition = fallback_condition

    @property
    def tags(self):
        """
        Gets the tags of this V2creditsPointOfSaleInformationEmv.
        EMV data that is transmitted from the chip card to the issuer, and from the issuer to the chip card. The EMV data is in the tag-length-value format and includes chip card tags, terminal tags, and transaction detail tags.  `Important` The following tags contain sensitive information and **must not** be included in this field:   - **56**: Track 1 equivalent data  - **57**: Track 2 equivalent data  - **5A**: Application PAN  - **5F20**: Cardholder name  - **5F24**: Application expiration date (This sensitivity has been relaxed for cmcic, amexdirect, fdiglobal, opdfde, six)  - **99**: Transaction PIN  - **9F0B**: Cardholder name (extended)  - **9F1F**: Track 1 discretionary data  - **9F20**: Track 2 discretionary data  For captures, this field is required for contact EMV transactions. Otherwise, it is optional.  For credits, this field is required for contact EMV stand-alone credits and contactless EMV stand-alone credits. Otherwise, it is optional.  `Important` For contact EMV captures, contact EMV stand-alone credits, and contactless EMV stand-alone credits, you must include the following tags in this field. For all other types of EMV transactions, the following tags are optional.   - **95**: Terminal verification results  - **9F10**: Issuer application data  - **9F26**: Application cryptogram 

        :return: The tags of this V2creditsPointOfSaleInformationEmv.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this V2creditsPointOfSaleInformationEmv.
        EMV data that is transmitted from the chip card to the issuer, and from the issuer to the chip card. The EMV data is in the tag-length-value format and includes chip card tags, terminal tags, and transaction detail tags.  `Important` The following tags contain sensitive information and **must not** be included in this field:   - **56**: Track 1 equivalent data  - **57**: Track 2 equivalent data  - **5A**: Application PAN  - **5F20**: Cardholder name  - **5F24**: Application expiration date (This sensitivity has been relaxed for cmcic, amexdirect, fdiglobal, opdfde, six)  - **99**: Transaction PIN  - **9F0B**: Cardholder name (extended)  - **9F1F**: Track 1 discretionary data  - **9F20**: Track 2 discretionary data  For captures, this field is required for contact EMV transactions. Otherwise, it is optional.  For credits, this field is required for contact EMV stand-alone credits and contactless EMV stand-alone credits. Otherwise, it is optional.  `Important` For contact EMV captures, contact EMV stand-alone credits, and contactless EMV stand-alone credits, you must include the following tags in this field. For all other types of EMV transactions, the following tags are optional.   - **95**: Terminal verification results  - **9F10**: Issuer application data  - **9F26**: Application cryptogram 

        :param tags: The tags of this V2creditsPointOfSaleInformationEmv.
        :type: str
        """
        if tags is not None and len(tags) > 1998:
            raise ValueError("Invalid value for `tags`, length must be less than or equal to `1998`")

        self._tags = tags

    @property
    def fallback(self):
        """
        Gets the fallback of this V2creditsPointOfSaleInformationEmv.
        Indicates whether a fallback method was used to enter credit card information into the POS terminal. When a technical problem prevents a successful exchange of information between a chip card and a chip-capable terminal:   1. Swipe the card or key the credit card information into the POS terminal.  2. Use the pos_entry_mode field to indicate whether the information was swiped or keyed.  This field is supported only on **Chase Paymentech Solutions** and **GPN**. 

        :return: The fallback of this V2creditsPointOfSaleInformationEmv.
        :rtype: bool
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """
        Sets the fallback of this V2creditsPointOfSaleInformationEmv.
        Indicates whether a fallback method was used to enter credit card information into the POS terminal. When a technical problem prevents a successful exchange of information between a chip card and a chip-capable terminal:   1. Swipe the card or key the credit card information into the POS terminal.  2. Use the pos_entry_mode field to indicate whether the information was swiped or keyed.  This field is supported only on **Chase Paymentech Solutions** and **GPN**. 

        :param fallback: The fallback of this V2creditsPointOfSaleInformationEmv.
        :type: bool
        """

        self._fallback = fallback

    @property
    def fallback_condition(self):
        """
        Gets the fallback_condition of this V2creditsPointOfSaleInformationEmv.
        Reason for the EMV fallback transaction. An EMV fallback transaction occurs when an EMV transaction fails for one of these reasons:   - Technical failure: the EMV terminal or EMV card cannot read and process chip data.  - Empty candidate list failure: the EMV terminal does not have any applications in common with the EMV card.    EMV terminals are coded to determine whether the terminal and EMV card have any applications in common.    EMV terminals provide this information to you.  Possible values:   - **1**: Transaction was initiated with information from a magnetic stripe, and the previous transaction at the       EMV terminal either used information from a successful chip read or it was not a chip transaction.  - **2**: Transaction was initiated with information from a magnetic stripe, and the previous transaction at the       EMV terminal was an EMV fallback transaction because the attempted chip read was unsuccessful.  This field is supported only on **GPN**. 

        :return: The fallback_condition of this V2creditsPointOfSaleInformationEmv.
        :rtype: float
        """
        return self._fallback_condition

    @fallback_condition.setter
    def fallback_condition(self, fallback_condition):
        """
        Sets the fallback_condition of this V2creditsPointOfSaleInformationEmv.
        Reason for the EMV fallback transaction. An EMV fallback transaction occurs when an EMV transaction fails for one of these reasons:   - Technical failure: the EMV terminal or EMV card cannot read and process chip data.  - Empty candidate list failure: the EMV terminal does not have any applications in common with the EMV card.    EMV terminals are coded to determine whether the terminal and EMV card have any applications in common.    EMV terminals provide this information to you.  Possible values:   - **1**: Transaction was initiated with information from a magnetic stripe, and the previous transaction at the       EMV terminal either used information from a successful chip read or it was not a chip transaction.  - **2**: Transaction was initiated with information from a magnetic stripe, and the previous transaction at the       EMV terminal was an EMV fallback transaction because the attempted chip read was unsuccessful.  This field is supported only on **GPN**. 

        :param fallback_condition: The fallback_condition of this V2creditsPointOfSaleInformationEmv.
        :type: float
        """

        self._fallback_condition = fallback_condition

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
        if not isinstance(other, V2creditsPointOfSaleInformationEmv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
