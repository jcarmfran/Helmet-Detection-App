import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "helmet"

list_of_files = [
    f"src/{project_name}/__init__.py",
    ## COMPONENTS
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",
    ## CONFIGURATION
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/config/s3_operations.py",
    ## CONSTANTS
    f"src/{project_name}/constants/__init__.py",
    ## ENTITY
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifacts_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    ## EXCEPTION
    f"src/{project_name}/exception/__init__.py",
    ## LOGGER
    f"src/{project_name}/logger/__init__.py",
    ## PIPELINE
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    ## UTILS
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    "flowcharts",
    "main.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "requirements.txt",
    "setup.py",
    "research/experiment.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")