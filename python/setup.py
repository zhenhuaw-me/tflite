import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tflite",
    version="0.0.1",
    author="王振华（Zhenhua WANG）",
    author_email="i@jackwish.net",
    description="The python package to parse TFLite models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jackwish.net/tflite",
    packages=setuptools.find_packages(),
    install_requires=[ 'flatbuffers',],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.5',
)
