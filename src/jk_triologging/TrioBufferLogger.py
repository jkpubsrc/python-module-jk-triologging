

import trio

import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioBufferLogger(TrioLogWrapper):

	@staticmethod
	def create(jsonRawData = None):
		return TrioBufferLogger(jk_logging.BufferLogger.create(jsonRawData = None))
	#

	async def hasData(self) -> bool:
		return await trio.to_thread.run_sync(self._l.hasData)
	#

	async def forwardTo(self, logger, bClear:bool = False):
		ldest = logger._l if isinstance(logger, TrioLogWrapper) else logger
		assert isinstance(ldest, jk_logging.AbstractLogger)

		await trio.to_thread.run_sync(self._l.forwardTo, ldest, bClear)
	#

	async def getDataAsJSON(self) -> list:
		return await trio.to_thread.run_sync(self._l.getDataAsJSON)
	#

	async def getDataAsPrettyJSON(self) -> list:
		return await trio.to_thread.run_sync(self._l.getDataAsPrettyJSON)
	#

#







