from utils import format_data
from scripts import open_yamlfile
from test import Test

filepath = pathlib.Path(__file__)


class TestFormat(Test):

    def test_invalid_format_yaml(self):
        try:
            format_data(yaml_data=self.invalid_data, yaml_structure=self.yaml_structure['globals'])
            assert False
        except InvalidInput as e:
            self.invalid_data = {}
            assert e.args[0] == error_messages['NOT_FOUND'][language].format('DEFINITIONS').replace('-', '\n')
        except Exception:
            assert False
