import argparse
import sys
import errno
import os


from pathlib import Path
from zap2rst import zap2rst

DESCRIPTION = '''
    Convert Whatsapp exported files to RestructuredText ..., then html or pdf.

    Media Files (pictures, audio em movies) when not informed,
    will be searched on the same path as conversation file.
'''


def check_file(filepath, raise_file_not_found=True):
    '''
    check is a file exists.

    Return

        If check fails,
            and the arg `raise_file_not_found` is True it raises a proper error.

            and  the arg `raise_file_not_found` is False, it returns `False`

        otherwise return True
    '''
    path = Path(filepath)  # name suffix stem

    is_file = path.is_file()
    if not is_file and raise_file_not_found:
        is_file = False
        raise FileNotFoundError(
            errno.ENOENT,
            os.strerror(errno.ENOENT),
            filepath
        )
        exit()
    return is_file


def get_base_path(filepath):
    check_file(filepath)
    path, file_name = os.path.split(filepath)
    return path


def command_line_parser(sys_args):
    '''
    define command line args return the argparse namespace object
    '''
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        epilog=''
    )
    parser.add_argument(
        'input',
        help='whatsapp text file name (a `.txt` file) - remember to use `"` if filename has spaces')
    parser.add_argument(
        '-m', '--mediapath',
        type=str,
        help='path for media files')
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='output file name - generated ResructuredText ')

    args = parser.parse_args(sys_args)
    return args


def main(args):

    check_file(args.input)

    # if media path is informed supress base path
    media_path = args.mediapath or get_base_path(args.input)

    # start to export.
    rst_file_name = zap2rst.output(args.input, media_path)

    return rst_file_name


if __name__ == '__main__':
    args = command_line_parser(sys.argv[1:])
    file = main(args)
    print(f'Output generated: {file.name}')
