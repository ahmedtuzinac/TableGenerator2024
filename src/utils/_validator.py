from scripts import error_messages, language


class Validator:
    @staticmethod
    def _validate(data: dict, fields: dict) -> tuple:
        """
            Method _validate validates that field's value type from data
            are same as provided in fields dict

            :param data: accepts dictionary of source data
            :param fields: accepts dictionary of key: field, value: type(field)

            :return: tuple on field values, if validation is success
        """

        for f in fields:
            v: any = data[f]
            assert isinstance(v, fields[f]), __class__.error_message(f, v, fields[f])
            ...

    @staticmethod
    def error_message(*args):
        ...
