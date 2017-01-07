#!/usr/bin/env python

from sys import exit
from pathlib import Path

def print0(*args):
	print(*args, end='')

################################################################################

# printv

message = m = 'message'
tab0 = t0 = 'tab0'
tab1 = t1 = 'tab1'
tab2 = t2 = 'tab2'
tab3 = t3 = 'tab3'

tab = lambda n: '{{:<{}}}'.format(n * 4).format('')
formatters = {}
formatters['message'] = formatters['m'] = '>>> {}'
formatters['tab0'] = '  > {}'
formatters['title'] = formatters['t'] = '>>> ~~~ {} ~~~ <<<'
formatters['error'] = formatters['e'] = '!!! {} !!!'

for n in range(10):
	formatter = tab(n) + formatters['tab0']
	formatters[n] = formatter
	formatters['tab' + str(n)] = formatter

def printv(*args, verbose=True, log=None):
	args = [arg for arg in args]
	if args[0] in formatters:
		fmt = args.pop(0)
	else:
		fmt = 'message'
	if len(args) > 1:
		orig_args = args
		args = []
		for arg in orig_args:
			args.append(arg)
			args.append(' ')

	output = ''
	bare_formatter = formatters[fmt].format('')
	for arg in args:
		arg_output = str(arg)
		arg_output = arg_output.replace('\n', '\n' + bare_formatter)
		arg_output = arg_output.replace('\t', tab(1))
		output += arg_output
	output = formatters[fmt].format(output)

	if verbose:
		print(output)
	if log is not None:
		if not Path(log).parent.is_dir():
			message = 'parent dir of specified log (`{}\') does not exist'
			print(formatters['e'].format(message.format(log)))
			exit(1)
		with Path(log).open('a+') as log_file:
			print(repr(output))
			for line in output.split('\n'):
				log_file.write(repr(line))
				#print(repr(line))

