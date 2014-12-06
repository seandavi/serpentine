**PLEASE NOTE: Development has now moved to the NCI-CCR-GB organization page here:**

https://github.com/NCI-CCR-GB/serpentine




## Introduction

Serpentine is, so far, a collection of rules and workflows for NGS data processing.
It is in development.

## Installation

The easiest way to get serpentine is to clone the repository.

```
git clone https://github.com/zhujack/serpentine.git
```

## Contributing

To contribute to the project, you can:

1. File a [new issue](https://github.com/NCI-CCR-GB/serpentine/issues/new)
2. [Fork](https://github.com/NCI-CCR-GB/serpentine/fork) the repository, make changes, and then make a pull request.

If you have questions, file a [new issue](https://github.com/NCI-CCR-GB/serpentine/issues/new) and label as a question or [email me](mailto:seandavi@gmail.com).


## Roadmap (to be updated)

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
$ tree [analysis_dir]

STUDY/
`-- variant
    `-- human_g1k_v37.bwamem
        |-- freebayes_all.vcf.gz
        |-- freebayes_all.vcf.gz.tbi
        |-- unifieldgenotyper_all.vcf.gz
        |-- unifieldgenotyper_all.vcf.gz.tbi
        `-- unifieldgenotyper_all.vcf.idx
SUBJECT/
|-- NA12878
|   `-- NA12878_DNA
|       `-- human_g1k_v37.bwamem
|           |-- bam
|           |   |-- NA12878_DNA.final.bai
|           |   |-- NA12878_DNA.final.bam
|           |   |-- NA12878_DNA.final.bam.bai
|           |   `-- NA12878_DNA.final.bam.tdf
|           |-- freebayes
|           |   |-- NA12878_DNA.freebayes.vcf.gz
|           |   `-- NA12878_DNA.freebayes.vcf.gz.tbi
|           |-- germline_compare
|           |-- haplotypecaller
|           |   |-- NA12878_DNA.haplotypecaller.vcf.gz
|           |   |-- NA12878_DNA.haplotypecaller.vcf.gz.tbi
|           |   `-- NA12878_DNA.haplotypecaller.vcf.idx
|           |-- mutect
|           |   |-- NA12878_DNA_vs_NA12891_DNA.mutect.call_stats.txt
|           |   |-- NA12878_DNA_vs_NA12891_DNA.mutect.coverage.wig.txt
|           |   |-- NA12878_DNA_vs_NA12892_DNA.mutect.call_stats.txt
|           |   `-- NA12878_DNA_vs_NA12892_DNA.mutect.coverage.wig.txt
|           |-- pindel
|           |   |-- NA12878_DNA.pindel.txt
|           |   |-- NA12878_DNA.pindel.vcf.gz
|           |   |-- NA12878_DNA.pindel.vcf.gz.tbi
|           |   |-- NA12878_DNA.pindel_BP
|           |   |-- NA12878_DNA.pindel_CloseEndMapped
|           |   |-- NA12878_DNA.pindel_D
|           |   |-- NA12878_DNA.pindel_INT_final
|           |   |-- NA12878_DNA.pindel_INV
|           |   |-- NA12878_DNA.pindel_LI
|           |   |-- NA12878_DNA.pindel_RP
|           |   |-- NA12878_DNA.pindel_SI
|           |   `-- NA12878_DNA.pindel_TD
|           |-- platypus
|           |   |-- NA12878_DNA.platypus.log
|           |   |-- NA12878_DNA.platypus.vcf.gz
|           |   `-- NA12878_DNA.platypus.vcf.gz.tbi
|           |-- qc
|           |   |-- NA12878_DNA.final.bam.base_distribution_by_cycle.pdf
|           |   |-- NA12878_DNA.final.bam.base_distribution_by_cycle_metrics
|           |   |-- NA12878_DNA.final.bam.insert_size_Histogram.pdf
|           |   |-- NA12878_DNA.final.bam.insert_size_metrics
|           |   |-- NA12878_DNA.final.bam.quality_by_cycle.pdf
|           |   |-- NA12878_DNA.final.bam.quality_by_cycle_metrics
|           |   |-- NA12878_DNA.final.bam.quality_distribution.pdf
|           |   |-- NA12878_DNA.final.bam.quality_distribution_metrics
|           |   `-- NA12878_DNA.final.bam.summetrics
|           |-- strelka
|           |   |-- NA12878_DNA_vs_NA12891_DNA.strelka.indels.vcf.gz
|           |   |-- NA12878_DNA_vs_NA12891_DNA.strelka.indels.vcf.gz.tbi
|           |   |-- NA12878_DNA_vs_NA12891_DNA.strelka.snvs.vcf.gz
|           |   |-- NA12878_DNA_vs_NA12891_DNA.strelka.snvs.vcf.gz.tbi
|           |   |-- NA12878_DNA_vs_NA12892_DNA.strelka.indels.vcf.gz
|           |   |-- NA12878_DNA_vs_NA12892_DNA.strelka.indels.vcf.gz.tbi
|           |   |-- NA12878_DNA_vs_NA12892_DNA.strelka.snvs.vcf.gz
|           |   `-- NA12878_DNA_vs_NA12892_DNA.strelka.snvs.vcf.gz.tbi
|           `-- unifieldgenotyper
|               |-- NA12878_DNA.unifieldgenotyper.vcf.gz
|               |-- NA12878_DNA.unifieldgenotyper.vcf.gz.tbi
|               `-- NA12878_DNA.unifieldgenotyper.vcf.idx
..

```
