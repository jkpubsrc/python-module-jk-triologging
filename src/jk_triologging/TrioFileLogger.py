

import trio

import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioFileLogger(TrioLogWrapper):

	@staticmethod
	def create(filePath, rollOver, bAppendToExistingFile = True, bFlushAfterEveryLogMessage = True, fileMode = None, logMsgFormatter = None):
		return TrioFileLogger(jk_logging.FileLogger.create(filePath, rollOver, bAppendToExistingFile, bFlushAfterEveryLogMessage, fileMode, logMsgFormatter))
	#

	async def closed(self) -> bool:
		return await trio.to_thread.run_sync(self._l.closed)
	#

	async def isClosed(self) -> bool:
		return await trio.to_thread.run_sync(self._l.isClosed)
	#

#







