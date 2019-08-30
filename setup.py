import setuptools
from paystackpy import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paystackpy",
    version=version.__version__,
    author=version.__author__,
    author_email="confiyobo@gmail.com",
    description="A Paystack API wrapper with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ConfiYobo/paystackpy",
    packages=setuptools.find_packages(),
    download_url='https://github.com/ConfiYobo/paystackpy/archive/0.05.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
