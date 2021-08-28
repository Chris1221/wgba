import argparse
from .bigWig import check_bigwig

def cli():
    parser = argparse.ArgumentParser(description='Figure out which genome build is likely from a particular file')
    parser.add_argument('path', help = "File")
    parser.add_argument('-s', "--summary", default = False, action = 'store_true')
    parser.add_argument('-t', '--tol', default = 2)

    args = parser.parse_args()
    check_bigwig(**vars(args))
    