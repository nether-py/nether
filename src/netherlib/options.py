import argparse
import textwrap

parser = argparse.ArgumentParser(
    description='A framework for building user interfaces',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''\
        Some common nether subcommands are:
            build      compile the current package
            clean      remove the target directory
            run        run a development server
            init       create a new nether package
        '''))

parser.add_argument('subcommand', metavar='SUBCOMMAND', type=str)


def parse_args():
    return parser.parse_args()
