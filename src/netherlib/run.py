from os import getcwd
from os.path import abspath
from flask import Flask, send_from_directory
from .build import build
from toml import load
from threading import Thread
from time import sleep


def rebuild(args):
    while True:
        build(args)
        sleep(1)


def run(args):
    with open('Nether.toml') as file:
        config = load(file)

    static = abspath(getcwd() + '/target')
    app = Flask(config['package']['name'],
                static_url_path='/',
                static_folder=static)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/')
    def index():
        return send_from_directory(static, 'index.html')

    Thread(target=rebuild, args=(args, )).start()
    app.run(port=3000, debug=True)
