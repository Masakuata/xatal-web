from flask import render_template, Blueprint, request, redirect, url_for
from app import db
from app.models import Project, User, Message
from flask_login import login_user, current_user, logout_user, login_required


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    portfolio = Project.query.all()
    return render_template('index.html', portfolio=portfolio, title="Desarrollo y Diseño web Xatal")


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.projects'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user, remember=True)
            next_page = request.args.get("next")
            return  redirect(next_page) if next_page else redirect(url_for("admin.projects"))
    return render_template('login.html')


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@main.route('/proyecto/<int:project_id>')
def project_detail(project_id):
    project = Project.query.filter_by(id=project_id).first()
    return render_template('project-detail.html', project=project)


@main.route('/enviar-mensaje', methods=['GET', 'POST'])
def send_message():
    if request.method == 'GET':
        return redirect(url_for('main.home'))
    else:
        form = request.form
        message = Message(name=form['name'], email=form['email'], subject=form['subject'], text=form['text'])
        db.session.add(message)
        db.session.commit()
        return render_template('enviar-mensaje.html', name=form['name'])

