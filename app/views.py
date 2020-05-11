from flask import render_template
from app import app
from .request import get_quote

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Blog'
    quote = get_quote()
    return render_template('index.html', title=title, quote=quote)