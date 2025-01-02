from setuptools import find_packages, setup
from typing import List

HYPEN_E_BOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]  # Corrected line

        if HYPEN_E_BOT in requirements:
            requirements.remove(HYPEN_E_BOT)
    return requirements

setup(
    name='MLProject1',
    version='0.0.1',
    author='Bhavani',
    author_email='bhavanibh612@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)