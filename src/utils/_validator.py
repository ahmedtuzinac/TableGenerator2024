from scripts import error_messages, language


class Validator:
    """
        Class Validator

        public:
            methods: _validate
    """

    @staticmethod
    def _validate(data: dict, fields: dict, rtn: bool = True) -> tuple:
        """
            Method _validate validates that field's value type from data
            are same as provided in fields dict

            :param data: accepts dictionary of source data
            :param fields: accepts dictionary of key: field, value: type(field)
            :param rtn: bool, if True method returns values, else returns keys

            :return: tuple of field values, if validation is success
        """
        rtnv = tuple()
        for f in fields:
            v: fields[f] = data[f]
            assert isinstance(v, fields[f]), __class__._error_message(f, type(v), fields[f])
            rtnv += (v,) if rtn else (f,)

        return rtnv

    @staticmethod
    def _error_message(*args) -> str:
        """
            Method error_message creates error message for INVALID_TYPE

            :args:
                field_name: field name
                given_type: type of provided value
                expected_type: expected type of provided value
            :return:
        """

        error = f'{error_messages["INVALID_TYPE"][language]}'.replace('-', '\n')

        field_name: str = str(args[0]).upper()
        given_type: str = args[1].__name__.upper()
        expected_type: str = args[2].__name__.upper()

        error = error.format(field_name, expected_type, given_type)
        return error
