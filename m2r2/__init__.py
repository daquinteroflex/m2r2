print("Importing from m2r2/__init__.py")
from . import rst
from .m2r2 import M2R, convert
print("tryagain")
from .sphinx.m2r2 import setup


__all__ = ("M2R", "convert", "setup", "rst")
