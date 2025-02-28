import unittest
import ast
from src.pe.syntax_checker import SyntaxCheckerPE

class TestSyntaxChecker(unittest.TestCase):
    def setUp(self):
        self.checker = SyntaxCheckerPE()

    def test_try_without_except(self):
        code = """
try:
    print("Hello")
"""
        tree = ast.parse(code)
        result = self.checker.process({'ast': tree, 'is_valid': True, 'errors': []})
        self.assertFalse(result['is_valid'])
        self.assertTrue(any('Try' in error['message'] for error in result['errors']))

    def test_valid_try_except(self):
        code = """
try:
    print("Hello")
except Exception:
    print("Error")
"""
        tree = ast.parse(code)
        result = self.checker.process({'ast': tree, 'is_valid': True, 'errors': []})
        self.assertTrue(result['is_valid'])
        self.assertEqual(len(result['errors']), 0)