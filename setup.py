from setuptools import setup, find_packages

setup(
    name="MdcmL",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "mdcml=mdcmL.cli:main",
        ],
    },
)
