


import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioFilterLogger(TrioLogWrapper):

	@staticmethod
	def create(logger:jk_logging.AbstractLogger, minLogLevel:jk_logging.EnumLogLevel = jk_logging.EnumLogLevel.WARNING):
		return TrioFilterLogger(jk_logging.FilterLogger.create(logger, minLogLevel))
	#

#







