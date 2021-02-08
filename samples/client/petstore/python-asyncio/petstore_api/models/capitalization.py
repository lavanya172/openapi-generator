# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from petstore_api.configuration import Configuration


class Capitalization(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'small_camel': 'str',
        'capital_camel': 'str',
        'small_snake': 'str',
        'capital_snake': 'str',
        'sca_eth_flow_points': 'str',
        'att_name': 'str'
    }

    attribute_map = {
        'small_camel': 'smallCamel',
        'capital_camel': 'CapitalCamel',
        'small_snake': 'small_Snake',
        'capital_snake': 'Capital_Snake',
        'sca_eth_flow_points': 'SCA_ETH_Flow_Points',
        'att_name': 'ATT_NAME'
    }

    def __init__(self, small_camel=None, capital_camel=None, small_snake=None, capital_snake=None, sca_eth_flow_points=None, att_name=None, local_vars_configuration=None):  # noqa: E501
        """Capitalization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._small_camel = None
        self._capital_camel = None
        self._small_snake = None
        self._capital_snake = None
        self._sca_eth_flow_points = None
        self._att_name = None
        self.discriminator = None

        if small_camel is not None:
            self.small_camel = small_camel
        if capital_camel is not None:
            self.capital_camel = capital_camel
        if small_snake is not None:
            self.small_snake = small_snake
        if capital_snake is not None:
            self.capital_snake = capital_snake
        if sca_eth_flow_points is not None:
            self.sca_eth_flow_points = sca_eth_flow_points
        if att_name is not None:
            self.att_name = att_name

    @property
    def small_camel(self):
        """Gets the small_camel of this Capitalization.  # noqa: E501


        :return: The small_camel of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._small_camel

    @small_camel.setter
    def small_camel(self, small_camel):
        """Sets the small_camel of this Capitalization.


        :param small_camel: The small_camel of this Capitalization.  # noqa: E501
        :type small_camel: str
        """

        self._small_camel = small_camel

    @property
    def capital_camel(self):
        """Gets the capital_camel of this Capitalization.  # noqa: E501


        :return: The capital_camel of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._capital_camel

    @capital_camel.setter
    def capital_camel(self, capital_camel):
        """Sets the capital_camel of this Capitalization.


        :param capital_camel: The capital_camel of this Capitalization.  # noqa: E501
        :type capital_camel: str
        """

        self._capital_camel = capital_camel

    @property
    def small_snake(self):
        """Gets the small_snake of this Capitalization.  # noqa: E501


        :return: The small_snake of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._small_snake

    @small_snake.setter
    def small_snake(self, small_snake):
        """Sets the small_snake of this Capitalization.


        :param small_snake: The small_snake of this Capitalization.  # noqa: E501
        :type small_snake: str
        """

        self._small_snake = small_snake

    @property
    def capital_snake(self):
        """Gets the capital_snake of this Capitalization.  # noqa: E501


        :return: The capital_snake of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._capital_snake

    @capital_snake.setter
    def capital_snake(self, capital_snake):
        """Sets the capital_snake of this Capitalization.


        :param capital_snake: The capital_snake of this Capitalization.  # noqa: E501
        :type capital_snake: str
        """

        self._capital_snake = capital_snake

    @property
    def sca_eth_flow_points(self):
        """Gets the sca_eth_flow_points of this Capitalization.  # noqa: E501


        :return: The sca_eth_flow_points of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._sca_eth_flow_points

    @sca_eth_flow_points.setter
    def sca_eth_flow_points(self, sca_eth_flow_points):
        """Sets the sca_eth_flow_points of this Capitalization.


        :param sca_eth_flow_points: The sca_eth_flow_points of this Capitalization.  # noqa: E501
        :type sca_eth_flow_points: str
        """

        self._sca_eth_flow_points = sca_eth_flow_points

    @property
    def att_name(self):
        """Gets the att_name of this Capitalization.  # noqa: E501

        Name of the pet   # noqa: E501

        :return: The att_name of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._att_name

    @att_name.setter
    def att_name(self, att_name):
        """Sets the att_name of this Capitalization.

        Name of the pet   # noqa: E501

        :param att_name: The att_name of this Capitalization.  # noqa: E501
        :type att_name: str
        """

        self._att_name = att_name

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Capitalization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Capitalization):
            return True

        return self.to_dict() != other.to_dict()
