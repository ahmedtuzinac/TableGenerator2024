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
        status = Element._create(variable=v,
                                 definition=definitions[v])
