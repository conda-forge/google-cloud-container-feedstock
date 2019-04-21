# -*- coding: utf-8 -*-

# --- Builtin imports ------------------------------------------------------------------------------
import importlib
import os
import pkgutil
from pkgutil import walk_packages
import sys

# ------------ 3rd-party imports -------------------------------------------------------------------
import google

package=google

for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
													  prefix=package.__name__+'.',
													  onerror=lambda x: None):
	print("    - %s" % modname)

