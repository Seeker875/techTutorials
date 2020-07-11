#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random 
import string

a2zList =  list(string.ascii_lowercase)

with open('sampleLetters.txt', 'w') as myFile:
	#sys.argv[1] for  input from command line
    for _ in range(int(sys.argv[1])):
    	#  _ is placeholder, when we dont need it
        myFile.write("%s\n" % a2zList[random.randint(0, 25)])	



