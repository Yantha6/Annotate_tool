from typing import Any, Dict, List
from src.pe.base import BasePE
import ast

class StyleCheckerPE(BasePE):
    """代码风格检查PE"""
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        输入: 前一个PE的结果字典
        输出: 包含风格检查结果的字典
        """
        results = {
            'is_valid': data.get('is_valid', True),
            'errors': data.get('errors', []),
            'style_score': 100,
            'style_issues': []
        }
        
        # 如果前面的检查失败，直接返回
        if not results['is_valid']:
            return results
            
        ast_tree = data.get('ast')
        if isinstance(ast_tree, ast.AST):
            checker = StyleNodeVisitor()
            checker.visit(ast_tree)
            results['style_issues'] = checker.issues
            results['style_score'] = max(0, 100 - len(checker.issues) * 5)
            
        return results

class StyleNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.issues = []
        
    def visit_FunctionDef(self, node):
        # 检查函数名是否符合PEP8
        if not node.name.islower():
            self.issues.append({
                'line': node.lineno,
                'message': f'函数名 "{node.name}" 应该使用小写字母'
            })
        self.generic_visit(node)