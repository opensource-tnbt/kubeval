# Copyright 2020 University Of Delhi.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Pod Health Checks
"""



import logging

from core import store_result
from core.pod_health_check import get_logs, pod_status
from tools.kube_utils import kube_api
from conf import settings


def pod_health_check():
    """
    Check health of all pods and get logs of failed pods
    """
    logger = logging.getLogger(__name__)
    kapi = kube_api()
    namespace_list = settings.getValue('kuberef_namespace_list')

    result = {'category':  'platform',
              'case_name': 'pod_health_check',
              'criteria':  'pass',
              'details': []
             }

    for namespace in namespace_list:
        pod_list = kapi.list_namespaced_pod(namespace)
        for pod in pod_list.items:
            pod_stats = pod_status(logger, pod)
            if pod_stats['criteria'] == 'fail':
                pod_stats['logs'] = get_logs(kapi, pod)
                result['criteria'] = 'fail'
            result['details'].append(pod_stats)
    
    #result = pod_health_check(logger, api, namespace_list)

    store_result(logger, result)
    return result
