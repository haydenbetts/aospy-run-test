import os  # Python built-in package for working with the operating system
import aospy
from datetime import datetime as datetime

from aospy.data_loader import GFDLDataLoader
from aospy import Run
from aospy import Model
from aospy import Proj
from aospy import Var
from aospy import Region

rootdir = os.path.abspath(os.path.join(os.getcwd(), '..', 'gridded_data', 'AM2.1_1979-2000-AllForc_h1', 'pp'))
output_dir = os.path.abspath(os.path.join(os.getcwd(), '..', 'gridded_data', 'AM2.1_1979-2000-AllForc_h1_results'))

base = GFDLDataLoader(
    data_direc=rootdir, 
    data_dur=5, 
    data_start_date=datetime(1980, 1, 1),
    data_end_date=datetime(1999, 12, 31),
    )

example_run = Run(
    name='air temp examination',
    description='An examination of air temperature 1980 => 1999',
    data_loader=base
)

example_model = Model(
    name='example_model',
    runs=[example_run],
    grid_file_paths=(
        os.path.join(rootdir, 'atmos', 'ts', 'monthly', 'zg_A1.199501-199912.nc')
    )
)

example_proj = Proj(
    'example_proj',
    direc_out=output_dir,
    models=[example_model]
)

hur = Var(
    name='hur',
    def_time=True,
    description='Relative humidity'
)

globe = Region(
    name='globe',
    description='Entire globe',
    west_bound=0,
    east_bound=360,
    south_bound=-90,
    north_bound=90,
    do_land_mask=False
)