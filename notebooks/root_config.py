# root_config.py - add the root directory to the system path so that local modules can be resolved
import os
import sys


# Append the parent directory to the sys path, so modules also resolve from there
def configure():
    absolute_path = os.path.abspath("..")
    if absolute_path not in sys.path:
        sys.path.append(absolute_path)


configure()
