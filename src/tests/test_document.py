import pathlib
import pytest

from models import *
from test import Test


class TestDocument(Test):

    def test_open_document(self):
        try:
            _ = Document(template_filepath=self.template_filepath)
            assert True
        except TemplateNotFoundError:
            assert False

    def test_open_document_with_invalid_template_filepath(self):
        invalid_template_filepath = self.template_filepath + '1'
        try:
            _ = Document(template_filepath=invalid_template_filepath)
            assert False
        except TemplateNotFoundError as e:
            assert type(e) == TemplateNotFoundError
