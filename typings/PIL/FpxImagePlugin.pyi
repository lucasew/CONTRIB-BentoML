"""
This type stub file was generated by pyright.
"""

from typing import Any

from .ImageFile import ImageFile

MODES: Any

class FpxImageFile(ImageFile):
    format: str
    format_description: str
    fp: Any
    def load(self): ...