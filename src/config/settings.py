class Config:
    """全局配置"""
    
    # 代码风格检查配置
    STYLE_RULES = {
        'function_naming': 'snake_case',
        'class_naming': 'PascalCase',
        'max_line_length': 80,
        'indent_size': 4
    }
    
    # 语法检查配置
    SYNTAX_RULES = {
        'check_try_except': True,
        'check_return_types': True,
        'check_unused_imports': True
    }
    
    # 评分配置
    SCORING = {
        'style_weight': 0.4,
        'syntax_weight': 0.6,
        'penalty_per_issue': 5
    }