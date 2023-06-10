from setuptools import setup, find_packages

def get_requirements(file_path:str)->List[str]:#It takes a file path as input and returns a list of strings representing the requirements.
    requirements = []
    with open(file_path) as file_obj:#With statements ensures that the file is properly closed after we finish with the requirements
        for line in file_obj:
            line = line.strip()# whit strip function we remove any leading or trailing whitespace from the line 
            if not line or line.startswith("#") or line.startswith("-e"): # meaning if line is empty or starts with # and -e so it is comment, skip with continue
                continue
            requirements.append(line) #append current line to requirements
    return requirements
            
setup(name='lungcancer_project', 
      version='1.0.0', 
      author='VukDjunisijevic',
      author_email='vucina19931906@gmail.com',
      packages=find_packages(),
      install_requires= get_requirements('requirements.text'))
            
    