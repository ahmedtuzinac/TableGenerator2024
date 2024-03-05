import pathlib
import pytest

from models import *
from test import Test


class TestDocument(Test):

    def test_open_document(self):
        document = Document(template_filepath=self.template_filepath)
        try:
            document.open_template()
            assert True
        except TemplateNotFoundError:
            assert False

    def test_open_document_with_invalid_template_filepath(self):
        invalid_template_filepath = self.template_filepath + '1'
        document = Document(template_filepath=invalid_template_filepath)
        try:
            document.open_template()
            assert False
        except TemplateNotFoundError:
            assert True
