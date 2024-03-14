import os
import pathlib
import uuid

from scripts import *
from utils import *
from elements import *
from models import *


def create_document(yaml_data: str, yaml_structure: str) -> None:
    # NOTE: here in format_data, validations are done by rules from structure.yaml,
    # NOTE: next step for validation are types of values
    import os
    output_dirpath = '/tmp/{}/'.format(uuid.uuid4())
    os.mkdir(output_dirpath)
    output_filepath = output_dirpath + 'output.docx'
    yaml_data: dict = format_data(yaml_data, yaml_structure)
    document = Document(template_filepath=yaml_filepath.format('template.docx'), output_filepath=output_filepath)
    created: bool = create_elements(yaml_data, document)
    ...
    # document.populate_placeholder(placeholders_filepath=pathlib.Path(__file__).parent.parent / 'placeholders.json'
    document.populate_placeholder(placeholders_filepath=pathlib.Path(__file__).parent.parent / 'placeholders.json')
    convert_to_pdf(output_filepath)
    output_pdf_filepath = output_dirpath + 'output.pdf'
    ...


def convert_to_pdf(docx_temp_filepath) -> None:
    import platform
    os_name = platform.system()
    soffice = 'soffice'
    if os_name == 'Darwin':
        soffice = '/Applications/LibreOffice.app/Contents/MacOS/soffice'

    cmd = [
        soffice,
        '--headless',
        '--convert-to', 'pdf',
        docx_temp_filepath,
        '--outdir', pathlib.Path(docx_temp_filepath).parent
    ]

    import subprocess
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while converting the file:", e)
        raise
    except Exception as e:
        print("An unexpected error occurred:", e)
        raise


if __name__ == '__main__':
    yaml_data_filepath = yaml_filepath.format('example.yaml')
    ...
    yaml_data: dict = open_yamlfile(yaml_data_filepath)

    create_document(yaml_data, yaml_structure['globals'])
