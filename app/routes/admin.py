from flask import render_template, Blueprint, request, redirect, url_for
from app import db
from app.models import Project, User, Message
from flask_login import login_user, current_user, logout_user, login_required


admin = Blueprint('admin', __name__)


@admin.route('/projects')
@login_required
def projects():
    
    portfolio = Project.query.all()
    return render_template('projects.html', title='Proyectos', portfolio=portfolio)


@admin.route('/register-project', methods=['POST', 'GET'])
@login_required
def register_project():
    if request.method == 'GET':
        return render_template('register-project.html', title='Registrar proyecto')
    else:
        form = request.form
        project = Project(title=form['title'], description=form['description'], url=form['url'], image=form['image'], category=form['category'], client=form['client'], text=form['text'])
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('main.home'))


@admin.route('/update-project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def update_project(project_id): 
    project = Project.query.filter_by(id=project_id).first()

    if request.method == 'POST':
        form = request.form
        project.title=form['title']
        project.description=form['description']
        project.url=form['url']
        project.image=form['image']
        project.category=form['category']
        project.client=form['client']
        project.text=form['text']
        db.session.commit()
        return redirect(url_for('admin.projects'))
    else:
        return render_template('update-project.html', project=project)


@admin.route('/delete-project/<int:project_id>')
@login_required
def delete_project(project_id):
    project = Project.query.filter_by(id=project_id).first()
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('admin.projects'))


@admin.route('/messages')
@login_required
def messages():
    messages = Message.query.all()
    return render_template('messages.html', title='Mensajes', messages=messages)


@admin.route('/delete-message/<int:message_id>')
@login_required
def delete_message(message_id):
    message = Message.query.filter_by(id=message_id).first()
    db.session.delete(message)
    db.session.commit()
    return redirect(url_for('admin.messages'))
