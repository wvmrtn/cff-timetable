#5!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:33:40 2019

@author: williammartin
"""

# import standard libraries
import datetime
import math
import os
import time
# import third-party libraries
import pandas as pd
# import local libraries
from cff_timetable import CFF

# read schedule for checking when to send notifications
schedule = pd.read_csv('schedule.csv')
# clean schedule
schedule = schedule[['from', 'to', 'via', 'limit', 'time', 'day', 'notice']]

if __name__ == '__main__':
    
    for index, entry in schedule.iterrows():
        
        # check for day and time
        now = datetime.datetime.now()
        day = now.strftime('%A')
        entry_time = datetime.datetime.strptime(entry['time'], '%H:%M')
        now = now.replace(year = entry_time.year, month = entry_time.month,
                          day = entry_time.day)
        
        if day == entry['day'] and \
            entry_time > now and \
            (entry_time - now).seconds < entry['notice']:
            
            cff = CFF(level = 'INFO', notify_slack = True)
            connections = cff.returnConnections(entry['from'], 
                                                entry['to'],
                                                via = None if math.isnan(entry['via']) else entry['via'],
                                                limit = entry['limit'],
                                                time = entry['time'])
            
            cff.showDelays(connections)
            
            # leave some time for notifications to pass
            time.sleep(5)
