[![PyPI](https://img.shields.io/pypi/v/flask-mongo-scaffold.svg?style=flat-square)](https://pypi.org/project/Flask-Mongo-Scaffold) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-mongo-scaffold.svg?style=flat-square) [![license](https://img.shields.io/github/license/richin13/flask-scaffold.svg?style=flat-square)](https://github.com/richin13/flask-scaffold/blob/master/LICENSE)


# Flask-Scaffold

Simple tool to generate a brand new Flask application using MongoDB as data backend

## Installation

Simply run:

```
$ pip install flask-mongo-scaffold
```

## Usage

To create a new app called blog do:

```
$ flaask new blog
```

## Resulting app

```
├── blog
│   ├── api
│   │   ├── __init__.py
│   │   └── views.py
│   ├── __init__.py
│   ├── models.py
│   └── web
│       ├── __init__.py
│       ├── static
│       │   ├── css
│       │   ├── js
│       │   └── vendor
│       ├── templates
│       │   ├── base.html
│       │   └── index.html
│       └── views.py
├── config.py
├── instance
│   └── config.py
├── requirements.txt
└── run.py
```

The resulting app is a simple Flask application that comes with:

 - MongoEngine to connect with a MongoDB database backend
 - SemanticUI and JQuery

Additionally, it creates a divisional structure using Flask's blueprints to separate the
front-end part of the application from the backend. It ships with the necessary files
to setup a simple API.

## License

See LICENSE

