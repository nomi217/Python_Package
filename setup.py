from setuptools import setup, find_packages

# with open("README.md", 'r') as f:
#     long_description = f.read()


from setuptools import setup, find_packages

setup(
    name="calculator-project",
    version="0.1.0",
    description="A simple python calculator using modular programming",
    author="Nauman Khalid <Your Name>",
    author_email="youremail@example.com",
    packages=find_packages(),
    install_requires=[  # List dependencies from requirements.txt
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Lisence ::OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)