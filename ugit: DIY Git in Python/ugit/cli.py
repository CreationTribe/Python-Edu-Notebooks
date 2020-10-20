import argparse


def main():
	args = parse_args()
	args.func(args)


def parse_args():
	parser = argparse.ArgumentParser()

	commands = parser.add_subparsers(dest='command')
	commands.required = True

	init_parser = commands.add_parser('init')
	init_parser.set_defaults(func=init)

	return parser.parse_args()


def init(args):
	print("hello butt")
uf2GmgLGzoU0G3Xm8pxLtip@JbQwtSk@QUq0VJs24yXtB0$a^lzgpocw&QPOa6voU#B2FyTI@xF6wNZIwbTpwQ0qj!q9wf%Iyms
