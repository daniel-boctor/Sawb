import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--delimiter',  default=' ', type=str, help='Specificy the delimiter for the file names.')
parser.add_argument('-o', '--output',  default='index', type=str, help='Specificy the file name you would like to write to.')
parser.add_argument('-t', '--output_type',  default='txt', type=str, help='Specificy weather the output file should be a txt or a csv.')
parser.add_argument('-f', '--directory_path',  default='.', type=str, help='Specificy the directory to index from.')
parser.add_argument('-s', '--save_path',  default='', type=str, help='Specificy the save location.')

args = parser.parse_args()

raw_file_names = [f for f in os.listdir(args.directory_path) if os.path.isdir(os.path.join(args.directory_path, f))]

with open(os.path.join(args.save_path, f"{args.output}.{args.output_type}"), "w") as output:
    for file in raw_file_names: output.write(file.split(args.delimiter)[0] + ('\n' if args.output_type=="txt" else ','))