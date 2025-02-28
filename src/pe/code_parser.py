from typing import Any, Dict
from src.pe.base import BasePE
import ast

class CodeParserPE(BasePE):
    """代码解析PE，将源代码转换为AST"""
    
    def process(self, data: str) -> Dict[str, Any]:
        """
        输入: 源代码字符串
        输出: 包含AST和解析结果的字典
        """
        try:
            tree = ast.parse(data)
            return {
                'ast': tree,
                'is_valid': True,
                'errors': []
            }
        except SyntaxError as e:
            return {
                'ast': None,
                'is_valid': False,
                'errors': [{
                    'line': getattr(e, 'lineno', 1),
                    'message': f'语法错误: {str(e)}'
                }]
            }