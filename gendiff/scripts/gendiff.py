import argparse


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


if __name__ == "__main__":
    main()
