

def get_diff(first_file_data: dict, second_file_data: dict) -> dict:
    common_keys = sorted(first_file_data.keys() | second_file_data.keys())

    """
    "action" field possible values 
    if field were present:
        - in first_file_data, but is not in second_file_data
                * removed (-)
        - in second_file_data, but not in first_file_data
                * added (+)
        - in both files:
            but values are not equal 
                * updated
            values are equal:
                * unchanged         
    """
    result = []

    for key in common_keys:
        if key not in second_file_data:
            result.append({
                'key': key,
                'value': first_file_data[key],
                'action': 'removed',
            })
        elif key not in first_file_data:
            result.append({
                'key': key,
                'value': second_file_data[key],
                'action': 'added',
            })
        elif first_file_data[key] == second_file_data[key]:
            result.append({
                'key': key,
                'value': second_file_data[key],
                'action': 'unchanged',
            })
        elif first_file_data[key] != second_file_data[key]:
            result.append({
                'key': key,
                'value': second_file_data[key],
                'action': 'updated',
                'value_diff': first_file_data[key],
            })

    return result
