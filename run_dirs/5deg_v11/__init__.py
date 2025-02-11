'''
5deg_but_v11

### Put detailed experiment description here ###
'''
import os
from datetime import date

expid='5deg_v11'
cmpexp='5deg_v11'
data_path='/discover/nobackup/dardag/GEOS_FORWARD/testout/5deg_v11'
plot_path=data_path+'/plots_ocn'
basin_mask='/discover/nobackup/projects/gmao/ssd/aogcm/basin_mask/72x36/basin_mask.nc'
grid_spec='/discover/nobackup/projects/gmao/ssd/aogcm/a12x72_o72x36/INPUT/grid_spec.nc'

start_year=1980
end_year=1981
skip_yrs=0
dates=(date(start_year+skip_yrs,1,15),date(end_year,12,15))

'''
You can also specify a custom format string for data file locations for selected collections. 
In the example below, a custom format is specified for geosgcm_ocn2d monthly and daily collections,
and for MOM output collection. For all other collections, a default format string will be used.

fmt={
    'geosgcm_ocn2d':{
        'MONTHLY': '{data_path}/{collection}/{expid}.{collection}.monthly.{date:%Y%m}.nc4',
        'DAILY'  : '{data_path}/{collection}/{expid}.{collection}.monthly.{date:%Y%m%d}_1500z.nc4'
        },
    'MOM_Output': '{data_path}/{collection}/ocean_month.e{date:%Y%m}01_00z.nc'
}
'''
