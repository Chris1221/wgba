# Which genome build again?

[![PyPI version](https://badge.fury.io/py/wgba.svg)](https://badge.fury.io/py/wgba) [![Downloads](https://pepy.tech/badge/wgba)](https://pepy.tech/project/wgba) [![CircleCI](https://circleci.com/gh/Chris1221/wgba/tree/main.svg?style=svg)](https://circleci.com/gh/Chris1221/wgba/tree/main) [![codecov](https://codecov.io/gh/Chris1221/wgba/branch/main/graph/badge.svg?token=fp2S6CX5fq)](https://codecov.io/gh/Chris1221/wgba)

A species-agnostic tool to figure out the probable genome build of a file. Currently supports bigWig and bed files, and an easy method to add your own genome build.

Install with `pip`

```{sh}
pip install wgba
```

https://user-images.githubusercontent.com/8516981/133273821-cac95fdf-cfa4-48de-8760-72b7f442cfe5.mp4


## Usage:

Auto detect file extension

```{sh}
wgba your_file.bed
```

Use a specific file extension, if your extension is non-standard for example

```{sh}
wgba -f bed your_file.bed
wgba -f bigwig your_file.bigWig
```

You can use shell globs to match multiple files, all of which will be processed independently

```{sh}
wgba *.bed 
```

You can mix and match supported files

```{sh}
wgba a_bed_file.bed and_a_bigwig.bw and_another.bigWig
```

Check if all of your files are on the same build with `-c`, `--check` 

```{sh}
wgba -c *.bed *.bw 
```

Summarise non-conforming chromosomes with `-s`, `--summary`

```{sh}
wgba -s bad_file.bed
```

Adjust the tolerance for build assignment with `-t`, `--tol`. This is useful if you know that one chromosome will never match.

```{sh}
wgba -t 2 one_bad_chromosome.bed
```

Add a genome build to the database

```{sh}
wgba -f add_build your_build.chrom.sizes
```

## Issues

This was written in about an hour for my own use. If you find something not working, please [raise an issue](https://github.com/Chris1221/wgba/issues/new/choose).

