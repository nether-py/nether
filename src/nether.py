#!/usr/bin/env python3
import sys
from netherlib.options import parse_args
from netherlib.init import init
from netherlib.build import build
from netherlib.run import run
from shutil import rmtree

args = parse_args()


def clean(args):
    rmtree('target')


subcommands = {
    'init': init,
    'build': build,
    'run': run,
    'clean': clean,
}

try:
    subcommand = subcommands[args.subcommand]
except:
    sys.exit(f'error: {args.subcommand}: subcommand is not implemented')
finally:
    subcommand(args)
