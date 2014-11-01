#!/bin/bash
#
module load snakemake
cd $PBS_O_WORKDIR
snakemake --jobname 's.{jobid}.{rulename}' --js serpentine/jobscript.sh \
  -k --stats snakemake.stats -T --rerun-incomplete \
  -s serpentine/bio/ngs/workflows/variant_calling_freebayes/Snakefile \
  -j 300 --cluster 'qsub {params.batch}' >& snakemake.log 
