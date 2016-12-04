#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'kanban'
__email__ = 'xjmarui@gmail.com'
__version__ = '0.1'

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from kanban.controllers.main import main
from kanban import assets
from kanban.models import db

from kanban.extensions import (
    assets_env,
    debug_toolbar
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. kanban.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)

    return app
