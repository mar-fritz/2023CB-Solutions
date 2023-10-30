import json


class PackageDependenciesGraph:
    def __init__(self, json_dict: dict):
        # store adjacency list
        self.pkg_dependencies = json_dict

    def collect_dep(self, pkg: str, lvl: int):
        """
        Helper function used by get_full_graph to recursively collect dependencies of pkg in res
        :param pkg: current package
        :param lvl: level of indent
        :return: str
        """
        res = ("\t" * lvl+"- "+pkg+"\n")
        for dependency in self.pkg_dependencies[pkg]:
            res += self.collect_dep(dependency, lvl + 1)
        return res

    def get_full_graph(self):
        """
        Returns full dependency graph as string
        :return: str
        """
        res = ""
        # for each package
        for pkg in self.pkg_dependencies.keys():
            # recursively collect child packages
            res += self.collect_dep(pkg, 0)
        return res


def get_dependency_graph_from_file(filepath='./data/deps.json'):
    """
    Returns dependency graph from JSON file
    :param filepath: path to JSON file of package dependencies
    :return: str
    """
    with open(filepath) as json_file:
        data = json.load(json_file)
    # create package dependencies graph
    package_deps = PackageDependenciesGraph(data)
    # and return full dependency graph
    return package_deps.get_full_graph()


if __name__ == "__main__":
    # run demo
    print(get_dependency_graph_from_file())
