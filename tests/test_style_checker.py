import unittest
import ast
from src.pe.style_checker import StyleCheckerPE

class TestStyleChecker(unittest.TestCase):
    def setUp(self):
        self.checker = StyleCheckerPE()

    def test_function_naming(self):
        code = """
def BadFunctionName():
    pass
"""
        tree = ast.parse(code)
        result = self.checker.process({'ast': tree, 'is_valid': True, 'errors': []})
        self.assertTrue(any('函数名' in issue['message'] for issue in result['style_issues']))

    def test_valid_style(self):
        code = """
def good_function_name():
    pass
"""
        tree = ast.parse(code)
        result = self.checker.process({'ast': tree, 'is_valid': True, 'errors': []})
        self.assertEqual(len(result['style_issues']), 0)
        self.assertEqual(result['style_score'], 100)