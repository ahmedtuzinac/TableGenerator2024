from scripts import *
from ._validator import Validator


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
        except Exception:
            assert False, Validator._error_message(var, definition['type'].upper(),
                                                   error_msg=error_messages['INVALID_TYPE'][language])

    @staticmethod
    def _create_text(*args: tuple):
        from ._json import update_json
        update_json({args[1]: args[0].get('value')})

    @staticmethod
    def _create_table(*args: tuple):
        ...
