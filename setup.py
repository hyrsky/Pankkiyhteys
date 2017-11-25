import os
from distutils.core import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Pankkiyhteys',
    version='0.1',
    description='Communicate with Finnish banks',
    license='MIT License',
    author='Santeri Hurnanen',
    author_email='santeri@oikeuttaelaimille.fi',
    url='https://github.com/hyrsky/Pankkiyhteys',
    packages=['pankkiyhteys', 'pankkiyhteys.b2c', 'pankkiyhteys.finvoice'],
)