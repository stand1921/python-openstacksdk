import argparse
import os

import os_client_config

from openstack import connection
from openstack import profile
from openstack import utils
import sys

prof = profile.Profile()
prof.set_region(profile.Profile.ALL, region)

conn = connection.Connection(
    profile=prof,
    user_agent='examples',
    auth_url=auth_url,
    project_name=project_name,
    username=username,
    password=password
)
