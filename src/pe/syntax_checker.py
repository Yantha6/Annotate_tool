from typing import Any, Dict, List
from src.pe.base import BasePE
import ast

class SyntaxCheckerPE(BasePE):
    """语法检查PE"""
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        输入: 包含AST的字典
        输出: 语法检查结果
        """
        results = {
            'is_valid': True,
            'errors': []
        }
        
        # 检查前一步的结果
        if not data.get('is_valid'):
            return data
            
        ast_tree = data.get('ast')
        if not isinstance(ast_tree, ast.AST):
            results['is_valid'] = False
            results['errors'].append({
                'line': 1,
                'message': '输入不是有效的AST对象'
            })
            return results
            
        checker = SyntaxNodeVisitor()
        checker.visit(ast_tree)
        
        # 合并错误信息
        results['errors'].extend(data.get('errors', []))
        results['errors'].extend(checker.errors)
        results['is_valid'] = len(results['errors']) == 0
        
        return results

class SyntaxNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.errors = []
        
    def visit_Try(self, node):
        if not node.handlers and not node.finalbody:
            self.errors.append({
                'line': node.lineno,
                'message': 'Try block without except or finally'
            })
        self.generic_visit(node)