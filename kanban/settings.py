import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'secret key'

    GIT_ROOT = '/tmp/git'
    WEB_ROOT = '/tmp/web'


class ProdConfig(Config):
    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    ASSETS_DEBUG = True

    DOMAIN = '6rz.in'


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True

    WTF_CSRF_ENABLED = False
