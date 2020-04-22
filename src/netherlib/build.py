from os import makedirs
from os.path import abspath, dirname
from distutils.dir_util import copy_tree
from glob import glob
from pscript import py2js
from .pyx import translate
from .imports import imports2raw


def build(args):
    copy_tree('static', 'target')
    makedirs('target/scripts', exist_ok=True)

    for filename in glob('src/**/*.py', recursive=True):
        with open(filename) as file:
            code = imports2raw(translate(file.read()))
            js = py2js(
                'RawJS(\'import { h, Component, render } from "https://unpkg.com/preact?module";\')\n'
                + code)

        target_file = filename.replace('src', 'target/scripts', 1)[:-3] + '.js'

        with open(target_file, 'w') as file:
            file.write(js)
