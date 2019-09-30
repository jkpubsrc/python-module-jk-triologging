

import trio

import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioMulticastLogger(TrioLogWrapper):

	@staticmethod
	def create(*argv):
		loggers = []
		for l in argv:
			if isinstance(l, TrioLogWrapper):
				loggers.append(l._l)
			else:
				assert isinstance(l, jk_logging.AbstractLogger)
				loggers.append(l)
		return TrioMulticastLogger(jk_logging.MulticastLogger.create(*loggers))
	#

	def addLogger(self, logger):
		if isinstance(logger, TrioLogWrapper):
			logger = logger._l
		assert isinstance(logger, jk_logging.AbstractLogger)
		self._l.addLogger(logger)
	#

	def removeLogger(self, logger):
		if isinstance(logger, TrioLogWrapper):
			logger = logger._l
		assert isinstance(logger, jk_logging.AbstractLogger)
		self._l.removeLogger(logger)
	#

	def removeAllLoggers(self):
		self._l.removeAllLoggers()
	#

#







