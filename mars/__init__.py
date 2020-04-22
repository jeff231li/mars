"""
Mars
Mars is a demo project for showing neat ideas.
"""

# Add imports here
from .mars import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
