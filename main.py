#5!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:33:40 2019

@author: williammartin
"""

# import standard libraries
import datetime
import os
import sys
import time
# import third-party libraries
import pandas as pd
# import local libraries
from cff_timetable import CFF, ABSPATH

TEST = False
if TEST:
    FILENAME = 'schedule_test.csv'
    CHANNEL = 'general'
else:
    FILENAME = sys.argv[1]
    CHANNEL = sys.argv[2]

TOKEN = os.environ['SLACK_API_TOKEN_BOT']

if __name__ == '__main__':
    
    # read schedule for checking when to send notifications
    schedule = pd.read_csv(os.path.join(ABSPATH, FILENAME))
    # clean schedule
    schedule = schedule[['from', 'to', 'via', 'limit', 'time', 'day', 'notice']]
    
    for index, entry in schedule.iterrows():
        
        # check for day and time
        now = datetime.datetime.now()
        day = now.strftime('%A')
        if pd.isna(entry['time']):
            entry_time = now
        else:
            entry_time = datetime.datetime.strptime(entry['time'], '%H:%M')
        now = now.replace(year = entry_time.year, month = entry_time.month,
                          day = entry_time.day)
        
        if day == entry['day'] and \
            entry_time >= now and \
            (entry_time - now).seconds < entry['notice']:
            
            cff = CFF(level = 'INFO', notify_slack = True, channel = '#{}'.format(CHANNEL),
                      bot_token = TOKEN)
            connections = cff.returnConnections(entry['from'], 
                                                entry['to'],
                                                via = None if pd.isna(entry['via']) else entry['via'],
                                                limit = entry['limit'],
                                                time = entry['time'])
            
            cff.showDelays(connections)
            
            # leave some time for notifications to pass
            time.sleep(5)
