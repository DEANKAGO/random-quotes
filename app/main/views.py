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