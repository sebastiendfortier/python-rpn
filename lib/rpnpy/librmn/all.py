#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Stephane Chamberland <stephane.chamberland@canada.ca>
# Copyright: LGPL 2.1
"""
 Short hand to load all rpnpy.librmn submodules in the same namespace

 See also:
     rpnpy.librmn
     rpnpy.librmn.proto
     rpnpy.librmn.proto_burp
     rpnpy.librmn.const
     rpnpy.librmn.base
     rpnpy.librmn.fstd98
     rpnpy.librmn.interp
     rpnpy.librmn.grids
     rpnpy.librmn.burp
     rpnpy.librmn.burp_const
     rpnpy.librmn.app
     rpnpy.librmn.app_const

"""

from . import *
from .proto import *
from .proto_burp import *
from .proto_app import *
from .const import *
from .base import *
from .fstd98 import *
from .interp import *
from .grids import *
from .burp import *
from .burp_const import *
from .app import *
from .app_const import *


if __name__ == "__main__":
    pass

# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;

