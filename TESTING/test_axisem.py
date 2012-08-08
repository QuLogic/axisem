#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  test_axisem.py
#   Purpose:   run the AXISEM tests automatically
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#-------------------------------------------------------------------

"""
The address should be given in more flexible way (automated/....)
"""

import subprocess
import sys
import os

print '====================================================='
test_no = \
    raw_input('Please provide the number of desired tests: \n' + \
        '1. test01: explosion\n' + \
        '2. test02: dipole (mxz)\n' + \
        '3. test03: quadpole (mxz)\n' + \
        '4. test04: CMT (source: north pole)\n' + \
        '5. test05: CMT (source: 70-50)\n' + \
        '\n(format = 01,02)' + \
        '\n')
print '====================================================='

m = -1

for i in range(0, len(test_no.split(','))):
    num = test_no.split(',')[i]
    
    address = os.path.join('.', 'automated', 'test_' + num)
    
    output = subprocess.check_call(['python', 'PyAxi.py', address])
    if output != 0: print output_print
    print "=============================================="