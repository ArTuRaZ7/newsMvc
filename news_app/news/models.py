from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, regexp


class User():
    def __init__(self, mail, nickname, password):
        self.email = mail
        self.nickname = nickname
        self.password = password


class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class AddUser(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    nickname = StringField("Nickname: ", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("Password", validators=[DataRequired(), regexp('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}')])
    submit = SubmitField("Submit")


class AddPost(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired(), Length(5, 50)])
    content = TextAreaField("Текст", validators=[DataRequired(), Length(10, 10000)])
    author = StringField("Nickname Автора", validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField("Submit")


users = []
posts = []
