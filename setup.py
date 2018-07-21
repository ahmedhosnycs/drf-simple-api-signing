import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-api-signing',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='GNU GENERAL PUBLIC LICENSE',
    description='A simple Django package to facilitate request signing.',
    long_description=README,
    install_requires=['django>=1.10.0'],
    url='',
    author='Ahmed Hosny Ibrahim',
    author_email='me@ahmedhosnycs.com',
    keywords=['api_signing', 'simple_api_signing', 'django'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Server-side Development :: HTTP Request Signing',
        'Topic :: Django :: Security :: HTTP Request Signing',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
