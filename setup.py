from setuptools import setup, find_packages

import os
import sys


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')
CHANGES = read('CHANGES.rst')

extra_kwargs = {}

if sys.version_info >= (3,):
    extra_kwargs = {'use_2to3': True}

setup(
    name='django-embed-video',
    packages=find_packages(),
    version='0.3',
    author='Juda Kaleta',
    author_email='juda.kaleta@gmail.com',
    url='https://github.com/yetty/django-embed-video',
    description='Django template tags for YouTube and Vimeo',
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords=['youtube', 'vimeo', 'video'],
    test_suite='embed_video.tests.tests',
    install_requires=['requests >= 1.2.3',],
    **extra_kwargs
)
