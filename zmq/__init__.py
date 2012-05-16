"""Python bindings for 0MQ."""

#-----------------------------------------------------------------------------
#  Copyright (C) 2010-2012 Brian Granger, Min Ragan-Kelley
#
#  This file is part of pyzmq
#
#  Distributed under the terms of the New BSD License.  The full license is in
#  the file COPYING.BSD, distributed as part of this software.
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import sys

import ctypes, os
here = os.path.dirname(__file__)
if sys.platform.startswith('win'):
    library = os.path.join(here, 'libzmq.pyd')
    ctypes.cdll.LoadLibrary(library)
else:
    library = os.path.join(here, "libzmq.so")
    _zeromq = ctypes.CDLL(library, mode=ctypes.RTLD_GLOBAL)
del ctypes, os, here, library

from zmq.utils import initthreads # initialize threads
initthreads.init_threads()

from zmq import core, devices
from zmq.core import *

def get_includes():
    """Return a list of directories to include for linking against pyzmq with cython."""
    from os.path import join, dirname, abspath, pardir
    base = dirname(__file__)
    parent = abspath(join(base, pardir))
    return [ parent ] + [ join(parent, base, subdir) for subdir in ('utils',) ]


__all__ = ['get_includes'] + core.__all__

