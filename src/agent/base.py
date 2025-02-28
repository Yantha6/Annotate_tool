from typing import Any, Dict, List
from src.pe.base import BasePE

class Agent:
    """Agent基类，用于管理和协调PE"""
    
    def __init__(self, name: str):
        self.name = name
        self.pes: List[BasePE] = []
        
    def add_pe(self, pe: BasePE) -> None:
        """添加处理元素"""
        self.pes.append(pe)
        
    def execute(self, data: Any) -> Any:
        """执行处理流程"""
        result = data
        for pe in self.pes:
            result = pe.process(result)
        return result