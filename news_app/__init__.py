from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hahaha'

import news_app.news.views
