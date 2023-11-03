#!/usr/bin/env python3
"""flask app task1
"""
from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Determines locale from our
    supported languages
    """
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config["LANGUAGES"]:
            return locale

    if 'locale' not in request.args:
        pref_user_locale = get_user_locale()
        if pref_user_locale:
            if pref_user_locale in app.config['LANGUAGES']:
                return pref_user_locale

    head_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if head_locale:
        return head_locale

    return app.config['BABEL_DEFAULT_LOCALE']


def get_user():
    """gets user id passed as URL parameter
    """
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """executed before anything
    """
    user = get_user()
    g.user = user


def get_user_locale():
    """gets users locale from mocked
    """
    users_id = g.user
    if users_id and users_id.get('locale') in app.config['LANGUAGES']:
        return users_id['locale']
    return None


@app.route('/')
def home():
    """Home page
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
