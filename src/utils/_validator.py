from scripts import error_messages, language


class Validator:
    """
        Class Validator

        public:
            methods: _validate
    """

    @staticmethod
    def _validate(data: dict, fields: dict, error_msg: str, rtn: bool = True) -> tuple:
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
            v: fields[f] = data.get(f)
            assert isinstance(v, fields[f]), __class__._error_message(f.upper(),
                                                                      fields[f].__name__.upper(),
                                                                      type(v).__name__.upper(),
                                                                      error_msg=error_msg)
            rtnv += (v,) if rtn else (f,)

        return rtnv

    @staticmethod
    def _error_message(*args, error_msg: str) -> str:
        """
            Method error_message creates error message

            :args: vars to be formatted in message
            :param error_msg: message structure string

            :return: sting error message
        """

        try:
            error = f'{error_msg}'.replace('-', '\n')
            error = error.format(*args)
        except Exception:
            raise

        return error
