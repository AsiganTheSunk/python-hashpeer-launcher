#!/usr/bin/python3

# Import Logging Libraries
from logging import getLoggerClass, addLevelName, NOTSET

# Constants
VERBOSE = 5
DEBUG0 = 15
FATAL = 50


class CustomLogger(getLoggerClass()):
    def __init__(self, name, level=NOTSET):
        super().__init__(name, level)
        addLevelName(VERBOSE, 'VERBOSE')
        addLevelName(DEBUG0, 'DEBUG0')
        addLevelName(FATAL, 'FATAL')

    def verbose(self, msg, *args, **kwargs):
        '''
        Verbose logging message it's thrown in case we enable verbose output of the process
        :param msg:
        :param args:
        :param kwargs:
        :return: verbose lvl logging message
        '''
        if self.isEnabledFor(VERBOSE):
            self._log(VERBOSE, msg, args, **kwargs)

    def debug0(self, msg, *args, **kwargs):
        '''
        Debug0 logging message it's thrown in case we need a less verbose output of the process, but still want to
        perform debugging
        :param msg:
        :param args:
        :param kwargs:
        :return: verbose lvl logging message
        '''
        if self.isEnabledFor(DEBUG0):
            self._log(DEBUG0, msg, args, **kwargs)

    def fatal(self, msg, *args, **kwargs):
        '''
        Fatal logging message it's thrown in case an unexpected Exception it's launched by the application
        :param msg:
        :param args:
        :param kwargs:
        :return: fatal lvl logging message
        '''
        if self.isEnabledFor(FATAL):
            self._log(DEBUG0, msg, args, **kwargs)
