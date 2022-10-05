import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_magic_file",
    version="0.0.6",
    author="Valtteri Remes",
    description="Small Python module to aid developers in getting file extensions from files securely.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    py_modules=["python_magic_file"],
    install_requires=[
        "python-magic == 0.4.27; platform_system != 'Windows'",
        "python-magic-bin == 0.4.14; platform_system == 'Windows'"
    ],
    url="https://github.com/vremes/python-magic-file",
)
