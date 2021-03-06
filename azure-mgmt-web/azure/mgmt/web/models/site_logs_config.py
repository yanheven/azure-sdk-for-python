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

from .resource import Resource


class SiteLogsConfig(Resource):
    """Configuration of Azure web site.

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param application_logs: Application logs configuration
    :type application_logs: :class:`ApplicationLogsConfig
     <azure.mgmt.web.models.ApplicationLogsConfig>`
    :param http_logs: Http logs configuration
    :type http_logs: :class:`HttpLogsConfig
     <azure.mgmt.web.models.HttpLogsConfig>`
    :param failed_requests_tracing: Failed requests tracing configuration
    :type failed_requests_tracing: :class:`EnabledConfig
     <azure.mgmt.web.models.EnabledConfig>`
    :param detailed_error_messages: Detailed error messages configuration
    :type detailed_error_messages: :class:`EnabledConfig
     <azure.mgmt.web.models.EnabledConfig>`
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'application_logs': {'key': 'properties.applicationLogs', 'type': 'ApplicationLogsConfig'},
        'http_logs': {'key': 'properties.httpLogs', 'type': 'HttpLogsConfig'},
        'failed_requests_tracing': {'key': 'properties.failedRequestsTracing', 'type': 'EnabledConfig'},
        'detailed_error_messages': {'key': 'properties.detailedErrorMessages', 'type': 'EnabledConfig'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, application_logs=None, http_logs=None, failed_requests_tracing=None, detailed_error_messages=None):
        super(SiteLogsConfig, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.application_logs = application_logs
        self.http_logs = http_logs
        self.failed_requests_tracing = failed_requests_tracing
        self.detailed_error_messages = detailed_error_messages
