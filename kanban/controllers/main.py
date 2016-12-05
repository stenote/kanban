from flask import Blueprint, render_template, request, redirect, flash
from kanban.models import Repo, db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', **{
        'Repos': Repo.query.all()
    })

@main.route('/add', methods=['POST'])
def add():
    if len(request.form.get('name', '')):

        r = Repo(request.form['name'])

        db.session.add(r)
        db.session.commit()

        if r.id:
            r.init()

        flash('success !')

    return redirect('/')
