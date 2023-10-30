import unittest
from solutions.solution1 import remove_duplicates


class DemoTestCase(unittest.TestCase):
    def test_simple_demo(self):
        """
        Tests the simple example provided in the exercise description
        """
        data = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
        result = remove_duplicates(data)
        self.assertEqual(result, ["a", "c", "d"])


if __name__ == '__main__':
    unittest.main()
