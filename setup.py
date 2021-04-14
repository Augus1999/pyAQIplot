from setuptools import setup, find_packages

setup(
    name='pyAQIplot',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/Augus1999/pyAQIplot',
    license='GPL-3.0',
    author='Nianze Augus TAO',
    author_email='TaoN@cardiff.ac.uk',
    description='plot AQI data',
    install_requires=[
        'pandas>=1.2.4',
        'Pillow>=8.2.0',
        'matplotlib>=3.2.1',
        'numpy>=1.20.2'
    ],
    python_requires='>=3',
)
