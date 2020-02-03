#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:04:33 2020

@author: williammartin
"""

__docformat__ = 'reStructuredText'

# import standard libraries
from datetime import datetime
import json
import logging
logger = logging.getLogger(__name__)
import requests as re
# import third-party libraries
# import local libraries
from .config import DEBUG, RES_URL, NOTIFY_ERR

# CFF class
class CFF:
    
    # init method
    def __init__(self, level = 'DEBUG' if DEBUG else 'WARNING'):
        
        # set logger of module
        self.level = level
        level = logging.getLevelName(level)
        logger.setLevel(level)
        
        # other properties
        self.res_url = RES_URL
        
        logger.debug('Created CFF object successfully')
     
    # procedure to check response
    def customGet(self, url, payload):
        
        try:
            r = re.get(url, params = payload)
            return r
        except re.exceptions.RequestException as e:
            logger.error(e)
            # send message on slack
            if NOTIFY_ERR:
                pass
            return None
            
    # show connections method
    def showConnections(self, fr, to, via = None, limit = 1, 
                        time = datetime.now().strftime('%H:%M')):
        
        url = self.res_url + '/connections'
        payload = {'from': fr, 'to': to, 'via': via, 'limit': limit,
                   'time': time}
        logger.debug('Sending requests with payload: {}'.format(payload))
        content = self.customGet(url, payload)

        if content:
            content = json.loads(content.text)
            
        return content['connections']
    
    # check delay at departure
    def checkDelays(self, connections):
        
        for i, c in enumerate(connections):
            logger.debug('Connection {} on {}'.format(i, c['from']['departure']))
            for s in c['sections']:
                departure = s['departure']
                location = departure['location']['name']
                delay = departure['delay']
                if delay:
                    logger.debug('{} from {}'.format(delay, location))
                else:
                    logger.debug('No delay from {}'.format(location))
        
    
    
