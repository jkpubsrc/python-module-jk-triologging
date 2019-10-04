

import os
import time
import traceback
import sys
import abc

import trio

from jk_logging import *





#
# This logger writes log data to a log file. Log file rotation is supported.
#
class TrioLogWrapper(object):


	def __init__(self, logger:AbstractLogger):
		self._l = logger
	#

	#
	# Perform logging with log level ERROR.
	#
	# @param	string text		The text to write to this logger.
	#
	async def error(self, text):
		await trio.to_thread.run_sync(self._l.error, text)
	#

	#
	# Perform logging with log level EXCEPTION.
	#
	# @param	Exception exception		The exception to write to this logger.
	#
	async def exception(self, exception):
		await trio.to_thread.run_sync(self._l.exception, exception)
	#

	#
	# Perform logging with log level ERROR.
	# This method is intended to be used in conjunction with STDERR handlers.
	#
	# @param	string text		The text to write to this logger.
	#
	async def stderr(self, text):
		await trio.to_thread.run_sync(self._l.stderr, text)
	#

	#
	# Perform logging with log level STDOUT.
	# This method is intended to be used in conjunction with STDOUT handlers.
	#
	# @param	string text		The text to write to this logger.
	#
	async def stdout(self, text):
		await trio.to_thread.run_sync(self._l.stdout, text)
	#

	#
	# Perform logging with log level SUCCESS.
	#
	# @param	string text		The text to write to this logger.
	#
	async def success(self, text):
		await trio.to_thread.run_sync(self._l.success, text)
	#

	#
	# Perform logging with log level WARNING. This method is provided for convenience and is identical with <c>warn()</c>.
	#
	# @param	string text		The text to write to this logger.
	#
	async def warning(self, text):
		await trio.to_thread.run_sync(self._l.warning, text)
	#

	#
	# Perform logging with log level WARNING. This method is provided for convenience and is identical with <c>warning()</c>.
	#
	# @param	string text		The text to write to this logger.
	#
	async def warn(self, text):
		await trio.to_thread.run_sync(self._l.warn, text)
	#

	#
	# Perform logging with log level INFO.
	#
	# @param	string text		The text to write to this logger.
	#
	async def info(self, text):
		await trio.to_thread.run_sync(self._l.info, text)
	#

	#
	# Perform logging with log level NOTICE.
	#
	# @param	string text		The text to write to this logger.
	#
	async def notice(self, text):
		await trio.to_thread.run_sync(self._l.notice, text)
	#

	#
	# Perform logging with log level DEBUG.
	#
	# @param	string text		The text to write to this logger.
	#
	async def debug(self, text):
		await trio.to_thread.run_sync(self._l.debug, text)
	#

	#
	# Perform logging with log level TRACE.
	#
	# @param	string text		The text to write to this logger.
	#
	async def trace(self, text):
		await trio.to_thread.run_sync(self._l.trace, text)
	#

	# Create a nested logger. This new logger can than be used like the current logger, but all log messages will be delivered
	# to an subordinate log structure (if supported by this logger).
	#
	async def descend(self, text):
		raise NotImplementedError()
	#

	#
	# If this logger is buffering log messages, clear all log messages from this buffer.
	# If this logger has references to other loggers, such as a <c>FilterLogger</c>
	# or a <c>MulticastLogger</c>
	#
	async def clear(self):
		await trio.to_thread.run_sync(self._l.clear)
	#

	#
	# Close this logger. Some logger make use of additional resources (such as files) which will be (permanently) closed by invoking this method.
	# By default this method does nothing. Some loggers may overwrite this method in order to make use of that functionality. After closing
	# a logger you should not invoke any more logging methods of that logger. Loggers that make use of <c>close()</c> should reject any logging
	# request after a <c>close()</c> has been invoked. <c>close()</c> must always be implemented as an indempotent operation: Redundant calls to <c>close()</c>
	# should cause no problems.
	#
	async def close(self):
		await trio.to_thread.run_sync(self._l.close)
	#

	def __str__(self):
		s = str(self._l)
		pos = s.find("Logger ")
		if pos >= 0:
			pos = s.rfind(".", 0, pos-1)
			if pos >= 0:
				return "<Trio" + s[pos+1:]
		return "<Trio" + s[1:]
	#

	def __repr__(self):
		return self.__repr__()
	#

#








