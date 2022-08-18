
from setuptools import setup,find_packages
from typing import List

# Declare variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Samir"
DESCRIPTION="This is a first FSDS nov batch machine learning project"
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirements 
    mention in requirements.txt file

    return This function is going to return a list which contain name of 
    libraries mentioned in requirements.txt file 
    """
    with open( REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().pop("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #["housing"]
install_requires=get_requirements_list()
)