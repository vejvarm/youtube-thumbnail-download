import sys
import os
from cx_Freeze import setup, Executable

__version__ = "1.0"

packages = ["sys", "os", "re", "requests", "bs4", "multiprocessing"]
includes = ["idna.idnadata"]

setup(
      name="YouTubeThumbnail",
      description="Download YouTube thumbnail images in max resolution",
      version= __version__,
      options={"build_exe": {
            "packages": packages,
            "includes": includes
      }},
      executables=[Executable("downloadThumbnail.py", base="Console")]
)
