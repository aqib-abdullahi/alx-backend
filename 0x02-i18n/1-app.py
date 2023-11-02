#!/usr/bin/env python3
"""flask app task1
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app, default_locale="en", default_timezone="UTC")


class Config:
    """class configures available
    languages
    """
    LANGUAGES = ["en", "fr"]
    babel_default_locale = "en"
    babel_default_timezone = "UTC"


@app.route('/')
def home():
    """Home page
    """
    return render_template('0-index.html')


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
