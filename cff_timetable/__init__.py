#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:22:27 2020

@author: williammartin
"""

__version__ = '2020.02.02'

import logging

# get root logger
logger = logging.getLogger()
# flush handlers
logger.handlers = []

# create streamhandler overwriting root streamhandler format
format_message = '%(asctime)s %(filename)-14s %(levelname)-8s: %(message)s'
format_date = '%Y-%m-%d %H:%M:%S'
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(format_message, format_date))
logger.setLevel(logging.WARNING) # Warning because we don't want logs from other standard modules using the root logger
logger.addHandler(handler)

from .config import *
from .cff_api import *
from .slack_api import *
