

import jk_logging

from .TrioLogWrapper import TrioLogWrapper
from .TrioBufferLogger import TrioBufferLogger
from .TrioConsoleLogger import TrioConsoleLogger
from .TrioFileLogger import TrioFileLogger
from .TrioFilterLogger import TrioFilterLogger
from .TrioMulticastLogger import TrioMulticastLogger
from .TrioNamedMulticastLogger import TrioNamedMulticastLogger
from .TrioNullLogger import TrioNullLogger
from .TrioStringListLogger import TrioStringListLogger





def instantiate(cfg) -> TrioLogWrapper:
	l = jk_logging.instantiate(cfg)

	if isinstance(l, jk_logging.BufferLogger):
		return TrioBufferLogger(l)
	elif isinstance(l, jk_logging.ConsoleLogger):
		return TrioConsoleLogger(l)
	elif isinstance(l, jk_logging.FileLogger):
		return TrioFileLogger(l)
	elif isinstance(l, jk_logging.FilterLogger):
		return TrioFilterLogger(l)
	elif isinstance(l, jk_logging.MulticastLogger):
		return TrioMulticastLogger(l)
	elif isinstance(l, jk_logging.NamedMulticastLogger):
		return TrioNamedMulticastLogger(l)
	elif isinstance(l, jk_logging.NullLogger):
		return TrioNullLogger(l)
	elif isinstance(l, jk_logging.StringListLogger):
		return TrioStringListLogger(l)
	else:
		return TrioLogWrapper(l)
#









