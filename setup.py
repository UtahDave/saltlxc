#!/usr/bin/python3
from setuptools import setup

setup(name='saltlxc',
      version='0.1',
      description='Create LXC containers with Salt installed',
      url='https://github.com/UtahDave/saltlxc',
      author='Dave Boucha',
      author_email='boucha@gmail.com',
      license='Apache 2.0',
      packages=['saltlxc'],
      include_package_data=True,
      install_requires=[
          'Click',
      ],
      entry_points = {
          'console_scripts': ['saltlxc=saltlxc.scripts:cli'],
      },
      zip_safe=False)
