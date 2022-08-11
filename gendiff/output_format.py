

def get_diff_str(diff: dict) -> str:
    output_str_diff = ''
    for line in diff:
        print(line)
        if line['action'] == 'removed':
            action = '-'
        elif line['action'] == 'unchanged':
            action = ' '
        elif line['action'] == 'added':
            action = '+'
        elif line['action'] == 'updated':
            output_str_diff += '{0} {1}: {2} \n'.format('-', line['key'],
                                                        line['value_diff'])
            action = '+'
        output_str_diff += '{0} {1}: {2} \n'.format(action, line['key'],
                                                    line['value'])

    return '{{\n {0}}}'.format(output_str_diff)
