import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grove_4ch_relay_board-bermanmk", 
    version="0.0.1",
    author="Mark Berman",
    author_email="bermanmk@gmail.com",
    description="i2c control of grove 4ch relay board",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bermanmk/grove_4ch_relay_board",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
