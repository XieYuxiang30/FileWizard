import sys

# 修复 Windows 控制台默认 GBK 编码导致的 emoji 乱码
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import argparse
from pathlib import Path
from src.organizer import organize_directory
from src.reporter import print_welcome, print_report


def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description="FileWizard - 一键整理你的文件夹")
    parser.add_argument("path", help="需要整理的文件夹路径 (例如: C:\\Users\\Downloads)")
    parser.add_argument("--dry-run", action="store_true", help="预览模式：只显示将移动哪些文件，不实际执行")
    
    args = parser.parse_args()

    print_welcome()
    
    # 获取当前 config.json 所在的绝对路径
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"

    # 执行整理
    report = organize_directory(args.path, config_path, dry_run=args.dry_run)
    
    # 打印报告
    print_report(report, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
