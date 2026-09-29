import sys

# 修复 Windows 控制台默认 GBK 编码导致的 emoji 乱码
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import argparse
from pathlib import Path
from src.organizer import organize_directory
from src.reporter import print_welcome, print_report


def pick_folder():
    # 弹出文件夹选择对话框，兼容打包后的 exe
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        folder = filedialog.askdirectory(title="选择要整理的文件夹")
        root.destroy()
        return folder or None
    except Exception:
        return None


def main():
    # 设置命令行参数，path 改为可选，方便双击 exe 使用
    parser = argparse.ArgumentParser(description="FileWizard - 一键整理你的文件夹")
    parser.add_argument("path", nargs="?", help="需要整理的文件夹路径 (例如: C:\\Users\\Downloads)")
    parser.add_argument("--dry-run", action="store_true", help="预览模式：只显示将移动哪些文件，不实际执行")
    
    args = parser.parse_args()
    target_path = args.path or pick_folder()

    if not target_path:
        print("未选择文件夹，程序退出。")
        sys.exit(0)

    print_welcome()
    
    # 获取当前 config.json 所在的绝对路径
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"

    # 执行整理
    report = organize_directory(target_path, config_path, dry_run=args.dry_run)
    
    # 打印报告
    print_report(report, dry_run=args.dry_run)
    
    # 结束后暂停，方便双击运行时查看结果
    input("\n按回车键退出...")


if __name__ == "__main__":
    main()
