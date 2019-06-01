try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='data_processing',
      version='0.1',
      description='Process raw data ',
      packages=['data_processing'],
      scripts=[]
      )
