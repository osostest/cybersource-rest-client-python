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


class InlineResponse2005(object):
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
        'links': 'InlineResponse2013Links',
        'id': 'str',
        'submit_time_utc': 'str',
        'status': 'str',
        'reconciliation_id': 'str',
        'client_reference_information': 'InlineResponse201ClientReferenceInformation',
        'refund_amount_details': 'InlineResponse2013RefundAmountDetails'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'reconciliation_id': 'reconciliationId',
        'client_reference_information': 'clientReferenceInformation',
        'refund_amount_details': 'refundAmountDetails'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, status=None, reconciliation_id=None, client_reference_information=None, refund_amount_details=None):
        """
        InlineResponse2005 - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._reconciliation_id = None
        self._client_reference_information = None
        self._refund_amount_details = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if refund_amount_details is not None:
          self.refund_amount_details = refund_amount_details

    @property
    def links(self):
        """
        Gets the links of this InlineResponse2005.

        :return: The links of this InlineResponse2005.
        :rtype: InlineResponse2013Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse2005.

        :param links: The links of this InlineResponse2005.
        :type: InlineResponse2013Links
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this InlineResponse2005.
        An unique identification number assigned by CyberSource to identify the submitted request.

        :return: The id of this InlineResponse2005.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse2005.
        An unique identification number assigned by CyberSource to identify the submitted request.

        :param id: The id of this InlineResponse2005.
        :type: str
        """
        if id is not None and len(id) > 26:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `26`")

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InlineResponse2005.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :return: The submit_time_utc of this InlineResponse2005.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InlineResponse2005.
        Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this InlineResponse2005.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2005.
        The status of the submitted transaction.

        :return: The status of this InlineResponse2005.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2005.
        The status of the submitted transaction.

        :param status: The status of this InlineResponse2005.
        :type: str
        """
        allowed_values = ["PENDING", "TRANSMITTED", "BATCH_ERROR", "VOIDED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this InlineResponse2005.
        The reconciliation id for the submitted transaction. This value is not returned for all processors. 

        :return: The reconciliation_id of this InlineResponse2005.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this InlineResponse2005.
        The reconciliation id for the submitted transaction. This value is not returned for all processors. 

        :param reconciliation_id: The reconciliation_id of this InlineResponse2005.
        :type: str
        """
        if reconciliation_id is not None and len(reconciliation_id) > 60:
            raise ValueError("Invalid value for `reconciliation_id`, length must be less than or equal to `60`")

        self._reconciliation_id = reconciliation_id

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this InlineResponse2005.

        :return: The client_reference_information of this InlineResponse2005.
        :rtype: InlineResponse201ClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this InlineResponse2005.

        :param client_reference_information: The client_reference_information of this InlineResponse2005.
        :type: InlineResponse201ClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def refund_amount_details(self):
        """
        Gets the refund_amount_details of this InlineResponse2005.

        :return: The refund_amount_details of this InlineResponse2005.
        :rtype: InlineResponse2013RefundAmountDetails
        """
        return self._refund_amount_details

    @refund_amount_details.setter
    def refund_amount_details(self, refund_amount_details):
        """
        Sets the refund_amount_details of this InlineResponse2005.

        :param refund_amount_details: The refund_amount_details of this InlineResponse2005.
        :type: InlineResponse2013RefundAmountDetails
        """

        self._refund_amount_details = refund_amount_details

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
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
