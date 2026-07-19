from kubernetes import client, config
from datetime import datetime, timezone


def get_node_role(node):
    labels = node.metadata.labels

    roles = []

    for label in labels:
        if label.startswith("node-role.kubernetes.io/"):
            role = label.replace("node-role.kubernetes.io/", "")
            roles.append(role)

    if not roles:
        roles.append("<none>")

    return ",".join(roles)


def get_node_status(node):
    for condition in node.status.conditions:
        if condition.type == "Ready":
            return "Ready" if condition.status == "True" else "NotReady"

    return "Unknown"


def get_node_age(node):
    now = datetime.now(timezone.utc)
    age = now - node.metadata.creation_timestamp

    return f"{age.days}d"


def list_nodes():
    config.load_kube_config()

    v1 = client.CoreV1Api()

    nodes = v1.list_node()

    result = []

    for node in nodes.items:
        result.append(
            {
                "name": node.metadata.name,
                "status": get_node_status(node),
                "roles": get_node_role(node),
                "age": get_node_age(node),
                "version": node.status.node_info.kubelet_version,
            }
        )

    return result
