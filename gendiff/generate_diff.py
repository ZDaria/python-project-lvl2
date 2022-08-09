import json
from gendiff.diff import get_diff


def get_decoding_json(diff_value):
    return dict(sorted(json.loads(diff_value).items(),
                       key=lambda item: item[0]))


def get_data_from_file(file, _type='json') -> dict:
    file_data = ''
    with open(file, "r") as _file:
        for line in _file:
            file_data += line
    if _type == 'json':
        return get_decoding_json(file_data)


def generate_diff(first_file: str, second_file: str, format_: str) -> str:
    data_1 = get_data_from_file(first_file)
    data_2 = get_data_from_file(second_file)
    print(data_1)
    print(data_2)
    file_diff = get_diff(data_1, data_2)
    print(file_diff)
    return 'ok'
