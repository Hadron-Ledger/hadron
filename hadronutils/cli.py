import argparse
from hadronutils import utils
from hadronutils import settings

settings.change_dir('poop')

def init(args):
	utils.run_generator()

#def start(args):

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

init_parser = subparsers.add_parser('init')
init_parser.set_defaults(func=init)

start_parser = subparsers.add_parser('start')
stop_parser = subparsers.add_parser('stop')
connect_parser = subparsers.add_parser('connect')

def main():
    args = parser.parse_args()
    args.func(args)