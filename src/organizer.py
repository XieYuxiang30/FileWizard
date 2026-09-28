import json
import shutil
from pathlib import Path


def load_config(config_path):
    # 读取配置文件
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_target_folder(file_suffix, config):
    # 根据文件后缀判断应该放入哪个文件夹
    file_suffix = file_suffix.lower()
    for folder_name, extensions in config.items():
        if file_suffix in extensions:
            return folder_name
    # 如果没找到匹配的，统一放入"其他"
    return "其他"


def organize_directory(target_dir, config_path, dry_run=False):
    # 核心整理函数
    # :param target_dir: 需要整理的文件夹路径
    # :param config_path: 配置文件的路径
    # :param dry_run: 是否开启预览模式（True则不实际移动文件）
    # :return: 整理报告字典
    target_path = Path(target_dir)
    if not target_path.exists() or not target_path.is_dir():
        return {"error": f"找不到文件夹: {target_dir}"}

    config = load_config(config_path)
    report = {key: 0 for key in config.keys()}
    
    # 遍历目标文件夹下的所有内容
    for item in target_path.iterdir():
        # 跳过文件夹和隐藏文件，只处理普通文件
        if item.is_dir() or item.name.startswith('.'):
            continue
            
        # 获取后缀，比如 .pdf
        suffix = item.suffix
        if not suffix:
            # 没有后缀的文件（比如 README），统一放入"其他"
            target_folder_name = "其他"
        else:
            target_folder_name = get_target_folder(suffix, config)
            
        # 构建目标文件夹路径
        dest_folder = target_path / target_folder_name
        
        # 如果是预览模式，只记录，不实际移动
        if dry_run:
            report[target_folder_name] += 1
            print(f"[预览] 将移动: {item.name} -> {target_folder_name}/")
        else:
            # 真正执行移动
            dest_folder.mkdir(exist_ok=True) # 文件夹不存在则创建
            dest_file = dest_folder / item.name
            
            # 处理重名文件：如果目标位置已有同名文件，加上数字后缀
            counter = 1
            while dest_file.exists():
                dest_file = dest_folder / f"{item.stem}({counter}){item.suffix}"
                counter += 1
                
            shutil.move(str(item), str(dest_file))
            report[target_folder_name] += 1
            
    return report
