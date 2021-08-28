import argparse
from .genomes import add_build
from .formats import check_bigwig, check_bed

from enum import Enum, auto

def cli():
    parser = argparse.ArgumentParser(description='Figure out which genome build is likely from a particular file')
    parser.add_argument('path', help = "File", nargs = "+")
    parser.add_argument('-f', '--format', choices = ['bed', 'bigwig', 'auto', 'add_build'], default = "auto", help = "")
    parser.add_argument('-s', "--summary", default = False, action = 'store_true')
    parser.add_argument('-t', '--tol', default = 2, type = int)

    args = parser.parse_args()

    for file in args.path:
        if args.format == "auto":
            format = detect_filetype(file)
        else:
            format = args.format

        d = vars(args)
        d['path'] = file
        if format == "bigWig":
            check_bigwig(**vars(args))
        elif format == "bed":
            check_bed(**vars(args))
        elif format == "add_build":
            add_build(file)

# Do this later
class FileTypes(Enum):
    BED = auto()
    BIGWIG = auto()

def detect_filetype(path):
    if any([i in path.lower() for i in ['.bed']]):
        return "bed"
    elif any([i in path.lower() for i in ['.bigWig', '.bigwig', '.bw']]):
        return "bigWig"

    return NotImplementedError("Please specify the format of your file(s) using the -f flag.")