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

from .content_key_policy_restriction_token_key import ContentKeyPolicyRestrictionTokenKey


class ContentKeyPolicyRsaTokenKey(ContentKeyPolicyRestrictionTokenKey):
    """Specifies a RSA key for token validation.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param exponent: Required. The RSA Parameter exponent
    :type exponent: bytearray
    :param modulus: Required. The RSA Parameter modulus
    :type modulus: bytearray
    """

    _validation = {
        'odatatype': {'required': True},
        'exponent': {'required': True},
        'modulus': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'exponent': {'key': 'exponent', 'type': 'bytearray'},
        'modulus': {'key': 'modulus', 'type': 'bytearray'},
    }

    def __init__(self, *, exponent: bytearray, modulus: bytearray, **kwargs) -> None:
        super(ContentKeyPolicyRsaTokenKey, self).__init__(, **kwargs)
        self.exponent = exponent
        self.modulus = modulus
        self.odatatype = '#Microsoft.Media.ContentKeyPolicyRsaTokenKey'
