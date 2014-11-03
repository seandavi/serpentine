## Conventions

- Sample names cannot have "/" or "." in them
- fastq files end in ".fastq.gz"

## output locations

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
