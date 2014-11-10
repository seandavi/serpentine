
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
   - bwa-freebayes
       + bwa alignment (100%)
	   + GATK processing (80%)
	   + freebayes calling (multisample)
	   + GATK VQSR
   - bwa-HaplotypeCaller
       + bwa alignment (100%)
	   + GATK processing (80%)
	   + freebayes calling (multisample)
	   + GATK VQSR
   - Novoalign-HaplotypeCaller
       + novoalign alignment 
	   + GATK processing (80%)
	   + freebayes calling (multisample)
	   + GATK VQSR
   - reporting
       + fastqc (100%)
	   + duplicate metrics (100%)
	   + recalibration tables (100%)
	   + alignment stats
2. Implement RNA-seq workflow
3. Implement Somatic workflows

## Conventions

- Sample names cannot have "/" or "." in them
- fastq files end in ".fastq.gz"

### output locations

```
$ tree -I 'serpentine|*fastqc*'
.
|-- RW1_ATCACG_L002.R1.250kreads.fastq.gz
|-- RW1_ATCACG_L002.R2.250kreads.fastq.gz
|-- RW2_CGATGT_L002.R1.250kreads.fastq.gz
|-- RW2_CGATGT_L002.R2.250kreads.fastq.gz
|-- RW3_TTAGGC_L003.R1.250kreads.fastq.gz
|-- RW3_TTAGGC_L003.R2.250kreads.fastq.gz
|-- RW4_TGACCA_L003.R1.250kreads.fastq.gz
|-- RW4_TGACCA_L003.R2.250kreads.fastq.gz
|-- RW5_ACAGTG_L003.R1.250kreads.fastq.gz
|-- RW5_ACAGTG_L003.R2.250kreads.fastq.gz
|-- config.json
|-- mapping
|   |-- human_g1k_v37
|   |   |-- samples
|   |   |   |-- RW1.bam.bai
|   |   |   |-- RW1.dupmetrics
|   |   |   |-- RW1.md.bam
|   |   |   |-- RW2.bam.bai
|   |   |   |-- RW2.dupmetrics
|   |   |   |-- RW2.md.bam
|   |   |   |-- RW3.bam.bai
|   |   |   |-- RW3.dupmetrics
|   |   |   |-- RW3.md.bam
|   |   |   |-- RW4.bam.bai
|   |   |   |-- RW4.dupmetrics
|   |   |   |-- RW4.md.bam
|   |   |   |-- RW5.bam.bai
|   |   |   |-- RW5.dupmetrics
|   |   |   `-- RW5.md.bam
|   |   `-- units
|   `-- log
|       `-- human_g1k_v37
|           |-- RW1_ATCACG_L002.log
|           |-- RW2_CGATGT_L002.log
|           |-- RW3_TTAGGC_L003.log
|           |-- RW4_TGACCA_L003.log
|           `-- RW5_ACAGTG_L003.log
|-- resources
|   `-- mapping
|       |-- human_g1k_v37.amb
|       |-- human_g1k_v37.ann
|       |-- human_g1k_v37.bwt
|       |-- human_g1k_v37.log
|       |-- human_g1k_v37.pac
|       `-- human_g1k_v37.sa
|-- snakemake.log
|-- snakemake.stats
|-- submit.sh

```
