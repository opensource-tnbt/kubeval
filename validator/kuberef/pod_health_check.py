

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
