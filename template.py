import os
from pathlib import Path

package_name = "FinanceComplaint"

list_of_files = [
    '.github/workflows/.gitkeep',
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/configuration/__init__.py",
    f"src/{package_name}/configuration/pipeline/__init__.py",
    f"src/{package_name}/configuration/pipeline/training.py",
    f"src/{package_name}/configuration/pipeline/prediction.py",

    f"src/{package_name}/constant/database/__init__.py",
    f"src/{package_name}/constant/environment/__init__.py",
    f"src/{package_name}/constant/environment/variable_key.py",
    f"src/{package_name}/constant/model/__init__.py",
    f"src/{package_name}/constant/prediction_pipeline/__init__.py",
    f"src/{package_name}/constant/prediction_pipeline/file_config.py",
    f"src/{package_name}/constant/training_pipeline/__init__.py",

    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/entity/artifact_entity.py",
    f"src/{package_name}/entity/config_entity.py",

    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/prediction/__init__.py",
    f"src/{package_name}/components/training/__init__.py",
    f"src/{package_name}/components/training/data_ingestion.py",
    f"src/{package_name}/components/training/data_validation.py",
    f"src/{package_name}/components/training/data_preprocessing.py",
    f"src/{package_name}/components/training/model_trainer.py",
    f"src/{package_name}/components/training/model_evaluation.py",
    f"src/{package_name}/components/training/model_pusher.py",

    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/training_pipeline.py",
    f"src/{package_name}/pipeline/prediction_pipeline.py",

    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/logging.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/data_access/__init__.py", # read data from mongodb and save to current
    f"src/{package_name}/cloud_storage/__init__.py", # all the code related to cloud get and upload to s3
    f"src/{package_name}/ml/__init__.py", # Create some custome function like - custom loss function
    "configs/prediction_pipeline/file_config.yaml",
    "configs/training_pipeline/data_ingestion.yaml",
    "configs/training_pipeline/data_validation.yaml",
    "configs/training_pipeline/data_preprocessing.yaml",
    "configs/training_pipeline/model_trainer.yaml",
    "configs/training_pipeline/model_evaluation.yaml",
    "configs/training_pipeline/model_pusher.yaml",
    "params.yaml",
    "requirements.txt",
    "requirements-dev.txt",
    "setup.py"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, file_name = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
        