import os
from box.exceptions import BoxValueError
import yaml
from Paragraph_Summerizer.logging import logger
from box import config_box
from pathlib import Path
from typing import Any
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> config_box:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} as been loaded successfully")
            return config_box(content)
    except BoxValueError:
        raise BoxValueError
    except Exception as e:
        return e
    
@ensure_annotations
def makedirs(path_of_dir : list,verbose = True):
    for path in path_of_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def get_size(path:Path)->str:
    sizeInkb = round(os.path.getsize(path)/1024)
    return f"file size is {sizeInkb}"