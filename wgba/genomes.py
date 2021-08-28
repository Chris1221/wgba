import pkg_resources

hg19 = pkg_resources.resource_filename('wgba.sizes', 'hg19.chrom.sizes')
grch38 = pkg_resources.resource_filename('wgba.sizes', 'grch38.chrom.sizes')

class Genome:
    def __init__(self, name):
        self.sizes = {}
        self.build = name
        path = self.genome_path(name)

        with open(path) as f:
            for line in f:
                chrom, length = line.strip().split()
                self.sizes[chrom] = int(length)
    
    def __getitem__(self, key):
        return self.sizes[key]

    def items(self):
        return self.sizes.items()

    def chroms(self):
        return [k for k in self.sizes.keys()]

    def size_of(self, chrom):
        return self.sizes[chrom]

    def genome_path(self, name):
        return pkg_resources.resource_filename('wgba.sizes', f'{name}.chrom.sizes')
        # Try except here for names not found

def build_genomes():
    genomes = []
    for g in ["hg19", "grch38"]:
        genomes.append(Genome(g))
    
    return genomes