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
'''
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
'''
inputs=GC.get_arguments()
rundir=inputs.rundir
variable=inputs.var
version=inputs.version
plot_pressure=inputs.plot_ps

## get number of arrays to plot (timestep)
nt=GC.get_n_timesteps(rundir, version)

## submit array jobs and wait to complete
print('%s plotting jobs to submit' %nt)
if plot_pressure:
    outname='/users/mjr583/scratch/GC/%s/%s/plots/%s_with_ps.mp4' % (version, rundir, variable)
    os.system("sbatch --wait  --array=1-%s anim_pcolormesh_with_p.py -r %s -v %s -V %s" % (nt, rundir, variable, version))
else:
    outname='/users/mjr583/scratch/GC/%s/%s/plots/%s.mp4' % (version, rundir, variable)
    os.system("sbatch --wait  --array=1-%s anim_pcolormesh.py -r %s -v %s -V %s" % (nt, rundir, variable, version))

## animate and delete .pngs 
with imageio.get_writer(outname, mode='I') as writer:
    for png in sorted(glob.glob('/users/mjr583/scratch/GC/%s/%s/plots/pcolorm_*%s*png' % (version, rundir, variable))):
        print(png)
        image = imageio.imread(png) 
        writer.append_data(image)
os.system("rm /users/mjr583/scratch/GC/%s/%s/plots/pcolorm_*%s*png" % (version, rundir, variable) )
