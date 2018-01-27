from setuptools import setup, find_packages

setup(
    name='sivtools',
    version='0.0.1',
    description="Sivji's Toolbox",
    url='https://github.com/alysivji/sivtools',
    author='Aly Sivji',
    author_email='alysivji@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(exclude=['tests', ]),
    install_requires=[''],
    download_url='https://github.com/alysivji/sivtools',
)
