import sys

import pathlib
import docx

from scripts import *
from ._validator import Validator

filepath = pathlib.Path(__file__)


class Element:
    """
        Class Element

        public:
            methods: create
    """

    @staticmethod
    def _create(**kwargs: dict) -> bool:
        var = kwargs.get('variable')
        definition = kwargs.get('definition')

        func = getattr(Element, '_create_{}'.format(definition['type']), None)
        try:
            func(definition, var)
        except TypeError:
            assert False, Validator._error_message(var, definition['type'].upper(),
                                                   error_msg=error_messages['INVALID_TYPE'][language])
        except Exception as e:
            raise e

    @staticmethod
    def _create_text(*args: tuple):
        from .elements.element_text import create
        try:
            create(*args)
        except Exception as e:
            raise e

    @staticmethod
    def _create_table(*args: tuple):
        from .elements.element_table import create
        try:
            create(*args)
        except Exception as e:
            raise e
