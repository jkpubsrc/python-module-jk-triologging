


import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioConsoleLogger(TrioLogWrapper):

	@staticmethod
	def create(printToStdErr = False, logMsgFormatter = None, printFunction = None):
		return TrioConsoleLogger(jk_logging.ConsoleLogger.create(printToStdErr, logMsgFormatter, printFunction))
	#

#







