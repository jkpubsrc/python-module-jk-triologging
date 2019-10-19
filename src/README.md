jk_triologging
==========

Introduction
------------

This python module ...

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_triologging)

Why this module?
----------------

With `jk_logging` there is a logging module available that allows constructing loggers from a JSON based description, offers buffers for log messages and supports hierarchical logging. Unfortunately this particular module is synchroneous and therefore can not be used in `Trio` directly. This implementation therefore wraps `jk_logging` and provides an API usable in `Trio`.

Limitations of this module
--------------------------

This module provides classes wrapping (almost all) classes from `jk_logging`. It provides almost all functionality despite one: Descending hierarchically is not supported. (This might change one day, but not in the near future.)

How to install module
----------------------

This module can be installed easily using `pip`.

Use this command for a system wide installation of this module:

```bash
$ sudo pip install jk-triologging
```

Use this command for user specific installation of this module:

```bash
$ pip install --user jk-triologging
```

The PiPy module is always kept in sync with the Github repository so using PyPi is equivalent to a manual installation using the code provided on Github.

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_triologging
```

### Construct a logger

Example:

```python
log = jk_triologging.TrioConsoleLogger.create(logMsgFormatter=jk_triologging.COLOR_LOG_MESSAGE_FORMATTER)
```

Here we construct a console logger (which is an object that writes log messages to STDOUT.) It is configured for using colors for all output here.

### Use the logger

You can create text based log messages and write them to the logger. Example:

```python
await log.debug("This is a test for DEBUG.")
await log.notice("This is a test for NOTICE.")
await log.info("This is a test for INFO.")
await log.warning("This is a test for WARNING.")
await log.error("This is a test for ERROR.")
```

Exceptions can be logged as well. Example:

```python
try:
	await log.notice("Let's try a calculation that will fail ...")
	a = 0
	b = 5 / a
except Exception as ee:
	await log.error(ee)
```

What kind of log objects are available?
---------------------------------------

You can make use of the following log objects:

* `TrioBufferLogger` - implements a buffer for log messages, which later on can be forwareded to another logger
* `TrioConsoleLogger` - implements writing to STDOUT
* `TrioFileLogger` - implements writing to a file
* `TrioFilterLogger` - implements filtering of log messages according to log level
* `TrioMulticastLogger` - implements forwarding log messages to multiple loggers
* `TrioNamedMulticastLogger` - implements forwarding log messages to multiple loggers
* `TrioNullLogger` - discards all log messages
* `TrioStringListLogger` - implements a buffer for log messages, where all log messages are stored a plain text strings

Further Reading
-------------------

See the `test` directory for detailed examples of all loggers.

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



