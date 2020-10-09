#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SBATCH --job-name=timeseries
#SBATCH --ntasks=1
#SBATCH --mem=10gb
#SBATCH --partition=interactive
#SBATCH --time=00:01:00
#SBATCH --output=LOGS/timeseries.log
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
import matplotlib
matplotlib.use('agg')
sys.path.append('/users/mjr583/python_lib')
import GC_tools as GC
import RowPy as rp
from CVAO_dict import CVAO_dict as d
import CVAO_tools as CV
plt.style.use('seaborn-darkgrid')

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
GC=pd.DataFrame({'Value':var_time}, index=time)

## Get Merge observations
df=CV.get_from_merge(d[species])
df=df[GC.index[0]:GC.index[-1]]

f,ax= plt.subplots(figsize=(8,8))
ax.scatter(df.Value,GC.Value)
plt.ylabel('GEOSChem %s (%s)' % (d[species]['abbr'], d[species]['unit']) )
plt.xlabel('CVAO %s (%s)' % (d[species]['abbr'], d[species]['unit']) )

Max=np.max([GC.Value.max(), df.Value.max()])
Min=np.min([GC.Value.min(), df.Value.min()])
plt.xlim(Min,Max)
plt.ylim(Min,Max)

line = mlines.Line2D([0, 1], [0, 1], color='red', alpha=0.2)
transform = ax.transAxes
line.set_transform(transform)
ax.add_line(line)#, alpha=0.6)

plt.savefig('/users/mjr583/scratch/GC/%s/%s/plots/scatter_GC-CV_%s.png' % (version, rundir, species) )
