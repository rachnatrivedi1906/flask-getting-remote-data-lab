#!/usr/bin/env python3
import os
import sys

# Ensure the parent `lib` directory is on sys.path so tests can import modules
# like `GetRequester` when pytest runs from the repo root.
HERE = os.path.dirname(__file__)
LIB_DIR = os.path.abspath(os.path.join(HERE, '..'))
if LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))