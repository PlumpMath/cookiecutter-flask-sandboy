#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig
from {{cookiecutter.app_name}}.models.foo import Foo
from {{cookiecutter.app_name}}.models.basket import Basket
from {{cookiecutter.app_name}}.extensions import db

if os.environ.get("{{cookiecutter.app_name | upper}}_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, db and the Foo model by default.
    """
    return {'app': app, 'db': db, 'Foo': Foo, 'Basket': Basket}


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
