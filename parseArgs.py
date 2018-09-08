# -*- coding: utf-8 -*-
from __future__ import print_function
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("pos1", help="positional argument 1")
parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default=None)
parser.add_argument("-i", "--int-arg", help="int argument", dest="argint", default=0)
args = parser.parse_args()
print("positional arg:", args.pos1)
if args.opt:
	print("optional arg:", args.opt)
if args.argint:
	print("int arg:", args.argint)
	print("int arg type:", type(args.argint))
