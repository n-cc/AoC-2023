import argparse

from common.file import get_input_from_file

parser = argparse.ArgumentParser()
parser.add_argument('input')

args = parser.parse_args()

def get_input() -> str:
    return get_input_from_file(args.input)