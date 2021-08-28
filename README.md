# Which genome build again?

A species-agnostic tool to figure out the probable genome build of a file. To add a new genome build, copy the `${BUILD}.chrom.sizes` file into `wgba/sizes/` and it will be automatically detected.

Usage:

```{sh}
wgca -f bed your_file.bed
wgca -f bigwig your_file.bigWig
wgca -f bed bed1.bed bed2.bed bed3.bed
wgca -f bed *.bed
```