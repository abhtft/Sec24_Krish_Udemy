#What things can change
#1.setup case
#2.Requirement file names



from setuptools import find_packages,setup
from typing import List

'''
Here, we import find_packages and setup from the setuptools module, 
which are used to package and distribute the project. We also import the List
type from the typing module to provide type hints.

'''



HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]#list comprehension

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

'''
HYPEN_E_DOT: A constant string '-e .' which might be present in the requirements.txt file
and needs to be removed.

get_requirements(file_path: str) -> List[str]: This function reads the requirements.txt file,
processes it to remove newline characters, and removes the '-e .' entry if it exists.
The processed list of requirements is then returned.

'''


setup(
name='mlproject',
version='0.0.1',
author='Abhishek',
author_email='abh.tft@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
