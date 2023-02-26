import argparse
import read_edf

arg_parser = argparse.ArgumentParser(description='Takes an edf file path and prints the info')
arg_parser.add_argument('--file_path', type=str, help='edf file path')
args = arg_parser.parse_args()
file_path = args.file_path
read_edf.print_edf_info(file_path)
