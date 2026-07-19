from tools.nodes import list_nodes


def print_nodes():
    nodes = list_nodes()

    print(
        f"{'NAME':42}"
        f"{'STATUS':10}"
        f"{'ROLES':30}"
        f"{'AGE':8}"
        f"{'VERSION'}"
    )

    for node in nodes:
        print(
            f"{node['name'][:42]:42}"
            f"{node['status']:10}"
            f"{node['roles']:30}"
            f"{node['age']:8}"
            f"{node['version']}"
        )


if __name__ == "__main__":
    print_nodes()
