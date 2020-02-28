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

class SlackHandler(Handler):
    
    def __init__(self, channel):
        
        Handler.__init__(self)
        self.bot_token = os.environ['SLACK_API_TOKEN_BOT']
        self.bot_client = slack.WebClient(token = self.bot_token)
        self.channel = channel
        
    def emit(self, record):
        
        log_entry = self.format(record)
        response = self.bot_client.chat_postMessage(
            channel = self.channel,
            text = log_entry,
            as_user = True)
        
        assert response["ok"]
        # assert response["message"]["text"] == log_entry
            
# test
if __name__ == '__main__':
    
    pass
