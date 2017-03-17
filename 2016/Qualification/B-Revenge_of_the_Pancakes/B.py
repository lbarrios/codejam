#!/usr/bin/env python
# -*- coding: utf-8 -*-
HAPPY = "+"
BLANK = "-"

S = []
flips = 0
def make_flip(i):
	global flips, S
	j = i
	while j>=0:
		S[j] = HAPPY if S[j]==BLANK else BLANK
		j -= 1
	flips += 1
	#print "FLIP!"

T = input()
for testcase in range(1,T+1):
	S = list(raw_input())
	#print "".join(S)
	flips = 0
	for i in reversed(range(len(S))):
		s = S[i]
		if s == BLANK:
			make_flip(i)	
		#print "".join(S)
	result = flips
	print "Case #{}: {}".format(testcase,result)
