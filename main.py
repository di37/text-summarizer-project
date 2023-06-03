import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from summarizerLogging import *
from utils import *
from textSummarizer import *
from config import *

# Custom Logging Demo
# logger.info("Logging initialized.")
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e