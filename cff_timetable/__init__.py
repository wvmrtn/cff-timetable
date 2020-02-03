#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:22:27 2020

@author: williammartin
"""

__version__ = '2020.02.02'

import logging
# import os
# import sys

# the below code could be in a INI file but more control when it's inside code
# logger configuration below
logger = logging.getLogger(__name__)
logger.handlers = []
format_message = '%(asctime)s %(filename)-14s %(levelname)-8s: %(message)s'
format_date = '%Y-%m-%d %H:%M:%S'

# if in debug mode, print everything to console
# if DEBUG:
    # handler = logging.StreamHandler()
    
# otherwise print in rotate file
# else:
    # pass
    # if not os.path.exists(OUTPUT_DIR):
    #     os.makedirs(OUTPUT_DIR)
    # handler = logging.handlers.TimedRotatingFileHandler(
    #     filename = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME),
    #     when = 'D', interval = 1, backupCount = 14)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(format_message, format_date))
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

from .config import *
from .cff_api import *