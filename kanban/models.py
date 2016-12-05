from flask.ext.sqlalchemy import SQLAlchemy
from flask import current_app
from git import Repo as R

db = SQLAlchemy()

class Repo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Repo %r>' % self.name

    def http_url(self):
        return 'http://%s.%s' % (self.name, current_app.config['DOMAIN'])

    def repo_url(self):
        return 'git@%s:/%s.git' % (current_app.config['DOMAIN'], self.name)

    def _git_path(self):
        return '%s/%s' % (current_app.config['GIT_ROOT'], self.name)

    def _web_path(self):
        return '%s/%s' % (current_app.config['WEB_ROOT'], self.name)

    def init(self):
        # init
        R.init(self._git_path(), bare=True)

        # clone
        r = R(self._git_path())
        r.clone(self._web_path())
