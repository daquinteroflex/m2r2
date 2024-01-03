print("Importing from m2r2/__init__.py")
from .m2r2 import M2R, convert
from .sphinx.m2r2 import setup
from . import rst
from . import cli
from . import sphinx

__all__ = ("M2R", "convert", "setup", "rst", "cli", "sphinx")
