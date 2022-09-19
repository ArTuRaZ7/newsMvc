from news_app import app
from news_app.news.models import User, Post, users, posts, AddPost, AddUser
from flask import render_template, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html', arr=posts)


@app.route('/post/<int:n>')
def post(n):
    return render_template('post.html', post=posts[n])


@app.route('/add/user', methods=['GET', 'POST'])
def new_user():
    form = AddUser()
    if form.validate_on_submit():
        nickname = form.nickname.data
        email = form.email.data
        password = form.password.data
        users.append(User(email, nickname, password))
        return redirect(url_for('new_user'))
    return render_template('add.html', form=form, h='Добавить пользователя')


@app.route('/add/post', methods=['GET', 'POST'])
def new_post():
    form = AddPost()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        author = form.author.data
        for authors in users:
            if authors.nickname == author:
                posts.append(Post(title, content, author))
                return redirect(url_for('new_post'))
        return render_template('add.html', form=form, h='Добавить публикацию', err='Пользователя с таким ником не найдено')
    return render_template('add.html', form=form, h='Добавить публикацию')

@app.route('/persons')
def persons():
    return render_template('persons.html', arr=users)