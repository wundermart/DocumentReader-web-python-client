# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


"""
Enumeration contains identifiers determining type of features for a document authenticity checks
"""
class SecurityFeatureType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    BLANK = int("0")

    FILL = int("1")

    PHOTO = int("2")

    MRZ = int("3")

    FALSE_LUMINESCENCE = int("4")

    HOLO_SIMPLE = int("5")

    HOLO_VERIFY_STATIC = int("6")

    HOLO_VERIFY_MULTI_STATIC = int("7")

    HOLO_VERIFY_DYNAMIC = int("8")

    PATTERN_NOT_INTERRUPTED = int("9")

    PATTERN_NOT_SHIFTED = int("10")

    PATTERN_SAME_COLORS = int("11")

    PATTERN_IR_INVISIBLE = int("12")

    PHOTO_SIZE_CHECK = int("13")

    PORTRAIT_COMPARISON_VS_GHOST = int("14")

    PORTRAIT_COMPARISON_VS_RFID = int("15")

    PORTRAIT_COMPARISON_VS_VISUAL = int("16")

    BARCODE = int("17")

    PATTERN_DIFFERENT_LINES_THICKNESS = int("18")

    PORTRAIT_COMPARISON_VS_CAMERA = int("19")

    PORTRAIT_COMPARISON_RFID_VS_CAMERA = int("20")

    GHOST_PHOTO = int("21")

    CLEAR_GHOST_PHOTO = int("22")

    INVISIBLE_OBJECT = int("23")

    LOW_CONTRAST_OBJECT = int("24")

    PHOTO_COLOR = int("25")

    PHOTO_SHAPE = int("26")

    PHOTO_CORNERS = int("27")

    PORTRAIT_COMPARISON_EXT_VS_VISUAL = int("29")

    PORTRAIT_COMPARISON_EXT_VS_RFID = int("30")

    PORTRAIT_COMPARISON_EXT_VS_CAMERA = int("31")

    allowable_values = [BLANK, FILL, PHOTO, MRZ, FALSE_LUMINESCENCE, HOLO_SIMPLE, HOLO_VERIFY_STATIC, HOLO_VERIFY_MULTI_STATIC, HOLO_VERIFY_DYNAMIC, PATTERN_NOT_INTERRUPTED, PATTERN_NOT_SHIFTED, PATTERN_SAME_COLORS, PATTERN_IR_INVISIBLE, PHOTO_SIZE_CHECK, PORTRAIT_COMPARISON_VS_GHOST, PORTRAIT_COMPARISON_VS_RFID, PORTRAIT_COMPARISON_VS_VISUAL, BARCODE, PATTERN_DIFFERENT_LINES_THICKNESS, PORTRAIT_COMPARISON_VS_CAMERA, PORTRAIT_COMPARISON_RFID_VS_CAMERA, GHOST_PHOTO, CLEAR_GHOST_PHOTO, INVISIBLE_OBJECT, LOW_CONTRAST_OBJECT, PHOTO_COLOR, PHOTO_SHAPE, PHOTO_CORNERS, PORTRAIT_COMPARISON_EXT_VS_VISUAL, PORTRAIT_COMPARISON_EXT_VS_RFID, PORTRAIT_COMPARISON_EXT_VS_CAMERA]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """SecurityFeatureType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityFeatureType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityFeatureType):
            return True

        return self.to_dict() != other.to_dict()
