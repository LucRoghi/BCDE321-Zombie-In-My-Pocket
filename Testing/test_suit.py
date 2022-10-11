import unittest

from Testing.test_database_handler import DatabaseHandlerTest
from Testing.test_map_tile import MapTileTest


class AllTests:
    def __init__(self):
        self.test_classes_to_run = [DatabaseHandlerTest, MapTileTest]
        self.big_suite = self.add_test_to_test_suite()

    def add_test_to_test_suite(self):
        loader = unittest.TestLoader()

        suites_list = []
        for test_class in self.test_classes_to_run:
            suite = loader.loadTestsFromTestCase(test_class)
            suites_list.append(suite)

        return unittest.TestSuite(suites_list)

    def run_test_suite(self):
        runner = unittest.TextTestRunner()
        results = runner.run(self.big_suite)
        return results


if __name__ == "__main__":
    test_suite = AllTests()
    test_suite.run_test_suite()
