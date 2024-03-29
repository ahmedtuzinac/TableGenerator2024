from scripts import *
from utils import *
from elements import *


def create_document(yaml_data: str, yaml_structure: str) -> None:
    yaml_data: dict = format_data(yaml_data, yaml_structure)
    created: bool = create_elements(yaml_data)
    ...


if __name__ == '__main__':
    yaml_data_filepath = yaml_filepath.format('example.yaml')
    ...
    yaml_data: dict = open_yamlfile(yaml_data_filepath)

    create_document(yaml_data, yaml_structure['globals'])
