# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestLogEntry(object):
    """
    Log entries related to a specific work request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestLogEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this WorkRequestLogEntry.
        :type message: str

        :param timestamp:
            The value to assign to the timestamp property of this WorkRequestLogEntry.
        :type timestamp: datetime

        """
        self.swagger_types = {
            'message': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'message': 'message',
            'timestamp': 'timestamp'
        }

        self._message = None
        self._timestamp = None

    @property
    def message(self):
        """
        **[Required]** Gets the message of this WorkRequestLogEntry.
        The description of an action that occurred.


        :return: The message of this WorkRequestLogEntry.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequestLogEntry.
        The description of an action that occurred.


        :param message: The message of this WorkRequestLogEntry.
        :type: str
        """
        self._message = message

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this WorkRequestLogEntry.
        The date and time the log entry occurred.


        :return: The timestamp of this WorkRequestLogEntry.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this WorkRequestLogEntry.
        The date and time the log entry occurred.


        :param timestamp: The timestamp of this WorkRequestLogEntry.
        :type: datetime
        """
        self._timestamp = timestamp

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
