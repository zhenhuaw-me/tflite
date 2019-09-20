import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tflite_parser",
    version="0.0.1",
    author="王振华（Zhenhua WANG）",
    author_email="i@jackwish.net",
    description="The python package to parse TFLite models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackwish/tflite_parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
