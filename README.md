# Which genome build again?

A species-agnostic tool to figure out the probable genome build of a file. Currently supports bigWig and bed files, and an easy method to add your own genome build.

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

You can use shell globs to match multiple files, all of which will be processed independantly

```{sh}
wgba *.bed 
```

You can mix and match supported files

```{sh}
wgba a_bed_file.bed and_a_bigwig.bw and_another.bigWig
```

Summarise non-conforming chromosomes with `-s`, `--summary`

```{sh}
wgba -s bad_file.bed
```

Adjust the tolerance for build assignemnt with `-t`, `--tol`. This is useful if you know that one chromosome will never match.

```{sh}
wgba -t 2 one_bad_chromosome.bed
```

Add a genome build to the database

```{sh}
wgba -f add_build your_build.chrom.sizes
```
