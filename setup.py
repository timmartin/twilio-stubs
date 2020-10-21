import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twilio-stubs",
    version="0.0.1",
    author="Tim Martin",
    author_email="tim@asymptotic.co.uk",
    description="Type declarations for the Twilio API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['twilio-stubs'],
    zip_safe=False
)