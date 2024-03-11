from utils import *
from scripts import open_yamlfile
from test import Test

filepath = pathlib.Path(__file__)


class TestFormat(Test):

    def open_data(self, filename):
        yaml_data: dict = open_yamlfile(filepath.parent / 'assets/{}'.format(filename))
        return yaml_data

    def test_invalid_format_yaml(self):
        data = self.open_data('invalid_format.yaml')

        try:
            format_data(yaml_data=data, yaml_structure=self.yaml_structure['globals'])
            assert False
        except InvalidInput as e:
            assert e.args[0] == error_messages['NOT_FOUND'][language].format('DEFINITIONS').replace('-', '\n')
        except Exception:
            assert False
