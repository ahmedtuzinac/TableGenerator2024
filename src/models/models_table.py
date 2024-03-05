from docx import document


class Table:
    """
        class Table, 2024-02-27
    """

    def __init__(self, **kwargs: dict):
        self.columns: list[dict] = kwargs.get('columns')
        self.rows: list[any] = kwargs.get('rows')
