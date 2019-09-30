

import trio

import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioNamedMulticastLogger(TrioLogWrapper):

	@staticmethod
	def create(**kwargs):
		loggers = {}
		for k, l in kwargs.items():
			if isinstance(l, TrioLogWrapper):
				loggers[k] = l._l
			else:
				assert isinstance(l, jk_logging.AbstractLogger)
				loggers[k] = l
		return TrioNamedMulticastLogger.create(jk_logging.NamedMulticastLogger.create(**loggers))
	#

	def addLogger(self, loggerName:str, logger):
		assert isinstance(loggerName, str)
		if isinstance(logger, TrioLogWrapper):
			logger = logger._l
		assert isinstance(logger, jk_logging.AbstractLogger)
		self._l.addLogger(loggerName, logger)
	#

	def removeLogger(self, loggerName:str):
		assert isinstance(loggerName, str)
		self._l.removeLogger(loggerName)
	#

	def removeAllLoggers(self):
		self._l.removeAllLoggers()
	#

#







