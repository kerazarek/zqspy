#!/usr/bin/env python

import zqspy
from zqspy import *
import sys

printv_prefs(time=False, log=True, verbose=True)

now = zqspy.now

# printv('hi', '\nthis is a test')
# printv('t', 'WOOOOT!!')
# printv('e', 'oh no, an error!')
# printv(0, 'tabbin on \nmultiple line\noh yeah\nso\nmany\nlines')
# printv(1, 'tabbin on \nmultiple line\noh yeah\nso\nmany\nlines')
# printv('m', 'tabbin on \nmultiple line\noh yeah\nso\nmany\nlines')
# printv('e', 'tabbin on \nmultiple line\noh yeah\nso\nmany\nlines')
#
# printv(zqspy.shell_command('echo', 'hi'))
# printv(now())
# printv(now('%H%M%S'))

title('COMMENCING THE THING!!!')
cr()
printv('This', 'is a test!')
