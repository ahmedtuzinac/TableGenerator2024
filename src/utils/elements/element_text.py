import pathlib

from utils import update_json

filepath = pathlib.Path(__file__)


def create(*args):
    var: str = args[1]
    value: str = args[0].get('value', '')

    try:
        update_json({var: value})
    except Exception:
        raise Exception(f'\nUPDATING_placeholders.json_ERROR\nPATH: {filepath}/{create.__name__}')
