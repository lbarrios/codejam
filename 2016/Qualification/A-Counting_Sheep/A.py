#!/usr/bin/env python
# -*- coding: utf-8 -*-

TOTAL_DIGITS=10

T = input()
for testcase in range(1,T+1):
	N = input()
	result = ""
	if N == 0:
		result = "INSOMNIA"
	else:
		#print "N: %s"%N
		number, count = 0, 0
		digits = [False for i in range(TOTAL_DIGITS)]
		while count < 10:
			number += N
			#print "Number: %s"%number
			str_number = str(number)
			for i in range(len(str_number)):
				digit = int(str_number[i])
				if not digits[digit]:
					count += 1
					digits[digit] = True
		result = number
	print "Case #{}: {}".format(testcase,result)
