import os
import unittest

"""
discover(start_dir, pattern='test*.py', top_level_dir=None)
Find all the test modules by recursing into subdirectories from the specified
start directory, and return a TestSuite object containing them. Only test files
that match pattern will be loaded. (Using shell style pattern matching.) Only module 
names that are importable (i.e. are valid Python identifiers) will be loaded.
"""

unit_test_path = os.path.dirname(os.path.abspath(__file__))

loader = unittest.TestLoader()
suite = loader.discover(start_dir=unit_test_path, pattern='test*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
