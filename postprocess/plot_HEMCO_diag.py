
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
from matplotlib.colors import LogNorm
import sys
sys.path.append('/users/mjr583/python_lib')
from CVAO_dict import CVAO_dict as d
import RowPy as rp
import GC_tools as GC

rundir='boundary_conds_run'
variable='EmisCO_BioBurn'
date='201701010000'

ems, times, lat, lon, lev, area = GC.HEMCO_Diag_read(rundir, variable=variable, date=date)
ems=ems[0]

X,Y = np.meshgrid(lon,lat)
f, ax = plt.subplots()
m=rp.get_basemap(ax=ax)

im=ax.pcolormesh(X,Y,ems, norm=LogNorm())
cbar = f.colorbar(im,orientation='horizontal')
cbar.ax.set_xlabel('variable')

plt.savefig('./test.png')
plt.close()
