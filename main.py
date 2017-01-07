#!/usr/bin/env python

import zqspy
import sys

global VERBOSE, LOGGING
VERBOSE = True
LOGFILE = None
LOGFILE = sys.argv[0] + '.log'

def printv(*args):
	zqspy.printv(*args, verbose=VERBOSE, log=LOGFILE)

printv('hi', '\nthis is a test')
printv('t', 'WOOOOT!!')
printv('e', 'oh no, an error!')