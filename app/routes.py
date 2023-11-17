from app import app, db

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required

from werkzeug.urls import url_parse

from app.models import User, Post
from app.forms import LoginForm, PostForm

@app.route('/')
@app.route('/index')
def index():
    print('hello')
    user_data = db.session.get(User,1)
    posts = user_data.posts
    return render_template('index.html', title='home', user_data=user_data, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Main', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/add_post', methods=['GET','POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, title=form.title.data ,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post published')
        return redirect(url_for('index'))
    return render_template('add_post.html', form=form)

@app.route('/post_list', methods=['GET'])
def post_list():
    user_data = db.session.get(User,1)
    posts = user_data.posts
    return render_template('post_list.html', posts=posts)



@app.route('/post_details/<int:id>', methods=['GET'])
def post_details(id):
    post = db.session.get(Post, id)
    username = db.session.get(User, post.user_id)
    return render_template('post_details.html', post=post, username=username)
    