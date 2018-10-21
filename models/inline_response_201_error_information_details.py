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


class InlineResponse201ErrorInformationDetails(object):
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
        'field': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'field': 'field',
        'reason': 'reason'
    }

    def __init__(self, field=None, reason=None):
        """
        InlineResponse201ErrorInformationDetails - a model defined in Swagger
        """

        self._field = None
        self._reason = None

        if field is not None:
          self.field = field
        if reason is not None:
          self.reason = reason

    @property
    def field(self):
        """
        Gets the field of this InlineResponse201ErrorInformationDetails.
        This is the flattened JSON object field name/path that is either missing or invalid.

        :return: The field of this InlineResponse201ErrorInformationDetails.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this InlineResponse201ErrorInformationDetails.
        This is the flattened JSON object field name/path that is either missing or invalid.

        :param field: The field of this InlineResponse201ErrorInformationDetails.
        :type: str
        """

        self._field = field

    @property
    def reason(self):
        """
        Gets the reason of this InlineResponse201ErrorInformationDetails.
        Possible reasons for the error. 

        :return: The reason of this InlineResponse201ErrorInformationDetails.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this InlineResponse201ErrorInformationDetails.
        Possible reasons for the error. 

        :param reason: The reason of this InlineResponse201ErrorInformationDetails.
        :type: str
        """
        allowed_values = ["MISSING_FIELD", "INVALID_DATA"]
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"
                .format(reason, allowed_values)
            )

        self._reason = reason

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
        if not isinstance(other, InlineResponse201ErrorInformationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
