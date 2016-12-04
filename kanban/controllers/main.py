from flask import Blueprint, render_template

from kanban.extensions import cache

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')
