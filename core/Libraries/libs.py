import os
import subprocess
import sys

from app.services import task_select


def install_libraries(task):
    libraries = {"image": ""}

    for lib in libraries.task:
        subprocess.call(["pip", "install", lib])


libs_ = []
install_libraries(libs_)
