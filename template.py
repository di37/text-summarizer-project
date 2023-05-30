import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: - %(message)s:')

absolute_imports = "import os, sys\nfrom os.path import dirname as up\n\nsys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))\n"

list_of_files = [
    (os.path.join("utils", "__init__.py"), "from utils.constants import *\nfrom utils.helper import *\n"),
    (os.path.join("utils", "helper.py"), absolute_imports),
    (os.path.join("utils", "constants.py"), absolute_imports),
    (os.path.join("textSummarizer", "__init__.py"),  "from textSummarizer.helper import *\nfrom textSummarizer.models import *\n"),
    (os.path.join("textSummarizer", "helper.py"), absolute_imports),
    (os.path.join("textSummarizer", "models.py"), absolute_imports),
    (os.path.join("textSummarizer", "pipeline.py"), absolute_imports),
    (os.path.join("config", "__init__.py"), "from config.helper import *"),
    (os.path.join("config", "helper.py"), absolute_imports),
    (os.path.join("config", "config.yaml"), ""),
    (os.path.join("config", "params.yaml"), ""),
    (os.path.join("logging", "__init__.py"), "from logging.helper import *"),
    (os.path.join("logging", "helper.py"), absolute_imports),
    (os.path.join("docker", "docker_run.sh"), ""),
    (os.path.join("docker", "Dockerfile"), ""),
    (os.path.join("research", "trials.ipynb"), ""),
    (".dockerignore", "databox\n**/*__pycache__\ndocker\n"),
    (".gitignore", "databox\n**/*__pycache__\n"),
    ("main_fastapi.py", absolute_imports),
    ("main.py", absolute_imports),
    ("README.md", ""),
    ("requirements.txt", ""),
]

for file_info in list_of_files:
    file_path = Path(file_info[0])
    filedir, filename = os.path.split(file_path)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,'w') as f:
            f.write(file_info[1])
            logging.info(f"Creating empty file: {file_path}")
    
    else:
        logging.info(f"{filename} is already exists")