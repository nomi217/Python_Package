# Modularization in Python

This project demonstrates how to modularize a Python project for better organization and maintainability.

## Calculator Project - Modular Python with Virtual Environments, Requirements, Testing

### Introduction
This project demonstrates modular programming principles in Python, leveraging virtual environments for dependency isolation, requirements.txt for package management, a well-structured setup.py for packaging, and pytest for unit testing.

### Modularization
Modularization breaks down your code into well-defined, reusable components. In this project, you'll likely have modules for:

- Calculations (addition, subtraction, multiplication, division, etc.)
- Print Output
- Error handling (validation, exception management)

<br>
Each module will contain functions and classes specific to its task, promoting code organization and maintainability.

## Setup Virtual Environment
1. To set up a virtual environment for this project, follow these steps:
2. First, ensure you have Python installed on your system. You can download and install Python from python.org.

3. Once Python is installed, open a terminal or command prompt.

4. Navigate to the directory where you want to create your virtual environment.

5. <b>Install virtualenv if you haven't already:</b>
```bash
pip install virtualenv
```
6. <b>Create a new virtual environment:</b>
```bash
virtualenv venv
```
7. <b>Activate the virtual environment:</b>

- On Windows:
```bash
venv\Scripts\activate
```
- On Unix or MacOS:
```bash
source venv/bin/activate
```
## Install Libraries/Dependencies
To install the required libraries for this project like pytest etc, use the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Directory Structure
```bash
calculator/
│
├── calculator/
│   ├── __init__.py
│   └── calculator_functionality.py
│
├── calculator_test/
│   ├── __init__.py
│   └── test_calculation.py
│
├── main.py
├── README.md
├── requirements.txt
└── setup.py
```

## Usage
### Calculator Functionality Module
### (`calculator/calculator_functionality.py`)
The calculator_functionality.py module defines functions for basic arithmetic operations such as addition, subtraction, multiplication, and division.

### Testing Functionality Module
### (`calculator_test/test_calculation.py`)
The test_calculation.py file contains test cases for the calculator functionality. It uses the pytest framework to run the tests.

### `main.py`
The main.py file contains the main program logic. It imports functions from calculator.calculator_functionality module to perform arithmetic operations and print output.

To run the main program, execute:
```bash
python main.py
```

## Setup.py
Create a setup.py file at the root of your project with the following details. The setup.py file is used to configure the project for distribution. It includes metadata about the project such as name, version, dependencies, etc. Make sure to update it accordingly for your project.
```
from setuptools import setup, find_packages

setup(
    name="calculator-project",
    version="0.1.0",
    description="A modular Python calculator",
    author="Your Name",
    author_email="youremail@example.com",
    packages=find_packages(),
    install_requires=[  # List dependencies from requirements.txt
        "numpy",
    ],
)
```

## Running Tests
To run tests for this project using pytest first go to directory Where you have written test cases, then execute the following command:
This will run all the test cases in the project.
```
pytest 
```
Or if you want to test a specific test cases, use this command:
```
pytest filename.py
```

To check the more details of test cases, use this command:
```
py.test -v 
```
The `py.test -v` command is used to run tests using the pytest framework in verbose mode. This means that it will display more detailed information about the tests being executed, including the names of individual test functions and the results of each test case. The `-v` flag stands for "verbose" and is useful for debugging and understanding the test execution process.

## License File
Include a license file (e.g., LICENSE.txt) to specify how your code can be used and distributed. Popular options include MIT, Apache 2.0, GPLv3. Choose one that aligns with your project's goals.



After completing the setup of your Python project, including creating the necessary files like setup.py, license.txt, and requirements.txt, and generating the distribution packages using `python setup.py sdist bdist_wheel`, the next steps involve local testing and deployment to a test environment, such as TestPyPI. Here's a brief explanation of these steps:

1. <b>Local Testing:  </b>
   - Before deploying your project, it's essential to test it locally to ensure everything works as expected.
   - You can install your project's dependencies using pip install -r requirements.txt.
   - Then, run your project locally to verify that it functions correctly.
   -  You can execute python main.py or whatever command is appropriate for running your project.

2. <b>Building Distribution Packages:</b>
   - Once you've confirmed that your project works locally, you can build the distribution packages using `python setup.py sdist - bdist_wheel`.
   - This command generates source and binary distribution packages that are ready for distribution.

3. <b>Generated Files:</b>
   - After running the build command, you will find the generated files in the following directories:
   - <b>build/</b>: Contains intermediate build files.
      -  This directory contains intermediate build files generated during the build process.
      -  It includes files necessary for building the distribution packages.
   - <b>dist/</b>: Contains the final distribution packages.
      -  This directory contains the final distribution packages that are ready for distribution.
      -  It typically includes the following files:
         -  `simple_calculator-0.1-py3-none-any.whl`: Wheel distribution package.
         -  `simple_calculator-0.1.tar.gz`: Source distribution package.
   - <b>simple_calculator.egg-info/</b>: Contains metadata files about the package:
      -  This directory contains metadata and information about the distribution packages.
      - It typically includes the following files:
         - `dependency_links.txt`: List of URLs for dependencies.
         - `PKG-INFO`: Metadata about the package.
         - `SOURCES.txt`: List of source files included in the distribution.
         - `top_level.txt`: List of top-level package directories.

4. <b>Deployment to TestPyPI:</b>
   - TestPyPI is a separate instance of the Python Package Index (PyPI) intended for testing purposes.
   - After successfully building the distribution packages, you can deploy them for testing purposes.
   - First, install the twine package if you haven't already: pip install twine.
   - One common approach is to upload the distribution packages to a Python package repository like TestPyPI.
   - Then, upload your distribution packages to TestPyPI using this command:
    ```
     twine upload --repository-url https://test.pypi.org/legacy/ dist/*.
    ```
   - You'll be prompted to enter your TestPyPI username and password.
5. <b>Testing on TestPyPI:</b>
   - Once your packages are uploaded to TestPyPI successfully, you can install them in a test environment using 
    ```
    pip install --index-url https://test.pypi.org/simple/<package-name>
    ```
   - TestPyPI allows you to verify that your packages can be installed correctly and work as expected in a real-world scenario.
6. <b>Final Deployment:</b>
   - After testing on TestPyPI, if everything looks good, you can proceed with the final deployment to the production Python package repository, such as PyPI.
   - You can follow a similar process to upload your packages to PyPI using twine.
</br>
</br>


By following these steps, you can ensure that your Python project is thoroughly tested locally and deployed to a test environment like TestPyPI before making it available to users on the main PyPI repository or other distribution channels.
</br>
</br>
Happy coding! I hope this guide simplifies Python package creation for you. :snake: :sparkles:

