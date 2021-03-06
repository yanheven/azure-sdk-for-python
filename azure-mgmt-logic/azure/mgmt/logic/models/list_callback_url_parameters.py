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


class ListCallbackUrlParameters(Model):
    """ListCallbackUrlParameters.

    :param not_after: The expiry time.
    :type not_after: datetime
    """ 

    _attribute_map = {
        'not_after': {'key': 'NotAfter', 'type': 'iso-8601'},
    }

    def __init__(self, not_after=None):
        self.not_after = not_after
