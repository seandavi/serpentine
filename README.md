
## Introduction

Serpentine is, so far, a collection of rules and workflows for NGS data processing.
It is in development.

## Contributing

To contribute to the project, you can:

1. File a [new issue](https://github.com/seandavi/serpentine/issues/new)
2. [Fork](https://github.com/seandavi/serpentine/fork) the repository, make changes, and then make a pull request.

If you have questions, file a [new issue](https://github.com/seandavi/serpentine/issues/new) and label as a question or [email me](mailto:seandavi@gmail.com).


## Roadmap

1. Implement germline workflow(s) for DNA
   - bwa-freebayes (90% complete)
       + bwa alignment 
	   + GATK processing 
	   + freebayes calling (multisample)
	   + GATK VQSR (TODO)
   - bwa-HaplotypeCaller
       + bwa alignment (100%)
	   + GATK processing (100%)
	   + Haplotype Caller (TODO)
	   + GATK VQSR (TODO)
   - Novoalign-HaplotypeCaller
       + novoalign alignment (TODO)
	   + GATK processing (100%)
	   + Haplotype Caller (TODO)
	   + GATK VQSR (TODO)
   - reporting
       + fastqc (100%)
	   + duplicate metrics (100%)
	   + recalibration tables (100%)
	   + alignment stats (TODO)
2. Implement RNA-seq workflow
   - STAR (1-pass)
   - STAR (2-pass)?
3. Implement Somatic workflows
   - bwa-mutect
   - bwa-strelka
   - novoalign-mutect
   - novoalign-strelka

## Conventions

- Sample names cannot have "/" or "." in them
- fastq files end in ".fastq.gz"

### output locations

- Alignment
```
mapping/{reference}/{aligner}/sample....bam
```

- Variants
```
variants/{reference}/{aligner}/{variant_caller}/variants.vcf
```

- QC
```
QC/fastqc/FASTQNAME_fastqc/....
```

### Config file example

An example config file is [available here](https://github.com/NCI-CCR-GB/serpentine/blob/master/example/example.json).
