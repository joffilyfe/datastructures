import os, setuptools

setup_path = os.path.dirname(__file__)

with open(os.path.join(setup_path, "README.md"), "r") as f:
    long_description = f.read()

setuptools.setup(
    name="datastructures",
    version="0.0.1",
    author="Joffily F",
    author_email="joffily@outlook.com",
    description="Project with some random data strucures implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "docs"]
    ),
    python_requires=">=3.7",
    test_suite="tests",
    url="https://github.com/joffilyfe/datastructures",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)