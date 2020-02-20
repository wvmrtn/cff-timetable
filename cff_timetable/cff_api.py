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
import pandas as pd
# import local libraries
from .config import DEBUG, RES_URL
from .slack_api import SlackHandler

# CFF class
class CFF:
    
    # init method
    def __init__(self, level = 'DEBUG', notify_slack = False):
        
        # set logger of module
        self.level = level
        self.notify_slack = notify_slack
        level = logging.getLevelName(level)
        logger.setLevel(level)
        
        # other properties
        self.res_url = RES_URL
        
        # log to slack in addition
        if self.notify_slack:
            # add the custom slack handler to the root logger
            logger.addHandler(SlackHandler())
            
        logger.debug('Created CFF object successfully')
     
    # procedure to check response
    def customGet(self, url, payload):
        
        logger.debug('Sending request to url: {}'.format(url))
        logger.debug('With payload: {}'.format(payload))
        try:
            r = re.get(url, params = payload)
            return r
        except re.exceptions.RequestException as e:
            logger.error(e)
            
    # show connections method
    def returnConnections(self, fr, to, via = None, limit = 1, 
                          time = datetime.now().strftime('%H:%M')):
        
        url = self.res_url + '/connections'
        payload = {'from': fr, 'to': to, 'via': via, 'limit': limit,
                   'time': time}
        content = self.customGet(url, payload)

        if content:
            content = json.loads(content.text)
        else:
            logger.warning('No connections found')
            
        return content['connections']
    
    # check delay at departure
    def returnDelays(self, connections):
        
        for i, c in enumerate(connections):
            datetime_departure = c['from']['departure']
            datetime_departure = pd.to_datetime(datetime_departure)
            date_departure = datetime_departure.strftime('%d.%m.%Y')
            time_departure = datetime_departure.strftime('%H:%M:%S')
            logger.info('Connection {} at {} on {}'.format(i+1, 
                                                           time_departure,
                                                           date_departure))
            
            # go over all sections of travel and identify delays
            for s in c['sections']:
                departure = s['departure']
                location = departure['location']['name']
                delay = departure['delay']
                if delay:
                    logger.warning('{} from {}'.format(delay, location))
                else:
                    logger.info('No delay from {}'.format(location))
            
            # check delay at destination
            arrival = s['arrival']
            location = arrival['location']['name']
            delay = arrival['delay']
            if delay:
                logger.warning('{} at {}'.format(delay, location))
            else:
                logger.info('No delay at arrival in {}'.format(location))
            
        
    
    
