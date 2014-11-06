#!/bin/bash
#
module load snakemake
cd $PBS_O_WORKDIR
export SERPENTINE_HOME="/path/to/serpentine"
snakemake --jobname 's.{jobid}.{rulename}' --js $SERPENTINE_HOME/jobscript.sh \
  -k --stats serpentine.stats -T --rerun-incomplete \
  -s ${SERPENTINE_HOME}/bio/ngs/workflows/variant_calling_freebayes/Snakefile \
  -j 300 --cluster 'qsub {params.batch}' >& serpentine.log 
