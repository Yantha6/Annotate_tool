from abc import ABC, abstractmethod
from typing import Any, Dict

class BasePE(ABC):
    """处理元素的基类"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        
    @abstractmethod
    def process(self, data: Any) -> Any:
        """处理数据的核心方法"""
        pass
    
    def initialize(self) -> None:
        """初始化PE"""
        pass
    
    def cleanup(self) -> None:
        """清理资源"""
        pass