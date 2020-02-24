#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:12:04 2019

@author: williammartin
"""

# import standard libraries
# import third-party libraries
# import local libraries
from cff_timetable import CFF

if __name__ == '__main__':

    cff = CFF(level = 'INFO', notify_slack = True)
    connections = cff.returnConnections('Neuchatel', 
                                        'EPFL',
					time = '08:00',
                                        limit = 1)
    cff.showDelays(connections)
