import json

from scripts import *
from utils import *


def create_elements(data: dict) -> bool:
    variables, definitions = Validator._validate(data=data,
                                                 fields={'variables': list, 'definitions': dict},
                                                 error_msg=error_messages["INVALID_INPUT"][language])

    for v in variables:
        _ = Validator._validate(data=definitions,
                                fields={v: dict}, error_msg=error_messages['INVALID_DEFINITON'][language])

        _ = Validator._validate(data=definitions[v],
                                fields={'type': str}, error_msg='-DEFINITION_{}'.format(v) + \
                                                                error_messages['NOT_FOUND'][language])
    status = Element.create(variables=variables,
                            definitions=definitions)


# NOTE: here does not have to be any validation... Everything should be in _validator/Validator
def create_element(element_name: str, element_data: dict) -> bool:
    defs = yaml_structure.get('functions')
    element_type = element_data.get('type')

    execute = globals()[defs[element_type]]
    execute(element_name=element_name, element_data=element_data)


def create_text(**kwargs):
    element_name = kwargs.get('element_name')
    element_data = kwargs.get('element_data')

    value = element_data.get('value')

    update_json({element_name: value})


def create_table(**kwargs):
    ...
