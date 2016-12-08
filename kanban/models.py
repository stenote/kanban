from flask.ext.sqlalchemy import SQLAlchemy
from flask import current_app
from git import Repo as R

import os

db = SQLAlchemy()

class Repo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name

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

        # set web_path
        with r.config_writer() as writer:
            writer.set_value('kanban', 'web', self._web_path())

        post_trigger_file = os.path.join(self._git_path(), 'hooks', 'post-update')

        with open(post_trigger_file, 'w') as f:
            f.writelines(r'''#!/bin/bash

web="$(git config kanban.web)"
branch="$(git branch)"

unset GIT_DIR

[[ ! -z "$branch" ]] && cd "$web" && git pull
exit 0
''')

        os.chmod(post_trigger_file, 0o755)

        r.clone(self._web_path())
