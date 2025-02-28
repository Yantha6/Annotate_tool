import unittest
import ast
from src.pe.code_parser import CodeParserPE

class TestCodeParser(unittest.TestCase):
    def setUp(self):
        self.parser = CodeParserPE()

    def test_valid_code(self):
        code = """
def hello():
    print("Hello, World!")
"""
        result = self.parser.process(code)
        self.assertTrue(result['is_valid'])
        self.assertIsInstance(result['ast'], ast.AST)
        self.assertEqual(len(result['errors']), 0)

    def test_invalid_code(self):
        code = """
def hello()
    print("Missing colon")
"""
        result = self.parser.process(code)
        self.assertFalse(result['is_valid'])
        self.assertIsNone(result['ast'])
        self.assertGreater(len(result['errors']), 0)