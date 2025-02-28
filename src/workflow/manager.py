from typing import Dict, List, Any
from src.agent.base import Agent

class WorkflowManager:
    """工作流管理器"""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        
    def register_agent(self, agent: Agent) -> None:
        """注册Agent"""
        self.agents[agent.name] = agent
        
    def execute_workflow(self, agent_name: str, data: Any) -> Any:
        """执行特定Agent的工作流"""
        if agent_name not in self.agents:
            raise KeyError(f"Agent {agent_name} not found")
        return self.agents[agent_name].execute(data)