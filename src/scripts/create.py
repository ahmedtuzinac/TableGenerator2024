import os
import pathlib
import uuid

from scripts import *
from utils import *
from elements import *
from models import *


def create_document(yaml_data: str, yaml_structure: str) -> None:
    # NOTE: here in format_data, validations are done by rules from structure.yaml,
    # NOTE: next step for validation are types of values

    yaml_data: dict = format_data(yaml_data, yaml_structure)
    created: bool = create_elements(yaml_data)
    import os
    output_dirpath = '/tmp/{}/'.format(uuid.uuid4())
    os.mkdir(output_dirpath)
    output_filepath = output_dirpath + 'output.docx'
    ...
    document = Document(template_filepath=yaml_filepath.format('template.docx'), output_filepath=output_filepath)
    document.populate_placeholder(placeholders_filepath=pathlib.Path(__file__).parent.parent / 'placeholders.json')
    ...

    import shutil

    try:
        shutil.rmtree(output_dirpath)
        print(f"DIR_{output_dirpath}_DELETED")
    except FileNotFoundError:
        print(f"Directory {output_dirpath} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    yaml_data_filepath = yaml_filepath.format('example.yaml')
    ...
    yaml_data: dict = open_yamlfile(yaml_data_filepath)

    create_document(yaml_data, yaml_structure['globals'])
