

import trio

import jk_logging

from .TrioLogWrapper import TrioLogWrapper




class TrioNullLogger(TrioLogWrapper):

	@staticmethod
	def create():
		return TrioNullLogger(jk_logging.NullLogger.create())
	#

#







