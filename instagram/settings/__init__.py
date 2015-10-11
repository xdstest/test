#-*- coding: utf-8 -*-

from common import *

try:
    from develop import *
except ImportError:
    try:
        from production import *
    except ImportError:
        pass