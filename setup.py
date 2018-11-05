# setup.py
from distutils.core import setup
import py2exe


################################################################
#
# Setup script used for py2exe
#
# *** Important note: ***
# Setting Python's optimize flag when building disables
# "assert" statments, which are used throughout the
# BitTornado core for error-handling.
#
################################################################

setup(windows=['CEP.py'])
