#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""WSGI script for Nova API

EXPERIMENTAL support script for running Nova API under Apache2 etc.

"""

from oslo_config import cfg
from oslo_log import log as logging
from paste import deploy

from nova import config
from nova import objects
from nova import service  # noqa
from nova import utils

CONF = cfg.CONF

config_files = ['/etc/nova/api-paste.ini', '/etc/nova/nova.conf']
config.parse_args([], default_config_files=config_files)

LOG = logging.getLogger(__name__)
logging.setup(CONF, "nova")
utils.monkey_patch()
objects.register_all()

conf = config_files[0]
name = "osapi_compute"

options = deploy.appconfig('config:%s' % conf, name=name)

application = deploy.loadapp('config:%s' % conf, name=name)
