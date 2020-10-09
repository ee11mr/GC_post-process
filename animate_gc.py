#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SBATCH --job-name=animate_gc
#SBATCH --ntasks=1
#SBATCH --mem=2gb
#SBATCH --time=00:10:00
#SBATCH --output=LOGS/anim.log
import os
import sys 
sys.path.append('/users/mjr583/python_lib')
import GC_tools as GC
import imageio
import glob

if len(sys.argv) == 1:
    rundir='high_res_CVO'
    version='12.9.3'
    species='O3'
else:
    rundir=sys.argv[1]
    species=sys.argv[2]
    try:
        version=sys.argv[3]
    except:
        version='12.9.3'

## get number of arrays to plot (timestep)
nt=GC.get_n_timesteps(rundir, version)

## submit array jobs and wait to complete
print('%s plotting jobs to submit' %nt) 
os.system("sbatch --wait  --array=1-%s anim_pcolormesh.py %s %s %s" % (nt, rundir, species, version))

## animate and delete .pngs 
with imageio.get_writer('/users/mjr583/scratch/GC/%s/%s/plots/%s.gif' % (version, rundir, species), mode='I') as writer:
    for png in sorted(glob.glob('/users/mjr583/scratch/GC/%s/%s/plots/pcolorm_*%s*png' % (version, rundir, species))):
        print(png)
        image = imageio.imread(png) 
        writer.append_data(image)
os.system("rm /users/mjr583/scratch/GC/%s/%s/plots/pcolorm_*%s*png" % (version, rundir, species) )
