import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils.helper import *

CONFIG_FILE_PATH = Path("./config/config.yaml")
PARAMS_FILE_PATH = Path("./config/params.yaml")