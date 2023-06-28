#!/usr/bin/python

from setuptools import setup, find_packages
import os 

def func_read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read();

setup(
    name   ='keras_callbacks',
    version='0.1.0',
    author ='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    maintainer='Fernando Pujaico Rivera',
    maintainer_email='fernando.pujaico.rivera@gmail.com',
    url='https://github.com/trucomanx/keras_callbacks',
    license='GPLv3',
    description='Keras callbacks.',
    long_description=func_read('README.txt'),
    packages=find_packages(where='.'),
    #package_dir={'':'./'},
    package_data = {
        'keras_callbacks': ['*.py']
    },
    keywords=['callbacks'],
    install_requires=[
       "tensorflow",
       "numpy", #"Django >= 1.1.1",
       "gtts",
       "ipython"
    ],
)

print("")
print("find_packages(where=\'.\');")
print(find_packages(where='.'))

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/keras_callbacks-0.1.0.tar.gz 
