#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging

from forms import *
import os
import random
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__, static_url_path='/static')

#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def new_main():
    butterflies = ["img/manyfly.webp", "img/mmanyfly.webp", "img/popfly.webp", "img/bf.png"]
    background = ["img/petal.gif", "img/saks.gif", "img/mmanyfly.webp", "img/manyfly.wbp"]
    fonts = ["cecep", "graw", "hey", "hot", "sns", "yakin"]
    fnt = random.choice(fonts)
    btfly = random.choice(butterflies)
    bg = random.choice(background)
    return render_template('new_main.html', the_font=fnt, b_fly=btfly, bg=bg)

@app.route('/home')
def home():
    return "was a route"
@app.route('/about')
def about():
    butterflies = ["img/manyfly.webp", "img/mmanyfly.webp", "img/popfly.webp", "img/bf.png"]
    background = ["img/petal.gif", "img/saks.gif", "img/mmanyfly.webp", "img/manyfly.webp"]
    fonts = ["cecep", "graw", "hey", "hot", "sns", "yakin"]
    fnt = random.choice(fonts)
    btfly = random.choice(butterflies)
    bg = random.choice(background)
    return render_template('about.html', the_font=fnt, b_fly=btfly, bg=bg)

@app.route('/contact')
def contact():
    butterflies = ["img/manyfly.webp", "img/mmanyfly.webp", "img/popfly.webp", "img/bf.png"]
    background = ["img/petal.gif", "img/saks.gif", "img/mmanyfly.webp", "img/manyfly.webp"]
    fonts = ["cecep", "graw", "hey", "hot", "sns", "yakin"]
    fnt = random.choice(fonts)
    btfly = random.choice(butterflies)
    bg = random.choice(background)
    return render_template('contact.html', the_font=fnt, b_fly=btfly, bg=bg)

@app.route('/mission')
def mission():
    butterflies = ["img/manyfly.webp", "img/mmanyfly.webp", "img/popfly.webp", "img/bf.png"]
    background = ["img/petal.gif", "img/saks.gif", "img/mmanyfly.webp", "img/manyfly.webp"]
    fonts = ["cecep", "graw", "hey", "hot", "sns", "yakin"]
    fnt = random.choice(fonts)
    btfly = random.choice(butterflies)
    bg = random.choice(background)
    return render_template('mission.html', the_font=fnt, b_fly=btfly, bg=bg)


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
