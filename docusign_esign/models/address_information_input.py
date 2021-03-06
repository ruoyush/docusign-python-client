# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AddressInformationInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address_information=None, display_level_code=None, receive_in_response=None):
        """
        AddressInformationInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_information': 'AddressInformation',
            'display_level_code': 'str',
            'receive_in_response': 'str'
        }

        self.attribute_map = {
            'address_information': 'addressInformation',
            'display_level_code': 'displayLevelCode',
            'receive_in_response': 'receiveInResponse'
        }

        self._address_information = address_information
        self._display_level_code = display_level_code
        self._receive_in_response = receive_in_response

    @property
    def address_information(self):
        """
        Gets the address_information of this AddressInformationInput.

        :return: The address_information of this AddressInformationInput.
        :rtype: AddressInformation
        """
        return self._address_information

    @address_information.setter
    def address_information(self, address_information):
        """
        Sets the address_information of this AddressInformationInput.

        :param address_information: The address_information of this AddressInformationInput.
        :type: AddressInformation
        """

        self._address_information = address_information

    @property
    def display_level_code(self):
        """
        Gets the display_level_code of this AddressInformationInput.
        Specifies the display level for the recipient.  Valid values are:   * ReadOnly * Editable * DoNotDisplay

        :return: The display_level_code of this AddressInformationInput.
        :rtype: str
        """
        return self._display_level_code

    @display_level_code.setter
    def display_level_code(self, display_level_code):
        """
        Sets the display_level_code of this AddressInformationInput.
        Specifies the display level for the recipient.  Valid values are:   * ReadOnly * Editable * DoNotDisplay

        :param display_level_code: The display_level_code of this AddressInformationInput.
        :type: str
        """

        self._display_level_code = display_level_code

    @property
    def receive_in_response(self):
        """
        Gets the receive_in_response of this AddressInformationInput.
        When set to **true**, the information needs to be returned in the response.

        :return: The receive_in_response of this AddressInformationInput.
        :rtype: str
        """
        return self._receive_in_response

    @receive_in_response.setter
    def receive_in_response(self, receive_in_response):
        """
        Sets the receive_in_response of this AddressInformationInput.
        When set to **true**, the information needs to be returned in the response.

        :param receive_in_response: The receive_in_response of this AddressInformationInput.
        :type: str
        """

        self._receive_in_response = receive_in_response

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
