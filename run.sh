#!/bin/bash

# activate environment
source ~/python_env/cff/bin/activate

# run python script
python ~/Github/cff-timetable/main.py schedule_williammartin.csv @URE5PNJTS INFO &> ~/Github/cff-timetable/run_williammartin.log
#python ~/Github/cff-timetable/main.py schedule_nelsonkoch.csv @UU2KYEYMR WARNING &> ~/Github/cff-timetable/run_nelsonkoch.log
#python ~/Github/cff-timetable/main.py schedule_test.csv @URE5PNJTS DEBUG &> ~/Github/cff-timetable/run_williammartin.log

