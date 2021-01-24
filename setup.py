import os.path

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}

setuptools.setup(
    name="twilio-stubs",
    version="0.1.0",
    author="Tim Martin",
    author_email="tim@asymptotic.co.uk",
    description="Type declarations for the Twilio API",
    url="https://github.com/timmartin/twilio-stubs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['twilio-stubs'],
    install_requires=[
        "twilio>=6.47.0"
    ],
    package_data=find_stubs("twilio-stubs"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed"
    ],
    zip_safe=False
)
