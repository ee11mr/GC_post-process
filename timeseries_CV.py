#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SBATCH --job-name=timeseries
#SBATCH --ntasks=1
#SBATCH --mem=1gb
#SBATCH --partition=interactive
#SBATCH --time=00:01:00
#SBATCH --output=LOGS/timeseries.log
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
sys.path.append('/users/mjr583/python_lib')
import GC_tools as GC
import RowPy as rp
from CVAO_dict import CVAO_dict as d
import CVAO_tools as CV

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

f,ax= plt.subplots(figsize=(12,4))
ax.plot(df.index, df.Value, 'k', label='CVAO')
ax.plot(GC.index, GC.Value, 'g', label='GEOS-Chem')
plt.ylabel('%s (%s)' % (d[species]['abbr'], d[species]['unit']) )

import matplotlib.dates as mdates
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))

plt.legend()
plt.savefig('/users/mjr583/scratch/GC/%s/%s/plots/timeseries_%s.png' % (version, rundir, species) )
