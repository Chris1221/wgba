import argparse
from .formats import check_bigwig, check_bed

def cli():
    parser = argparse.ArgumentParser(description='Figure out which genome build is likely from a particular file')
    parser.add_argument('path', help = "File", nargs = "+")
    parser.add_argument('-f', '--format', choices = ['bed', 'bigwig'], help = "")
    parser.add_argument('-s', "--summary", default = False, action = 'store_true')
    parser.add_argument('-t', '--tol', default = 2, type = int)


    args = parser.parse_args()
    for file in args.path:
        d = vars(args)
        d['path'] = file
        if args.format == 'bigwig':
            check_bigwig(**vars(args))
        elif args.format == 'bed':
            check_bed(**vars(args))



    