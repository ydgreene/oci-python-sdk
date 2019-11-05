# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScaleAnalyticsInstanceDetails(object):
    """
    Input payload to scale an Analytics instance up or down.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScaleAnalyticsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity:
            The value to assign to the capacity property of this ScaleAnalyticsInstanceDetails.
        :type capacity: Capacity

        """
        self.swagger_types = {
            'capacity': 'Capacity'
        }

        self.attribute_map = {
            'capacity': 'capacity'
        }

        self._capacity = None

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this ScaleAnalyticsInstanceDetails.

        :return: The capacity of this ScaleAnalyticsInstanceDetails.
        :rtype: Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this ScaleAnalyticsInstanceDetails.

        :param capacity: The capacity of this ScaleAnalyticsInstanceDetails.
        :type: Capacity
        """
        self._capacity = capacity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
