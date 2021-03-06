from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mail_guesser", 
    version="0.0.2",
    author="Sachin Tripathi",
    author_email="sachintripathi@protonmail.com",
    description="A Email Guesser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snifhex/email-guesser",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)