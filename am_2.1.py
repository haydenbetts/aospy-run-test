from aospy import submit_mult_calcs
import example_run_lib as lib

calc_suite_specs = dict(
    library=lib,
    projects=[lib.example_proj],
    models=[lib.example_model],
    runs=[lib.example_run],
    variables=[lib.hur],
    regions='all',
    date_ranges='default',
    output_time_intervals=['ann'],
    output_time_regional_reductions=['av', 'reg.av'],
    output_vertical_reductions=[None],
    input_time_intervals=['monthly'],
    input_time_datatypes=['ts'],
    input_time_offsets=[None],
    input_vertical_datatypes=[False],
)

calc_exec_options = dict(prompt_verify=False, parallelize=False, write_to_tar=False)

calcs = submit_mult_calcs(calc_suite_specs, calc_exec_options)