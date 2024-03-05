import pathlib
from pathlib import PosixPath

import yaml

from models import *

filepath: PosixPath = pathlib.Path(__file__)
yaml_filepath: str = '{}/{}'.format(str(filepath.parent.parent.parent), 'assets/{}')
placeholders_json_filepath = str(pathlib.Path(__file__).parent.parent / 'placeholders.json')


def open_yamlfile(yaml_filepath: str) -> dict:
    try:
        with open(yaml_filepath, 'r') as file:
            yaml_data: dict = yaml.load(file, Loader=yaml.FullLoader)
    except Exception as e:
        raise e

    return yaml_data


yaml_structure_filepath: str = yaml_filepath.format('structure.yaml')
yaml_structure: dict = open_yamlfile(yaml_structure_filepath)
