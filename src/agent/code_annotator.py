from typing import Any, Dict
from src.agent.base import Agent
from src.pe.code_parser import CodeParserPE
from src.pe.syntax_checker import SyntaxCheckerPE
from src.pe.style_checker import StyleCheckerPE
from src.pe.result_aggregator import ResultAggregatorPE

class CodeAnnotatorAgent(Agent):
    """代码标注Agent，用于协调各个PE进行代码分析"""
    
    def __init__(self):
        super().__init__(name="code_annotator")
        # 按顺序添加所需的PE
        self.add_pe(CodeParserPE())
        self.add_pe(SyntaxCheckerPE())
        self.add_pe(StyleCheckerPE())
        self.add_pe(ResultAggregatorPE())