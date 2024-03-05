import pathlib

import docx

from .models_table import Table
from .models_exceptions import *


class Document:
    """
        class Document, 2024-02-27
    """
    document: docx.document.Document | None = None

    def __init__(self, **kwargs: dict):
        self.kwargs: dict = kwargs
        self.set_attrs()

    def set_attrs(self):
        for k, v in self.kwargs.items():
            setattr(self, k, v)
        del self.kwargs

    def open_template(self):
        try:
            self.document = docx.Document(self.template_filepath)
            return
        except Exception:
            self.document = None
            raise TemplateNotFoundError('\nERROR: TEMPLATE_NOT_FOUND\nPATH: {}'.format(self.template_filepath))

    # def add_table(self, table: Table) -> bool:
    #     ...
    #
    # def create(self):
    #     ...
