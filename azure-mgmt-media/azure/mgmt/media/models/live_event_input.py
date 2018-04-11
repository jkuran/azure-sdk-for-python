# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LiveEventInput(Model):
    """The Live Event input.

    :param streaming_protocol: The streaming protocol for the Live Event.
     Possible values include: 'FragmentedMP4', 'RTMP'
    :type streaming_protocol: str or
     ~azure.mgmt.media.models.LiveEventInputProtocol
    :param key_frame_interval_duration: ISO 8601 timespan duration of the key
     frame interval duration.
    :type key_frame_interval_duration: str
    :param access_token: The access token.
    :type access_token: str
    :param endpoints: The input endpoints for the Live Event.
    :type endpoints: list[~azure.mgmt.media.models.LiveEventEndpoint]
    """

    _attribute_map = {
        'streaming_protocol': {'key': 'streamingProtocol', 'type': 'LiveEventInputProtocol'},
        'key_frame_interval_duration': {'key': 'keyFrameIntervalDuration', 'type': 'str'},
        'access_token': {'key': 'accessToken', 'type': 'str'},
        'endpoints': {'key': 'endpoints', 'type': '[LiveEventEndpoint]'},
    }

    def __init__(self, **kwargs):
        super(LiveEventInput, self).__init__(**kwargs)
        self.streaming_protocol = kwargs.get('streaming_protocol', None)
        self.key_frame_interval_duration = kwargs.get('key_frame_interval_duration', None)
        self.access_token = kwargs.get('access_token', None)
        self.endpoints = kwargs.get('endpoints', None)
