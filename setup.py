from setuptools import setup, find_packages
import sys
from glob import glob
import os

# Build version file.
from subprocess import check_call
versionfile = os.path.join('lib','rpnpy','version.py')
makefile = 'Makefile'
if os.path.exists(makefile):
    if os.path.exists(versionfile):
        os.remove(versionfile)
    check_call(['make', '-f', makefile, 'version'], env={'rpnpy':'.'})

setup (
    name = 'eccc_rpnpy',
    version = open('VERSION').read(),
    description = 'A Python interface for the RPN libraries at Environment and Climate Change Canada',
    long_description = open('DESCRIPTION').read(),
    url='http://wiki.cmc.ec.gc.ca/wiki/Python-RPN',
    author = 'Stephane Chamberland',
    author_email='stephane.chamberland@ec.gc.ca',
    license = 'LGPL-2.1',
    keywords = 'rpnpy python-rpn vgrid librmn rmnlib libburpc',
    packages = find_packages('lib'),
    py_modules = ['Fstdc','rpn_helpers','rpnstd'],
    scripts = glob('bin/rpy.*'),
    package_dir = {'':'lib'},
    install_requires = ['numpy','pytz'],
)
