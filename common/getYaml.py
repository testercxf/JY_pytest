import os
import yaml
from typing import Dict, Any

class Getyaml:
    """YAML文件读取工具类"""
    
    def read_yaml_file(self, yaml_name: str, part: str) -> Dict[str, Any]:
        """
        读取YAML文件中的特定部分
        
        Args:
            yaml_name: YAML文件名
            part: 要读取的部分名称
            
        Returns:
            Dict: 读取的YAML数据
            
        Raises:
            FileNotFoundError: 文件不存在时抛出
            KeyError: 指定的部分不存在时抛出
        """
        file_path = os.path.join(os.getcwd(), 'testdata', yaml_name)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"YAML文件不存在: {file_path}")
            
        with open(file_path, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            
            if part not in value:
                raise KeyError(f"在YAML文件中找不到指定部分: {part}")
                
            return value[part]
