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


class InlineResponse2007(object):
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
        'links': 'InstrumentidentifiersLinks',
        'id': 'str',
        'object': 'str',
        'state': 'str',
        'card': 'InstrumentidentifiersCard',
        'bank_account': 'InstrumentidentifiersBankAccount',
        'processing_information': 'InstrumentidentifiersProcessingInformation',
        'metadata': 'InstrumentidentifiersMetadata'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'object': 'object',
        'state': 'state',
        'card': 'card',
        'bank_account': 'bankAccount',
        'processing_information': 'processingInformation',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, id=None, object=None, state=None, card=None, bank_account=None, processing_information=None, metadata=None):
        """
        InlineResponse2007 - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._object = None
        self._state = None
        self._card = None
        self._bank_account = None
        self._processing_information = None
        self._metadata = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if object is not None:
          self.object = object
        if state is not None:
          self.state = state
        if card is not None:
          self.card = card
        if bank_account is not None:
          self.bank_account = bank_account
        if processing_information is not None:
          self.processing_information = processing_information
        if metadata is not None:
          self.metadata = metadata

    @property
    def links(self):
        """
        Gets the links of this InlineResponse2007.

        :return: The links of this InlineResponse2007.
        :rtype: InstrumentidentifiersLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse2007.

        :param links: The links of this InlineResponse2007.
        :type: InstrumentidentifiersLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this InlineResponse2007.
        Unique identification number assigned by CyberSource to the submitted request.

        :return: The id of this InlineResponse2007.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse2007.
        Unique identification number assigned by CyberSource to the submitted request.

        :param id: The id of this InlineResponse2007.
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """
        Gets the object of this InlineResponse2007.
        Describes type of token. For example: customer, paymentInstrument or instrumentIdentifier.

        :return: The object of this InlineResponse2007.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this InlineResponse2007.
        Describes type of token. For example: customer, paymentInstrument or instrumentIdentifier.

        :param object: The object of this InlineResponse2007.
        :type: str
        """
        allowed_values = ["instrumentIdentifier"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def state(self):
        """
        Gets the state of this InlineResponse2007.
        Current state of the token.

        :return: The state of this InlineResponse2007.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this InlineResponse2007.
        Current state of the token.

        :param state: The state of this InlineResponse2007.
        :type: str
        """
        allowed_values = ["ACTIVE", "CLOSED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def card(self):
        """
        Gets the card of this InlineResponse2007.

        :return: The card of this InlineResponse2007.
        :rtype: InstrumentidentifiersCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this InlineResponse2007.

        :param card: The card of this InlineResponse2007.
        :type: InstrumentidentifiersCard
        """

        self._card = card

    @property
    def bank_account(self):
        """
        Gets the bank_account of this InlineResponse2007.

        :return: The bank_account of this InlineResponse2007.
        :rtype: InstrumentidentifiersBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this InlineResponse2007.

        :param bank_account: The bank_account of this InlineResponse2007.
        :type: InstrumentidentifiersBankAccount
        """

        self._bank_account = bank_account

    @property
    def processing_information(self):
        """
        Gets the processing_information of this InlineResponse2007.

        :return: The processing_information of this InlineResponse2007.
        :rtype: InstrumentidentifiersProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this InlineResponse2007.

        :param processing_information: The processing_information of this InlineResponse2007.
        :type: InstrumentidentifiersProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def metadata(self):
        """
        Gets the metadata of this InlineResponse2007.

        :return: The metadata of this InlineResponse2007.
        :rtype: InstrumentidentifiersMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this InlineResponse2007.

        :param metadata: The metadata of this InlineResponse2007.
        :type: InstrumentidentifiersMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
