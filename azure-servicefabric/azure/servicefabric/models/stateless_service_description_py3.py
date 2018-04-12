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

from .service_description import ServiceDescription


class StatelessServiceDescription(ServiceDescription):
    """Describes a stateless service.

    All required parameters must be populated in order to send to Azure.

    :param application_name: The name of the application, including the
     'fabric:' URI scheme.
    :type application_name: str
    :param service_name: Required. The full name of the service with 'fabric:'
     URI scheme.
    :type service_name: str
    :param service_type_name: Required. Name of the service type as specified
     in the service manifest.
    :type service_type_name: str
    :param initialization_data: The initialization data as an array of bytes.
     Initialization data is passed to service instances or replicas when they
     are created.
    :type initialization_data: list[int]
    :param partition_description: Required. The partition description as an
     object.
    :type partition_description:
     ~azure.servicefabric.models.PartitionSchemeDescription
    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme: The correlation scheme.
    :type correlation_scheme:
     list[~azure.servicefabric.models.ServiceCorrelationDescription]
    :param service_load_metrics: The service load metrics.
    :type service_load_metrics:
     list[~azure.servicefabric.models.ServiceLoadMetricDescription]
    :param service_placement_policies: The service placement policies.
    :type service_placement_policies:
     list[~azure.servicefabric.models.ServicePlacementPolicyDescription]
    :param default_move_cost: The move cost for the service. Possible values
     include: 'Zero', 'Low', 'Medium', 'High'
    :type default_move_cost: str or ~azure.servicefabric.models.MoveCost
    :param is_default_move_cost_specified: Indicates if the DefaultMoveCost
     property is specified.
    :type is_default_move_cost_specified: bool
    :param service_package_activation_mode: The activation mode of service
     package to be used for a service. Possible values include:
     'SharedProcess', 'ExclusiveProcess'
    :type service_package_activation_mode: str or
     ~azure.servicefabric.models.ServicePackageActivationMode
    :param service_dns_name: The DNS name of the service. It requires the DNS
     system service to be enabled in Service Fabric cluster.
    :type service_dns_name: str
    :param scaling_policies: Scaling policies for this service.
    :type scaling_policies:
     list[~azure.servicefabric.models.ScalingPolicyDescription]
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    :param instance_count: Required. The instance count.
    :type instance_count: int
    """

    _validation = {
        'service_name': {'required': True},
        'service_type_name': {'required': True},
        'partition_description': {'required': True},
        'service_kind': {'required': True},
        'instance_count': {'required': True, 'minimum': -1},
    }

    _attribute_map = {
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'service_type_name': {'key': 'ServiceTypeName', 'type': 'str'},
        'initialization_data': {'key': 'InitializationData', 'type': '[int]'},
        'partition_description': {'key': 'PartitionDescription', 'type': 'PartitionSchemeDescription'},
        'placement_constraints': {'key': 'PlacementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'CorrelationScheme', 'type': '[ServiceCorrelationDescription]'},
        'service_load_metrics': {'key': 'ServiceLoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'ServicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'DefaultMoveCost', 'type': 'str'},
        'is_default_move_cost_specified': {'key': 'IsDefaultMoveCostSpecified', 'type': 'bool'},
        'service_package_activation_mode': {'key': 'ServicePackageActivationMode', 'type': 'str'},
        'service_dns_name': {'key': 'ServiceDnsName', 'type': 'str'},
        'scaling_policies': {'key': 'ScalingPolicies', 'type': '[ScalingPolicyDescription]'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'instance_count': {'key': 'InstanceCount', 'type': 'int'},
    }

    def __init__(self, *, service_name: str, service_type_name: str, partition_description, instance_count: int, application_name: str=None, initialization_data=None, placement_constraints: str=None, correlation_scheme=None, service_load_metrics=None, service_placement_policies=None, default_move_cost=None, is_default_move_cost_specified: bool=None, service_package_activation_mode=None, service_dns_name: str=None, scaling_policies=None, **kwargs) -> None:
        super(StatelessServiceDescription, self).__init__(application_name=application_name, service_name=service_name, service_type_name=service_type_name, initialization_data=initialization_data, partition_description=partition_description, placement_constraints=placement_constraints, correlation_scheme=correlation_scheme, service_load_metrics=service_load_metrics, service_placement_policies=service_placement_policies, default_move_cost=default_move_cost, is_default_move_cost_specified=is_default_move_cost_specified, service_package_activation_mode=service_package_activation_mode, service_dns_name=service_dns_name, scaling_policies=scaling_policies, **kwargs)
        self.instance_count = instance_count
        self.service_kind = 'Stateless'
