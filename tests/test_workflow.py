import unittest
from src.workflow.manager import WorkflowManager
from src.agent.code_annotator import CodeAnnotatorAgent

class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.workflow_manager = WorkflowManager()
        self.workflow_manager.register_agent(CodeAnnotatorAgent())

    def test_complete_workflow(self):
        code = """
def hello_world():
    try:
        print("Hello, World!")
    except Exception as e:
        print(f"Error: {e}")
"""
        result = self.workflow_manager.execute_workflow("code_annotator", code)
        self.assertIsNotNone(result)
        self.assertTrue(result['syntax_valid'])
        self.assertGreaterEqual(result['style_score'], 0)
        self.assertLessEqual(result['style_score'], 100)

    def test_invalid_code_workflow(self):
        code = "def invalid_function("
        result = self.workflow_manager.execute_workflow("code_annotator", code)
        self.assertIsNotNone(result)
        self.assertFalse(result['syntax_valid'])