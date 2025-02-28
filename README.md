好的，我来帮您编写一个详细的 README.md 文件：

```markdown:/Users/bytedance/Code/MyWork/Annotate_tool/README.md
# Annotate_tool

一个用于Python代码质量检查和标注的工具。

## 功能特点

- 语法正确性检查
- 代码风格分析
- 代码质量评分
- 详细的问题报告

## 项目结构

```plaintext
src/
├── agent/          # Agent模块，用于协调各个处理元素
├── pe/            # Processing Elements，各种处理单元
├── workflow/      # 工作流管理
├── utils/         # 工具函数
└── config/        # 配置文件
```

## 使用方法

### 命令行使用

分析单个Python文件：
```bash
python src/main.py path/to/your/code.py
```

使用详细输出模式：
```bash
python src/cli.py path/to/your/code.py --verbose
```

保存分析结果到文件：
```bash
python src/cli.py path/to/your/code.py -o result.txt
```

### 输出示例

```
标注结果:
语法检查: 通过
代码风格得分: 95
总体得分: 95

发现的问题:
- 第10行: 函数名应使用小写字母
- 第15行: 行长度超过80个字符
```

## 配置

可以在 `src/config/settings.py` 中修改以下配置：

- 代码风格规则
- 语法检查规则
- 评分权重

## 开发

### 添加新的检查规则

1. 在 `src/pe/` 目录下创建新的处理元素
2. 在 `CodeAnnotatorAgent` 中注册新的PE
3. 更新结果聚合逻辑

### 运行测试

```bash
python -m unittest discover tests
```

## 联系方式

- Email: [1257330051@example.com]
- GitHub: [@Yantha6]