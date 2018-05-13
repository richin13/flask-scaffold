from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-Mongo-Scaffold',
    version='0.1',
    description='A tool to generate a simple flask app using MongoDB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/richin13/flask-scaffold',
    author='Ricardo Madriz',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Utilities',
        'Environment :: Console',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='flask scaffold mongodb development',
    py_modules=['flask_scaffold'],
    install_requires=['click', 'Jinja2', 'PyYAML'],
    
    entry_points={
        'console_scripts': [
            'flaask=flask_scaffold:main', # flaask command to avoid collisions with Flask's CLI utlity
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/richin13/flask-scaffold/issues',
        'Source': 'https://github.com/richin13/flask-scaffold/issues',
    },
)

