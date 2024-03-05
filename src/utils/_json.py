import json

from scripts import placeholders_json_filepath


def update_json(updated_data: dict) -> None:
    try:
        with open(placeholders_json_filepath, 'r') as file:
            data = json.load(file)
    except Exception as e:
        data = {}

    data.update(updated_data)

    with open(placeholders_json_filepath, 'w') as file:
        json.dump(data, file, indent=4)
