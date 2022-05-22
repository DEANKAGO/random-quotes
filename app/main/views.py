import requests
from datetime import datetime

from flask import render_template
from flask_login import login_user, current_user, login_required

from . import main
from .models import User, Blog, Comment
from .forms import (RegisterForm,
                    LoginForm,
                    BlogForm,
                    UpdateBlogForm,
                    CommentForm)


@main.route('/register', methods=['GET', 'POST'])
def create_user():
    register_form = RegisterForm()
    if register_form.is_submitted():
        login_form = LoginForm()
        user = User(username=register_form.username.data,
                    email=register_form.email.data,
                    password=register_form.password.data)
        user.create()

        return render_template('login.html', form=login_form)
    return render_template("registerPage.html", form=register_form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data,
                                    password=login_form.password.data).first()

        if user:
            login_user(user)
            return render_template('home.html', user=user)

        register_form = RegisterForm()
        return render_template('registerPage.html', form=register_form)
    return render_template("login.html", form=login_form)


@main.route('/postBlog', methods=['GET', 'POST'])
@login_required
def post_blog():
    form = BlogForm()
    if form.is_submitted():
        blog = Blog(title=form.title.data,
                    blog=form.blog.data,
                    timestamp=datetime.now(),
                    user_id=current_user.id)
        blog.create()
        return render_template('singleBlog.html', blog=blog)
    return render_template('addBlog.html', form=form)


