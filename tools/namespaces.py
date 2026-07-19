from kubernetes import client, config


def list_namespaces():
    """
    Return all Kubernetes namespaces using the current kubeconfig.
    """

    config.load_kube_config()

    v1 = client.CoreV1Api()

    namespaces = v1.list_namespace()

    return [ns.metadata.name for ns in namespaces.items]
