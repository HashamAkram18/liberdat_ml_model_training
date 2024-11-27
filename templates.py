import os
from pathlib import Path

list_of_files = [
    ".github/workflow",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exceptions/exceptions.py",
    "tests/unit_tests/__init__.py",
    "tests/integration_tests/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "README.md",
    "LICENSE",
    "data/raw",
    "data/processed",
    "logs",
    "models",
    "outputs",
    "notebooks/data_ingestion.ipynb",
    "notebooks/data_transformation.ipynb",
    "notebooks/model_training.ipynb",
    "notebooks/model_evaluation.ipynb",
    "notebooks/prediction.ipynb",
    ".env",
    "init_setup.sh",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "Dockerfile"
    # Add more files as needed
    
]

# Create a directory structure in the current working directory
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, "w"):
            pass