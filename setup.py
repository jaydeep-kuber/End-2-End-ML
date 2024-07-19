from typing import List
from setuptools import find_packages, setup 


Hyphen_e_Dot = "-e ." # -e . helps to triger setup file so in may or may not read by function we need to handle it 
def get_reqs(file_path:str)-> List[str]:
    '''
    this fucntion will get all the requiremnts from requirement.txt file
    '''
    reqs = []
    with open(file_path) as file:
        reqs = file.readlines()
        reqs = [req.replace("\n", "") for req in reqs]

    if Hyphen_e_Dot in reqs:
        reqs.remove(Hyphen_e_Dot)

    return reqs




setup(

name='End to End ML project',
version='0.0.1',
author='Jaydeep',
author_email='jayofficial085@gmail.com',
packages=find_packages(),
install_requires=get_reqs('requirements.txt') # this line install all the req 

)