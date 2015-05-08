#!/usr/bin/env python2.7
# Name: Christopher Vitale
# -*- coding: utf-8 -*-

import csv

reader = csv.reader(open("tandemmain.csv", "rU"), dialect='excel')

for row in reader:
	print '''<svg width="55" height="55"><rect width="50" height="50" style="fill:rgb(''' + row[10] + "," + row[11] + "," + row[12] + ''')"></svg>'''