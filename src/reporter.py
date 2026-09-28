from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# 禁用遗留 Windows 渲染器，避免 GBK 编码导致 emoji 报错
console = Console(legacy_windows=False)


def print_welcome():
    console.print(Panel.fit("🧙‍♂️ [bold magenta]FileWizard 文件自动分类整理器[/bold magenta]", border_style="cyan"))


def print_report(report, dry_run=False):
    # 打印最终的整理报告表格
    if "error" in report:
        console.print(f"[bold red]❌ 错误: {report['error']}[/bold red]")
        return

    title = "📊 预览报告 (未实际移动)" if dry_run else "✅ 整理完成报告"
    table = Table(title=title, show_header=True, header_style="bold green")
    table.add_column("分类文件夹", style="cyan")
    table.add_column("移动文件数量", style="yellow", justify="right")

    total = 0
    for folder, count in report.items():
        if count > 0:
            table.add_row(folder, str(count))
            total += count
            
    if total == 0:
        console.print("[yellow]📭 目标文件夹已经很整洁，没有需要整理的文件。[/yellow]")
    else:
        console.print(table)
        action = "预计移动" if dry_run else "成功移动"
        console.print(f"✨ 共 {action} [bold green]{total}[/bold green] 个文件。")
