#!/usr/bin/python3




import os
import trio

from jk_triologging import *



async def main():

	clog = TrioConsoleLogger.create(logMsgFormatter=COLOR_LOG_MESSAGE_FORMATTER)

	blog = TrioBufferLogger.create()

	await blog.info("First we write something to a buffer.")
	await blog.info("And something more.")
	await blog.notice("And more.")
	await blog.debug("And even more.")
	await blog.warn("And even a warning.")
	await blog.info("Soon we'll forward all this to the console.")
	await blog.forwardToDescended(clog, "This is a test.")

#





trio.run(main)











