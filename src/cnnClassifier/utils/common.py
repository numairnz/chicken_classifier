import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

import os
import yaml
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import json
import joblib
from cnnClassifier import logger




@ensure_annotations
def read_yaml1(path: Path )->ConfigBox:
    try:
        with open(path) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f'Yaml file at {path} is read')
            return ConfigBox(config)
    except Exception as e:
        raise e
@ensure_annotations
def create_directories(path_to_dirs : list , verbose  = True):
    for path in path_to_dirs:
        os.makedirs(path,exist_ok = True)
        if verbose == True:
            logger.info(f'Directory created at {path}')

@ensure_annotations
def save_json(data: dict , path: Path):
    with open(path,'w') as f:
        json.dump(data,f,indent = 4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path, 'w') as f:
        content = json.load(path)
    logger.info(f"json file loaded")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any, path = Any):
    joblib.dump(data,path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Any)->Any:
    data = joblib.load(path)
    return data


def get_size(path: Path)->str:
    size = round(os.path.getsize(path)/1024)
    return f'~{size}KB'



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
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
def create_directories1(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json1(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json1(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin1(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin1(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size1(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

