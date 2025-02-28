from typing import Any, Dict, List
from src.pe.base import BasePE

class ResultAggregatorPE(BasePE):
    """结果聚合PE"""
    
    def process(self, data: Any) -> Dict[str, Any]:
        """
        输入: 前一个PE的输出结果
        输出: 聚合后的最终结果
        """
        final_result = {
            'overall_score': 0,
            'syntax_valid': True,  # 默认为True
            'style_score': 100,    # 默认满分
            'issues': []
        }
        
        # 如果输入是字典，直接使用其中的信息
        if isinstance(data, dict):
            if 'is_valid' in data:
                final_result['syntax_valid'] = data['is_valid']
            if 'errors' in data:
                final_result['issues'].extend(data['errors'])
            if 'style_issues' in data:
                final_result['issues'].extend(data['style_issues'])
            if 'score' in data:
                final_result['style_score'] = data['score']
        
        # 计算总体得分
        if not final_result['syntax_valid']:
            final_result['overall_score'] = 0
        else:
            final_result['overall_score'] = final_result['style_score']
        
        return final_result