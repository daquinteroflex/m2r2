print("Importing from m2r2/__init__.py")
print("Importing from .constants")
from .constants import *
print("Importing from .typing")
from .typing import *
print("Importing from .rst_parser")
from .rst_parser import *
print("Importing from .rst_renderer")
from .rst_renderer import *
print("Importing from .m2r2")
from .m2r2 import M2R, convert
print("tryagain")
from .sphinx.m2r2 import setup


# __all__ = ("M2R", "convert", "setup", "rst")
