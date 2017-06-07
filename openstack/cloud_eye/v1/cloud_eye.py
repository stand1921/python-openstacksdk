# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.cloud_eye import cloud_eye_service
from openstack import resource


class Alarm(resource.Resource):
    resource_key = None
    resources_key = None
    base_path = "/V1.0/%s(project_id)/alarms"
    service = cloud_eye_service.CloudEyeService()
    id_attribute = "name"

    allow_list = True

    #: The transaction date and time.
    timestamp = resource.prop("x-timestamp")
    #: The name of this resource.
    name = resource.prop("name")
    #: The value of the resource. Also available in headers.
    value = resource.prop("value", alias="x-resource-value")
    #: Is this resource cool? If so, set it to True.
    #: This is a multi-line comment about cool stuff.
    cool = resource.prop("cool", type=bool)
