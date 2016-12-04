from flask import Blueprint, render_template
from kanban.models import Repo

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', **{
        'Repos': Repo.query.all()
    })
