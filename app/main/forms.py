from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    username = StringField('Enter Username', validators=[
        DataRequired("Name Required")])
    email = StringField('Enter Email', validators=[
                        DataRequired("Email Required"), ])
    password = PasswordField('Enter Password', validators=[
                             DataRequired("Password Required")])
    submit = SubmitField('submit')

class LoginForm(FlaskForm):
    email = StringField('Enter Email', validators=[
                        DataRequired("Email Required"), ])
    password = PasswordField('Enter Password', validators=[
                             DataRequired("Password Required")])
    submit = SubmitField('submit')


class BlogForm(FlaskForm):
    title = StringField('Enter blog title', validators=[
                        DataRequired("Cannot be empty")])
    blog = StringField('Share your blog', validators=[
        DataRequired("Cannot be empty")])
    submit = SubmitField('submit')


class UpdateBlogForm(FlaskForm):
    title = StringField('Update blog title', validators=[
                        DataRequired("Cannot be empty")])
    blog = StringField('Update your blog', validators=[
        DataRequired("Cannot be empty")])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    comment = StringField('Enter a comment', validators=[
        DataRequired("Cannot be empty")])
    submit = SubmitField('submit')


class UpdateCommentForm(FlaskForm):
    comment = StringField('update comment', validators=[
        DataRequired("Cannot be empty")])
    submit = SubmitField('submit')
