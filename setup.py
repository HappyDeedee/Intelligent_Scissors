from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext_modules = [
    Extension(
        "intelligent_scissors_cython",
        sources=["src/intelligent_scissors_cython.pyx"],
        include_dirs=[np.get_include()]
    )
]

setup(
    ext_modules=cythonize(ext_modules),
)   