import os
from pathlib import Path
import yaml
import json
from src.adenocarcinoma_detection import logger
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    
    
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e: 
        raise e
    
    


@ensure_annotations
def create_directories(dir_path: list, verbose=True):
    
    
    for path in dir_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")  
            



@ensure_annotations
def get_size(path: Path) -> str:
    
    
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"

    

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)
