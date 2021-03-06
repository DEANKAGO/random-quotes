import requests
from datetime import datetime

from flask import render_template, redirect, url_for
from flask_login import login_user, current_user, login_required

from . import main
from .models import User, Blog, Comment
from .forms import (RegisterForm,
                    LoginForm,
                    BlogForm,
                    UpdateBlogForm,
                    CommentForm)


@main.route('/', methods=['GET'])
def home():
    _quote = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    quote = _quote.json()
    blogs = Blog.query.all()
    return render_template('home.html', user=current_user, quote=quote, blogs=blogs)


@main.route('/register', methods=['GET', 'POST'])
def create_user():
    register_form = RegisterForm()
    if register_form.is_submitted():
        login_form = LoginForm()
        user = User(username=register_form.username.data,
                    email=register_form.email.data,
                    password=register_form.password.data)
        user.create()

        return redirect(url_for('main.login'))
    return render_template("registerPage.html", form=register_form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data,
                                password=login_form.password.data).first()

        if user:
            login_user(user)
            return redirect(url_for('main.home'))

        register_form = RegisterForm()
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


@main.route('/blogs', methods=['GET'])
def get_all_blogs():
    blogs = Blog.query.all()
    return render_template('blogsIndex.html', blogs=blogs)

@main.route('/blog/<int:id>', methods=['GET'])
def get_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(blog_id=id).all()

    return render_template('singleBlog.html', blog=blog, comments=comments)


@main.route('/updateBlog/<int:id>', methods=['GET', 'POST'])
@login_required
def update_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    form = UpdateBlogForm(title=blog.title, blog=blog.blog)

    if form.is_submitted():
        blog.title = form.title.data
        blog.blog = form.blog.data
        blog.update()
        return render_template('singleBlog.html', blog=blog)

    return render_template('updateBlog.html', blog=blog, form=form)


@main.route('/deleteBlog/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    blog.delete()

    blogs = Blog.query.all()
    return render_template('blogsIndex.html', blogs=blogs)

# Comments

@main.route('/postComment/<int:blogId>', methods=['GET', 'POST'])
@login_required
def post_comment(blogId):
    form = CommentForm()
    if form.is_submitted():
        comment = Comment(comment=form.comment.data,
                          blog_id=blogId,
                          user_id=current_user.id)
        comment.create()
        return render_template('singleComment.html', comment=comment)
    return render_template('addComment.html', form=form)


@main.route('/comment/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    return render_template('singleComment.html', comment=comment)


@main.route('/updateComment/<int:id>', methods=['GET', 'POST'])
@login_required
def update_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    form = UpdateCommentForm(comment=comment.comment)

    if form.is_submitted():
        comment.comment = form.comment.data
        comment.update()
        return render_template('singleComment.html', blog=blog)

    return render_template('updateComment.html', comment=comment, form=form)


@main.route('/deleteComment/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    blog_id = comment.blog_id
    comment.delete()

    blog = Blog.query.filter_by(id=blog_id).first()
    return render_template('singleBlog.html', blog=blog)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))