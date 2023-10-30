import unittest
from solutions.solution2 import get_dependency_graph_from_file


class GetDependencyGraphFileTestCase(unittest.TestCase):
    def test_simple_demo(self):
        res = get_dependency_graph_from_file('./tests_data/deps.json')
        # read correct output from file
        with open('./tests_data/deps_json_output.txt', 'r') as file:
            demo_res = file.read()
        self.assertEqual(res, demo_res)

    def test_three_levels_indent(self):
        """
        Tests case where input dependency graph includes 3 levels of depth
        """
        res = get_dependency_graph_from_file('./tests_data/three_levels_indent.json')
        # read correct output from file
        with open('./tests_data/three_levels_indent_output.txt', 'r') as file:
            demo_res = file.read()
        self.assertEqual(res, demo_res)


if __name__ == '__main__':
    unittest.main()
