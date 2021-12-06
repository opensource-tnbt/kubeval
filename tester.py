from kubernetes import client, config
from kubernetes.stream import stream
import logging

def test_list_node(api):
    node_list = api.list_node()
    nodes = []
    if node_list:
        print(node_list)
    else:
        print("FAILED")

    for node in node_list.items:
        nodes.append(node.metadata.name)
        print(node.metadata.name)

def main():
    config.load_kube_config('/home/sridhar/kubeval/conf/pod18.config')
    api = client.CoreV1Api()
    logger = logging.getLogger(__name__)
    test_list_node(api)

if __name__ == "__main__":
    main()
