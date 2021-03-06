
## Introduction

Serpentine is a project that leverages the snakemake workflow management to create a flexible, efficient, and highly parallelizable pipelines for data analysis.  The current focus is on DNA sequence analysis, but there is no limitation on the workflows that can be implemented.  We have definite plans for RNA-seq and combined RNA/DNA pipelines in the works.  Additional pipeline suggestions are welcome. 

## Current capabilities

Serpentine can currently run workflows composed of any combination of the following steps.  The steps are run in a fully-parallel manner based on job dependencies and available resources.  The whole process is driven by a json config file [(example config file)](https://github.com/NCI-CCR-GB/serpentine/blob/master/workflows/variant_calling/config.json).

- aligners: 
    - novoalign
    - bwa-mem
- postprocessing: 
    - Duplicate marking
    - realignment around indels
    - base quality recalibration
- variant callers:
    - germline:
        - UnifiedGenotyper
        - HaplotypeCaller
        - Freebayes
        - platypus
        - pindel
- metrics:
    - insert size
    - quality metrics
    - alignment summary metrics
    - duplication metrics

## Graphical representation of variant calling workflow

![](https://raw.githubusercontent.com/NCI-CCR-GB/serpentine/master/workflows/variant_calling/serpentine.jpg)


=======
## Installation

The easiest way to get serpentine is to clone the repository.

```
git clone https://github.com/NCI-CCR-GB/serpentine.git
```

## Contributing

To contribute to the project, you can:

1. File a [new issue](https://github.com/NCI-CCR-GB/serpentine/issues/new)
2. [Fork](https://github.com/NCI-CCR-GB/serpentine/fork) the repository, make changes, and then make a pull request.

If you have questions, file a [new issue](https://github.com/NCI-CCR-GB/serpentine/issues/new) and label as a question or [email me](mailto:seandavi@gmail.com).


## Conventions

- Sample names cannot have "/" or "." in them
- fastq files end in ".fastq.gz"

### output locations

### Config file example

An example config file is [available here](https://github.com/NCI-CCR-GB/serpentine/blob/master/workflows/variant_calling/config.json).
