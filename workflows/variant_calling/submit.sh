#!/bin/bash
#
#
NOW=$(date +"%H%M%S_%m%d%Y")
module load snakemake
cd $PBS_O_WORKDIR
export SERPENTINE_HOME=[path2serpentine_clinomics]
snakemake --jobname 's.{jobid}.{rulename}' \
  --js $SERPENTINE_HOME/jobscript.sh \
  -k -r -p -w 10 \
  -T --rerun-incomplete \
  --stats snakemake_${NOW}.stats \
  -j 300 --cluster 'qsub {params.batch}' \
  >& snakemake_${NOW}.log 
