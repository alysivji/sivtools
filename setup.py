from setuptools import setup, find_packages

from sivtools import __version__

setup(
    name='sivtools',
    version=__version__,
    description="General purpose toolbox",
    long_description="Pramatic programmers have their own toollbox",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        # 'Programming Language :: Python :: 2.7', #TODO get it working for py2
        'Topic :: Utilities',
    ],
    keywords='toolbox utilities',
    url='https://github.com/alysivji/sivtools',
    download_url='https://pypi.python.org/pypi/sivtools/',
    author='Aly Sivji',
    author_email='alysivji@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests', ]),
    install_requires=[''],
)
