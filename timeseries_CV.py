#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SBATCH --job-name=pcolor_plot
#SBATCH --ntasks=1
#SBATCH --mem=10gb
#SBATCH --partition=nodes
#SBATCH --time=00:05:00
#SBATCH --output=LOGS/pcolormesh_%a.log
#SBATCH --array=1-2
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
sys.path.append('/users/mjr583/python_lib')
import GC_tools as GC
import RowPy as rp
from CVAO_dict import CVAO_dict as d

#jobid=int(os.getenv("SLURM_ARRAY_TASK_ID"))
rundir=sys.argv[1]
species=sys.argv[2]
version='12.9.3'

var, lat, lon, lev, time = GC.get_gc_var(rundir, species, version)

y = rp.find_nearest(lat, 16.52)
x = rp.find_nearest(lon, -24.51)
var_time=[]
for t in range(len(time)):
    v=var[t,0,y,x]
    var_time.append(v)
df=pd.DataFrame({species:var_time}, index=time)

## Get Merge observations

f,ax= plt.subplots(figsize=(12,4))
ax.plot(df.index, df.O3, 'g', label='GEOS-Chem')
plt.ylabel('%s (%s)' % (d[species]['abbr'], d[species]['unit']) )
plt.legend()
plt.savefig('/users/mjr583/scratch/GC/%s/%s/plots/timeseries_%s.png' % (version, rundir, species) )
