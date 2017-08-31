# Kool

Kool is an open source platform for online classroom management. 

This project focus is to create a minimalist framework that educationist can extend when building an online classroom management system.

## Code Example

Create a new user table and instantiate it with one record 

```
>>> from kool.contrib.auth import User
>>> tbl_user = User(first_name='Antony', last_name='Orenge', email='antony@test.com', password='secretpwd')
>>> tbl_user.save()
```

To insert a record in an existing table

```
>>> tbl_user.insert({'first_name': 'Mary', 'last_name': 'Doe', 'email': 'mary@doe.com', 'password': 'secretpwd2'})
```

To query an existing table

```
>>> from kool.db.models import where
>>> tbl_user.filter(where('last_name') == 'Doe')
```

To perform complex queries

```
>>> from kool.db.flatfile import Query
>>> User = Query()
>>> tbl_user.filter((User.first_name == 'Antony') | (User.first_name == 'Mary'))
```

## Motivation

Currently, teachers who manage online classes use several tools with different purposes. For example, they can use one application for distributing content (mailing lists, custom websites), one application for quizzes and homework submission, one application to manage gradebooks, another for classroom discussion (forums, webconferencing or chat), and several others. Our aim is to consolidate the necessary functionality into one standalone solution while keeping it lightweight, easy to deploy & use, and also make it easy to add new functionality.

## Installation

Start by setting up a virtual environment. See [Virtual Environments Tutorial](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

Once you're done, run: 

```
pip install -U pip
pip install -r requirements.txt
```

## Tests

Run test by running:

```
pytest tests/
```

## Test Coverage

Test coverage is covered by coverage and pytest-cov tools. The output report is in html format under htmlcov/dir.


## Related projects

* [Blackboard](http://www.blackboard.com/) 
* [Canvas](https://www.canvaslms.com/)
* [Chamilo](https://chamilo.org/es/)
* [Moodle](https://moodle.org/)
* [OpenEDX](https://github.com/edx/edx-platform)
* [OpenSWAD](https://openswad.org/)
* [Privacy preserving data publishing](https://github.com/rain1/Privacy-Preserving-Data-Publishing)
* [Pygrades](https://bitbucket.org/jjauhien/pygrades)
* [List on Wikipedia](https://en.wikipedia.org/wiki/List_of_learning_management_systems)

## License

Kool is licensed under MIT License
