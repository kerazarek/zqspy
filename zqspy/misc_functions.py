#!/usr/bin/env python

from pathlib import Path
import sys, subprocess, datetime, pytz

def print0(*args):
	print(*args, end='')

def shell_command(*commands):
	process = subprocess.Popen(list(commands), stdout=subprocess.PIPE)
	process_stdout = process.communicate()
	process_stdout = process_stdout[0]
	process_stdout = process_stdout.decode()
	process_stdout = process_stdout.replace('\n', '')
	return process_stdout

def now(fmt=None):
	dt_fmt = '%m-%d-%y %H:%M:%S %z %Z'
	dt_str = shell_command('date', '+{}'.format(dt_fmt))
	dt_dt = datetime.datetime.strptime(dt_str, dt_fmt)
# 	print(dt_dt)

	if fmt is not None:
		return dt_dt.strftime(fmt)
	else:
		return dt_dt


################################################################################

# printv

message = m = 'message'
tab0 = t0 = 'tab0'
tab1 = t1 = 'tab1'
tab2 = t2 = 'tab2'
tab3 = t3 = 'tab3'

tab = lambda n: '{{:<{}}}'.format(n * 4).format('')
# formatters = {}
# formatters['message'] = formatters['m'] = '>>> {}'
# formatters['tab0'] = '  > {}'
# formatters['title'] = formatters['t'] = '>>> ~~~ {} ~~~ <<<'
# formatters['error'] = formatters['e'] = '!!! {} !!!'
#
# for n in range(10):
# 	formatter = tab(n) + formatters['tab0']
# 	formatters[n] = formatter
# 	formatters['tab' + str(n)] = formatter

formatters = {
	'message': {
		'prefix': '>>> ',
		'subprefix': '  > '
	},
	'sub': {
		'prefix': '  > '
	},
	'title': {
		'prefix': '>>> ~~~ ',
		'subprefix': tab(2),
		'suffix': ' ~~~ <<<'
	},
	'error': {
		'prefix': '!!! ',
		'subprefix': tab(1),
		'suffix': ' !!!'
	},
	'nothing': {}
}
formatters['m'] = formatters['message']
formatters['s'] = formatters['sub']
formatters['>'] = formatters['sub']
formatters['t'] = formatters['title']
formatters['e'] = formatters['error']
formatters[''] = formatters['nothing']

printv_defaults = {
	'fmt': 'message',
	'tab': 0,
	'time': False,
	'time_fmt': '%m-%d-%y %H:%M:%S',
	'verbose': True,
	'log': None,
	'logfile': None
}

def printv_prefs(**kwargs):
	if 'PRINTV_PREFS' not in globals():
		global PRINTV_PREFS
		PRINTV_PREFS = printv_defaults
	for k in kwargs:
		PRINTV_PREFS[k] = kwargs[k]

def printv(*args, **kwargs):
	if 'PRINTV_PREFS' in globals():
		prefs = PRINTV_PREFS
	else:
		prefs = printv_defaults
	for k in kwargs:
		if k in prefs:
			prefs[k] = kwargs[k]

	if prefs['verbose'] or (prefs['log'] is not None):
		output = ''
		for arg in args:
			output += str(arg)
			if len(args) > 1: output += ' '
		output_lines = output.split('\n')
		output = ''
		for l in range(len(output_lines)):
			line = output_lines[l]
			if prefs['time'] is not False:
				if type(prefs['time']) is str:
					prefs['time_fmt'] = prefs['time']
				output += '[{}] '.format(now(fmt=prefs['time_fmt']))
			output += tab(prefs['tab'])
			if 'prefix' in formatters[prefs['fmt']]:
				if l == 0 or 'subprefix' not in formatters[prefs['fmt']]:
					output += formatters[prefs['fmt']]['prefix']
				else:
					output += formatters[prefs['fmt']]['subprefix']
			output += line
			if 'suffix' in formatters[prefs['fmt']] and l == len(output_lines) - 1:
				output += formatters[prefs['fmt']]['suffix']
			output += '\n'

		if prefs['verbose']:
			print0(output)
		if prefs['log'] is not None:
			if type(prefs['log']) is str:
				prefs['logfile'] = prefs['log']
			elif prefs['logfile'] is None:
				prefs['logfile'] = '{}.log'.format(sys.argv[0])
			assert Path(prefs['logfile']).parent.is_dir(), \
				'parent dir does not exist for logfile `{}\''.format(prefs['logfile'])
			with Path(prefs['logfile']).open('a') as logfile:
				logfile.write(output)

def title(*args, **kwargs): printv(*args, **kwargs, fmt='title')
def error(*args, **kwargs): printv(*args, **kwargs, fmt='error')
def cr(): printv(fmt='nothing')



