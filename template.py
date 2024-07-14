import os
from pathlib import Path

# print(Path("a/b/c.txt")) # pathlib handles all "\" and "/" related issue (in windows there is "\"(backword slash) , for linux there is "/"(forword slash) )

list_of_files = [
    r".github\workflows\.gitkeep",
    r"src\__init__.py",
    r"src\components\__init__.py", #component is part of pipeline
    r"src\components\data_ingestion.py",
    r"src\components\data_transformation.py",
    r"src\components\model_trainer.py",
    r"src\components\model_evaluation.py",
    r"src\pipeline\__init__.py",
    r"src\pipeline\training.py",
    r"src\pipeline\prediction_pipeline.py",
    r"src\utils\__init__.py",
    r"src\utils\utils.py",
    r"src\logger\logging.py",
    r"src\exception\exception.py",
    r"test\unit\__init__.py",
    r"test\integration\__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.py",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    r"experiment\experiments.ipynb",
]

 
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass # create empty file

