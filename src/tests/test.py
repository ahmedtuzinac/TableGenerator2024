import pathlib
import pytest

from scripts import open_yamlfile, yaml_filepath


class Test:
    invalid_data: dict
    template_filepath: str
    yaml_structure: dict
    yaml_data: dict

    @pytest.fixture(autouse=True)
    def setup(self):
        self.template_filepath: str = str(pathlib.Path(__file__).parent.parent.parent / 'assets/template.docx')
        self.yaml_structure: dict = open_yamlfile(yaml_filepath=yaml_filepath.format('structure.yaml'))
        self.yaml_data: dict = open_yamlfile(yaml_filepath=yaml_filepath.format('example.yaml'))
        self.invalid_data: dict = open_yamlfile(yaml_filepath=pathlib.Path(__file__).parent / 'assets/invalid_format.yaml')
