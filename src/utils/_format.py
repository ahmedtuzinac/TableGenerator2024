from models import *
from scripts import *


def format_data(yaml_data: dict, yaml_structure: dict, key: str = None) -> dict:
    """
        We are reading paths and extracting values from data*.yaml,
        by the rules writen in structure.yaml.

        :param yaml_data: dictionary with data from request
        :param yaml_structure: dictinary with lookups for paths
        :param key: if some path is dynamic, just pass key

        :return data: dictinary with keys of necessary elements from data
    """

    data = {}
    for d in yaml_structure:
        path = yaml_structure[d]
        if key:
            path: str = format_path(path, key)
        try:
            value: any = eval(f'yaml_data{path}')
            data[d] = value

        except Exception:
            error: str = error_messages['NOT_FOUND'][language].replace('{}', d.upper()).replace('-', '\n')
            raise InvalidInput(error)
    return data


def format_path(path: str, key: str) -> str:
    return path.format(key)
