#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:55:53 2020

@author: williammartin
"""

__docformat__ = 'reStructuredText'

# import standard libraries
import logging
from logging import Handler
logger = logging.getLogger(__name__)
import os
# import third-party libraries
import slack
# import local libraries
from .config import CHANNEL

class SlackHandler(Handler):
    
    def __init__(self):
        
        Handler.__init__(self)
        self.bot_token = os.environ['SLACK_API_TOKEN_BOT'] # needs to be added to the environment variables!  
        self.bot_client = slack.WebClient(token = self.bot_token)
        
    def emit(self, record):
        
        log_entry = self.format(record)
        response = self.bot_client.chat_postMessage(
            channel = CHANNEL,
            text = log_entry)
        
        assert response["ok"]
        # assert response["message"]["text"] == log_entry
            
# test
if __name__ == '__main__':
    
    pass
