

import trio

import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioStringListLogger(TrioLogWrapper):

	@staticmethod
	def create(logMsgFormatter = None):
		return TrioStringListLogger(jk_logging.StringListLogger.create(logMsgFormatter))
	#

	async def hasData(self):
		await trio.to_thread.run_sync(self._l.hasData())
	#

	async def toList(self):
		await trio.to_thread.run_sync(self._l.toList())
	#

#







