#5!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:33:40 2019

@author: williammartin
"""

# import standard libraries
import os
# import third-party libraries
# import local libraries
from cff_timetable import CFF

if __name__ == '__main__':
    
    cff = CFF(level = 'INFO', notify_slack = True)
    connections = cff.returnConnections('Neuchatel', 'EPFL',
                                        limit = 1)
    
    cff.returnDelays(connections)
    
    # payload = {'from': 'Neuchâtel', 'to': 'Lausanne'}
    
    # r = requests.get('http://transport.opendata.ch/v1/connections', 
    #                  params = payload)
        
    # if r.status_code == requests.codes.ok:
    #     content = r.json()
        
    # else:
    #     r.raise_for_status()
