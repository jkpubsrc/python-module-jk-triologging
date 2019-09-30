#!/usr/bin/env python3



import os
import time
import traceback
import sys
import abc
import trio

from jk_triologging import *



async def main():

	print()
	print("-- ConsoleLogger --")
	print()

	clog = instantiate({
		"type": "ConsoleLogger",
		"logMsgFormatter": "color",
	})

	await clog.debug("This is a test for DEBUG.")
	await clog.notice("This is a test for NOTICE.")
	await clog.info("This is a test for INFO.")
	await clog.warning("This is a test for WARNING.")
	await clog.error("This is a test for ERROR.")

	print()
	print("-- Exception Handling --")
	print()

	def produceError():
		a = 5
		b = 0
		c = a / b

	try:
		await clog.notice("Now let's try a calculation that will fail ...")
		produceError()
	except Exception as ee:
		await clog.error(ee)

	print()
	print("-- FilterLogger --")
	print()

	flog = instantiate({
		"type": "FilterLogger",
		"minLogLevel": "WARNING",
		"nested": {
			"type": "ConsoleLogger",
			"logMsgFormatter": "color",
		}
	})

	await flog.debug("This message will not appear in the log output.")
	await flog.notice("This message will not appear in the log output.")
	await flog.info("This message will not appear in the log output.")
	await flog.warning("This message will appear in the log output.")
	await flog.error("This message will appear in the log output.")

	print()
	print("-- BufferLogger --")
	print()

	blog = instantiate({
		"type": "BufferLogger",
	})

	await blog.info("First we write something to a buffer.")
	await blog.info("And something more.")
	await blog.notice("And more.")
	await blog.debug("And even more.")
	await blog.warn("And even a warning.")
	await blog.info("Then we write it to the console by forwarding the data to another logger.")
	await blog.forwardTo(clog)

	print()
	print("-- MulticastLogger --")
	print()

	mlog = instantiate({
		"type": "MulticastLogger",
		"nested": [
			{
				"type": "ConsoleLogger",
				"logMsgFormatter": "color",
			},
			{
				"type": "ConsoleLogger",
				"logMsgFormatter": "color",
			}
		]
	})
	await mlog.info("This message gets written twice.")

	print()
	print("-- NamedMulticastLogger --")
	print()

	nmlog = instantiate({
		"type": "NamedMulticastLogger",
		"nested": {}
	})
	nmlog.addLogger("log1", clog)
	nmlog.addLogger("log2", clog)
	await nmlog.info("This message gets written twice.")
	nmlog.removeLogger("log1")
	await nmlog.info("This message gets written once.")

#





trio.run(main)




