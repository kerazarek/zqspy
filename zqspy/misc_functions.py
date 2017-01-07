#!/usr/bin/env python

global VERBOSE, LOGGING
VERBOSE = True
LOGGING = True

global message, m, tab1, t1, tab2, t2, tab3, t3
message = m = 'message'
tab0 = t0 = 'tab0'
tab1 = t1 = 'tab1'
tab2 = t2 = 'tab2'
tab3 = t3 = 'tab3'

global printv_formatters
tab = lambda n: '{{:<{}}}'.format(n * 4).format('')
printv_formatters = {
	'message': 	'>>> {text}',
	'tab0': 	'  > {text}',
	'error': 	'!!! {text} !!!'
}
for n in range(10):
	formatter = tab(n) + printv_formatters['tab0']
	printv_formatters[n] = formatter
	printv_formatters['tab' + str(n)] = formatter

def printv(*args):
	args = [arg for arg in args]
	if args[0] in printv_formatters:
		fmt = args.pop(0)
	else:
		fmt = 'message'

	output = ''
	bare_formatter = printv_formatters[fmt].format(text='')
	for arg in args:
		arg_output = str(arg)
		arg_output = arg_output.replace('\n', '\n' + bare_formatter)
		output += arg_output + ' '
	output = printv_formatters[fmt].format(text=output)

	if VERBOSE:
		print(output)

