import setuptools

import minotorr

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='minotorr',
    version=minotorr.__version__,
    author='gokender',
    author_email='gauthier.chaty+pypi@outlook.com',
    description='Unofficial Libre Hardware Monitor python client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Gokender/minotorr',
    packages=setuptools.find_packages(include=['minotorr']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['requests'],
    test_suite='tests',
    python_requires='>=3.6',
)