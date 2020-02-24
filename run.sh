#!/bin/bash

# activate environment
source ~/python_env/cff/bin/activate

# run python script
python ~/Github/cff-timetable/main.py williammartin williammartin &> ~/Github/cff-timetable/run_williammartin.log

