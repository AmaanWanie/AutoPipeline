# FRAMEWORK

## 1. Frontend

## src

### components

    - TaskSelection.js: Dropdown for task selection
    - ModelSelection.js: Model choice or builder
    - PreprocessingOptions.js: Preprocessing options
    - TrainingMonitor.js: Training monitor
    - InferenceUpload.js: For inference
    - EnvironmentManager.js: Create environments, select packages, view installed libraries
    - LibraryInstaller.js: Install new libraries in selected environments

### Other Files

    - App.js: Main app UI combining components
    - index.js: Frontend entry point

## 2. Backend

## app

## routes

    - task_selection.py: API for task management
    - train_model.py: API to train models
    - get_metrics.py: API to fetch training metrics
    - infer.py: API for inference
    - environment_manager.py: API for creating and managing environments
    - library_installer.py: API to install libraries in environments

## services

    - model_service.py: Logic for model management
    - preprocessing.py: Preprocessing logic
    - training.py: Model training logic
    - inference.py: Inference logic
    - environment_service.py: Logic for environment creation, deletion, listing
    - library_service.py: Logic for installing libraries

## main.py

    - Backend entry point

## 3. Core

- ├── /environments
- │   └── environment_manager.py    # Create, activate, delete environments (virtualenv/conda)
- ├── /libraries
- │   └── library_installer.py      # Install libraries in selected environments (pip/conda)
- ├── /models
- │   └── prebuilt_models.py        # Pre-built model definitions
- ├── /training
- │   └── trainer.py                # Training logic
- └── /utils
- - ├── logger.py                 # Log training, environment changes, and errors
- - └── config.py                 # Configuration settings

- /Environments
- ├── create_environment.py    # Script to create new environments
- ├── list_environments.py     # Script to list available environments
- ├── activate_environment.py  # Script to activate an environment
- ├── delete_environment.py    # Script to delete environments
- ├── /libraries
- - ├── install_library.py   # Install a library into the selected environment
  - └── list_libraries.py    # List installed libraries in the environment

- /Deployment
- ├── Dockerfile              # Container with required environments
- ├── docker-compose.yml      # Manage frontend/backend environments
- ├── /scripts
- │   └── deploy.sh           # Deployment script with environments

- /DesktopApp
- ├── main.py                 # Main entry point for the desktop app
- ├── /ui
- - ├── task_selection.ui   # GUI layout for task selection
- - ├── model_selection.ui  # GUI layout for model selection
- - ├── preprocessing.ui    # GUI layout for preprocessing options
- - ├── environment_manager.ui  # GUI layout for environment management
- - ├── training_monitor.ui # GUI layout for monitoring training
- - └── inference.ui        # GUI layout for inference
