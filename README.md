# 🧙‍♂️ FileWizard (文件自动分类整理器)

告别杂乱的下载文件夹，一键让你的电脑文件井井有条！

## ✨ 核心功能

1. **按类型自动归档**：读取配置文件，自动创建（如"图片"、"文档"、"压缩包"等）文件夹，并把对应后缀的文件移进去。
2. **未知文件处理**：不认识的格式统一扔进"其他"文件夹。
3. **安全预览模式（Dry-Run）**：新手最怕的就是写错代码把文件全弄乱。实现一个 `--dry-run` 参数，只打印"将要移动什么"，但**绝不动你真实的文件**。确认无误后再真正执行。
4. **终端极致美化**：利用 `rich` 库，在终端打出漂亮的进度条和整理汇总表格。

## 🚀 快速开始

### 方式一：使用 Python 运行

1. 克隆代码到本地
2. 安装依赖：`pip install -r requirements.txt`
3. 预览整理（安全）：`python main.py "你的文件夹路径" --dry-run`
4. 确认无误后执行：`python main.py "你的文件夹路径"`

### 方式二：使用 exe 文件（无需 Python 环境）

1. 前往 [Releases](https://github.com/XieYuxiang30/FileWizard/releases) 下载最新版本的 `FileWizard.exe`
2. 将 `FileWizard.exe` 和 `config.json` 放在同一个文件夹下
3. 打开 PowerShell，进入该文件夹，运行：
   ```bash
   # 预览模式（安全，不实际移动）
   .\FileWizard.exe "你的文件夹路径" --dry-run
   
   # 正式整理
   .\FileWizard.exe "你的文件夹路径"
   ```

> **提示：** 如果没有 `config.json`，程序会自动生成默认分类规则。你也可以复制项目根目录的 `config.json` 来自定义分类。

### 方式三：自己打包 exe

1. 克隆仓库并安装依赖：`pip install -r requirements.txt pyinstaller`
2. 运行打包命令：`pyinstaller -F --name FileWizard main.py`
3. 打包完成后，exe 文件位于 `dist/FileWizard.exe`

## 📋 支持的后缀（默认配置）

- **图片**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.bmp`
- **文档**: `.pdf`, `.docx`, `.doc`, `.txt`, `.md`, `.xlsx`, `.pptx`, `.csv`
- **视频**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`
- **音频**: `.mp3`, `.wav`, `.flac`
- **压缩包**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **程序脚本**: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.exe`, `.msi`

你可以直接修改 `config.json` 来自由定义分类规则。

## 🛠️ 项目结构

```
FileWizard/
├── .gitignore
├── README.md
├── config.json         # 分类规则配置文件
├── main.py             # 主程序入口
└── src/
    ├── __init__.py     # 包初始化
    ├── organizer.py    # 核心整理逻辑
    └── reporter.py     # 终端输出美化
```

## 💡 技术亮点

- 基于 JSON 配置文件，用户可以自己随意定义分类规则，无需改代码
- 零第三方复杂依赖，核心逻辑靠 Python 自带的 `pathlib` 和 `shutil` 搞定，稳健且运行极快
- 自动处理重名文件，避免覆盖
