from os import getcwd
from os.path import abspath
from flask import Flask, send_from_directory
from .build import build
from toml import load


def run(args):
    with open('Nether.toml') as file:
        config = load(file)

    static = abspath(getcwd() + '/target')
    app = Flask(config['package']['name'],
                static_url_path='/',
                static_folder=static)

    @app.route('/')
    def index():
        return send_from_directory(static, 'index.html')

    build(args)
    app.run(port=3000, debug=True)
