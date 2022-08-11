import argparse
from gendiff.generate_diff import generate_diff
from gendiff.output_format import get_diff_str


def main(first_file=None, second_file=None, format_=None):
    parser = argparse.ArgumentParser(description='Compares two configuration '
                                                 'files and shows a '
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='json')

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    format_ = args.format
    diff = generate_diff(first_file=first_file, second_file=second_file,
                         format_=format_)
    print(get_diff_str(diff))


if __name__ == "__main__":
    main()
