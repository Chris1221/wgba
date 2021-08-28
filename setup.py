from setuptools import setup

setup(
   name='wgba',
   version='0.1',
   python_requires='>3.6', 
   description='Which genome build again?',
   author='Chris Cole',
   author_email='ccole@well.ox.ac.uk',
   packages=['wgba'],  #same as name
      entry_points={
        'console_scripts': [
            'wgba = wgba.cli:cli',
        ],
    }
)