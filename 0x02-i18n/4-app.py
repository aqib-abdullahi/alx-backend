#!/usr/bin/env python3
"""flask app task1
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """class configures available
    languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines locale from our
    supported languages
    """
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config["LANGUAGES"]:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Home page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
