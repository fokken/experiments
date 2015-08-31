#!/usr/bin/python
import logging,logging.handlers,time

def setup_logger(logpath):
	logger = logging.getLogger("awesomelogger")
	logger.setLevel(logging.DBUG)
	handler.FileHandler(logpath)
	logger.addHandler()
	return logger

def print_time(message):
	print time.strftime("%Y%m%d_%H%M%S:")+message
