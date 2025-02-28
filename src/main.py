import os
import sys

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from workflow.manager import WorkflowManager
from agent.code_annotator import CodeAnnotatorAgent

def main(code=None):
    # 初始化工作流管理器
    workflow_manager = WorkflowManager()
    
    # 创建并注册代码标注Agent
    code_annotator = CodeAnnotatorAgent()
    workflow_manager.register_agent(code_annotator)
    
    # 如果没有提供代码，使用示例代码
    # 修改示例代码，添加 except 块
    if code is None:
        code = """def Hello_World():
    try:e
        print("Hello, World!")
    except Exception as e:
        print(f"Error: {e}")"""
    
    # 执行标注工作流
    try:
        result = workflow_manager.execute_workflow("code_annotator", code)
        print("标注结果:")
        print(f"语法检查: {'通过' if result['syntax_valid'] else '未通过'}")
        print(f"代码风格得分: {result['style_score']}")
        print(f"总体得分: {result['overall_score']}")
        
        if result['issues']:
            print("\n发现的问题:")
            for issue in result['issues']:
                print(f"- 第{issue.get('line', '未知')}行: {issue['message']}")
        
        return result
    
    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")
        return None

if __name__ == "__main__":
    # 如果提供了文件路径参数
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            main(code)
        except FileNotFoundError:
            print(f"错误: 找不到文件 '{file_path}'")
        except Exception as e:
            print(f"错误: {str(e)}")
    else:
        # 运行示例代码
        main()