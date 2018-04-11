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


class CrossSiteAccessPolicies(Model):
    """The client access policy.

    :param client_access_policy: The content of clientaccesspolicy.xml used by
     Silverlight.
    :type client_access_policy: str
    :param cross_domain_policy: The content of crossdomain.xml used by
     Silverlight.
    :type cross_domain_policy: str
    """

    _attribute_map = {
        'client_access_policy': {'key': 'clientAccessPolicy', 'type': 'str'},
        'cross_domain_policy': {'key': 'crossDomainPolicy', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CrossSiteAccessPolicies, self).__init__(**kwargs)
        self.client_access_policy = kwargs.get('client_access_policy', None)
        self.cross_domain_policy = kwargs.get('cross_domain_policy', None)
