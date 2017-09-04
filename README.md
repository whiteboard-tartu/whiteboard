# Kool

[![CircleCI](https://circleci.com/gh/edasi/kool/tree/master.svg?style=shield)](https://circleci.com/gh/edasi/kool/tree/master)
[![codecov](https://codecov.io/gh/edasi/kool/branch/master/graph/badge.svg)](https://codecov.io/gh/edasi/kool)

Kool is an open source platform for online classroom management. 

This project focus is to create a minimalist framework that educationist can extend when building an online classroom management system.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python3. See [Python3 Tutorial](https://docs.python.org/3/tutorial/)
* Virtualenv. See [Virtual Environments Tutorial](https://docs.python.org/3/tutorial/venv.html) 
* Pip. See [Quickstart to installing Python modules](https://pip.pypa.io/en/stable/quickstart/)

### Installing

1. Setup a virtual environment

```
python3 -m venv kool-env
```

On Windows, run:
```
kool-env\Scripts\activate.bat
```

On Unix or MacOS, run:
```
source tutorial-env/bin/activate
```

2. Install requirements 

```
pip install -U pip
pip install -r requirements.txt
```


### Code Examples

On python interactive shell, start by creating a user.

```
>>> from kool.contrib.auth import User
>>> tbl_user = User(first_name='John', last_name='Doe', email='john@doe.com', password='secretpwd')
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


## Tests

On a terminal, run:

```
pytest tests/
```

### Test Coverage

Test coverage is covered by [coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/index.html) and [pytest-cov](https://github.com/pytest-dev/pytest-cov) tools. Local test reports are build in html format inside under htmlcov/dir. However, online test reports are built by [CircleCI](https://circleci.com/gh/edasi/kool/) 


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


## Documentation

Read the latest project documentation at [DOC](http://kool-docs.readthedocs.io/en/latest/)


## License

Kool is licensed under [MIT License](https://github.com/edasi/kool/blob/master/LICENSE)
