import argparse
import sys
from src.main import main

def parse_args():
    parser = argparse.ArgumentParser(description='代码标注工具')
    parser.add_argument('file', help='要分析的Python文件路径')
    parser.add_argument('--output', '-o', help='输出结果的文件路径')
    parser.add_argument('--verbose', '-v', action='store_true', help='显示详细信息')
    return parser.parse_args()

def cli_main():
    args = parse_args()
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        result = main(code)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(str(result))
        else:
            print(result)
            
    except Exception as e:
        print(f"错误: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    cli_main()