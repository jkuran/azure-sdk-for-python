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


class TranscriptModerationBodyItemTermsItem(Model):
    """TranscriptModerationBodyItemTermsItem.

    :param index: Index of the word
    :type index: int
    :param term: Detected word.
    :type term: str
    """

    _validation = {
        'index': {'required': True},
        'term': {'required': True},
    }

    _attribute_map = {
        'index': {'key': 'Index', 'type': 'int'},
        'term': {'key': 'Term', 'type': 'str'},
    }

    def __init__(self, index, term):
        self.index = index
        self.term = term