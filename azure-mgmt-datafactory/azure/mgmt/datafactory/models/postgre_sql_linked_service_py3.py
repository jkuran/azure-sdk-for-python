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

from .linked_service import LinkedService


class PostgreSqlLinkedService(LinkedService):
    """Linked service for PostgreSQL data source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param server: Required. Server name for connection. Type: string (or
     Expression with resultType string).
    :type server: object
    :param database: Required. Database name for connection. Type: string (or
     Expression with resultType string).
    :type database: object
    :param schema: Schema name for connection. Type: string (or Expression
     with resultType string).
    :type schema: object
    :param username: Username for authentication. Type: string (or Expression
     with resultType string).
    :type username: object
    :param password: Password for authentication.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'server': {'required': True},
        'database': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'server': {'key': 'typeProperties.server', 'type': 'object'},
        'database': {'key': 'typeProperties.database', 'type': 'object'},
        'schema': {'key': 'typeProperties.schema', 'type': 'object'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, *, server, database, additional_properties=None, connect_via=None, description: str=None, parameters=None, annotations=None, schema=None, username=None, password=None, encrypted_credential=None, **kwargs) -> None:
        super(PostgreSqlLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations, **kwargs)
        self.server = server
        self.database = database
        self.schema = schema
        self.username = username
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.type = 'PostgreSql'
