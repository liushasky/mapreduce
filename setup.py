import setuptools
from distutils.core import setup
from distutils.extension import Extension
import warnings
    
cmdclass = {}
ext_modules = []

setuptools.setup(
    name="ray-mapreduce",
    version="1.0.0",
    author="Sha Liu",
    author_email="liu226@iu.edu",
    description="Simple Mapreduce implementation based on Ray multiprocessing",
    packages=setuptools.find_packages(),
    install_requires=[
        "ray>=1.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux, Mac OS",
    ],
    python_requires='>=3.6',
    py_modules=['mapreduce'],
    cmdclass=cmdclass,
)