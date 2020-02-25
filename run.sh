#!/bin/bash

# activate environment
source ~/python_env/cff/bin/activate

# run python script
#python ~/Github/cff-timetable/main.py schedule_williammartin.csv cff_williammartin &> ~/Github/cff-timetable/run_williammartin.log
#python ~/Github/cff-timetable/main.py schedule_nelsonkoch.csv cff_nelsonkoch &> ~/Github/cff-timetable/run_nelsonkoch.log
python ~/Github/cff-timetable/main.py schedule_test.csv cff_williammartin &> ~/Github/cff-timetable/run_williammartin.log

