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

from .execution_activity import ExecutionActivity


class CustomActivity(ExecutionActivity):
    """Custom activity type.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param command: Required. Command for custom activity Type: string (or
     Expression with resultType string).
    :type command: object
    :param resource_linked_service: Resource linked service reference.
    :type resource_linked_service:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param folder_path: Folder path for resource files Type: string (or
     Expression with resultType string).
    :type folder_path: object
    :param reference_objects: Reference objects
    :type reference_objects:
     ~azure.mgmt.datafactory.models.CustomActivityReferenceObject
    :param extended_properties: User defined property bag. There is no
     restriction on the keys or values that can be used. The user specified
     custom activity has the full responsibility to consume and interpret the
     content defined.
    :type extended_properties: dict[str, object]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'command': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'command': {'key': 'typeProperties.command', 'type': 'object'},
        'resource_linked_service': {'key': 'typeProperties.resourceLinkedService', 'type': 'LinkedServiceReference'},
        'folder_path': {'key': 'typeProperties.folderPath', 'type': 'object'},
        'reference_objects': {'key': 'typeProperties.referenceObjects', 'type': 'CustomActivityReferenceObject'},
        'extended_properties': {'key': 'typeProperties.extendedProperties', 'type': '{object}'},
    }

    def __init__(self, **kwargs):
        super(CustomActivity, self).__init__(**kwargs)
        self.command = kwargs.get('command', None)
        self.resource_linked_service = kwargs.get('resource_linked_service', None)
        self.folder_path = kwargs.get('folder_path', None)
        self.reference_objects = kwargs.get('reference_objects', None)
        self.extended_properties = kwargs.get('extended_properties', None)
        self.type = 'Custom'
