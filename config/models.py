import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from utils import *

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

class DataValidationConfig(BaseModel):
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: List[str]