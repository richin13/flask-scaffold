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

The resulting app is a simple Flask application that comes with:

 - MongoEngine to connect with a MongoDB database backend
 - SemanticUI and JQuery

Additionally, it creates a divisional structure using Flask's blueprints to separate the
front-end part of the application from the backend. It ships with the necessary files
to setup a simple API.

## License

See LICENSE

