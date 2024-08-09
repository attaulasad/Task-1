# setup.py

from setuptools import setup, find_packages

setup(
    name="language_translation_tool",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "translate=main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A command-line tool for translating text between languages",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
