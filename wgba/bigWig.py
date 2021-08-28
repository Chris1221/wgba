import pandas as pd 
import pyBigWig

from .genomes import build_genomes

def check_bigwig(path, summary = False, tol = 2, **other):
    bw = pyBigWig.open(path)

    consistent = {}
    for g in build_genomes():
        consistent[g.build] = {}
        for chrom, length in bw.chroms().items():
            if chrom not in g.chroms():
                consistent[g.build][chrom] = False
                continue

            if length > g[chrom]:
                consistent[g.build][chrom] = False
            else:
                consistent[g.build][chrom] = True
    
    
    
    for g in consistent.keys():
        if summary: print(f"Not consistent with {g}:")
        n_not = 0
        for chrom in consistent[g].keys():
            if not consistent[g][chrom]:
                n_not += 1
                if summary: print(f"\t{chrom}") 

        if n_not < tol:
            print(f"This is probably {g}.") 

    
