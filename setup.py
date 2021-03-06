#!/usr/bin/env python
# from setuptools import setup
import setuptools
# compile fortran code using f2py
from numpy.distutils.core import setup, Extension

import os

# fortran module to be compiled with f2py:
admint2 = Extension(name='admint2',
                    sources=['pypride/admint2.f90'])
lagrange = Extension(name='lagrange',
                     sources=['pypride/lagrange.f90'])
# fort = Extension(name='fort',
#                  sources=['pypride/fort.f'])

# bins = [os.path.join('pypride/bin', l) for l in os.listdir('pypride/bin') if l[-3:] == '.py']

setup(name='pypride',
      description='Python Tools for Planetary Interferometry and Doppler Experiments',
      author='Dr. Dmitry A. Duev',
      author_email='duev@caltech.edu',
      url='https://github.com/dmitryduev/pypride',
      license='MIT',
      version='2.0.0b',
      platforms=['Linux', 'MacOS X'],
      packages=['pypride'],
      package_dir={'pypride': 'pypride'},
      # ext_package='pypride',
      ext_modules=[admint2, lagrange],
      # scripts=bins,
      install_requires=['astropy>=3.2.1',
                        'jplephem>=2.9',
                        'multidict>=4.7.4',
                        'numba>=0.45.1',
                        'numpy>=1.13',
                        'paramiko>=2.6.0',
                        'pysofa2>=18.1.30.4',
                        'requests>=2.22.0',
                        'scikit-learn>=0.21.3',
                        'scipy>=1.3.1']
      )
