import json

from scripts import *
from utils import *


def create_elements(data: dict) -> bool:

    variables, definitions = Validator._validate(data=data,
                                                 fields={'variables': list, 'definitions': dict})

    for v in variables:
        # try:
        #     element_data: dict = definitions[variable]
        # except Exception:
        #     raise ElementDefinitionNotFoundError('\nNOT_FOUND_DEFINITION\n'
        #                                          'VARIABLE: {}'.format(str(variable)))
        # element = create_element(str(variable), element_data)
        ...


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
