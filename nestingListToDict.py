#!/usr/local/bin/python
# -*- coding: utf-8 -*-
X = ['łoję',"om","złom"]
d = {}

for path in X:
	path=path[::-1]
	current_level = d
	uni=[]
	for part in path:
		if(ord(part)>127 and len(uni)<2):
			uni.append(part)
		if(len(uni)==2):
			part = ''.join(i for i in uni)[::-1]
			uni=[]
		if(len(uni)==0):
			if part==path[-1] or part == path[::-1][0:2]:
				current_level[part] = {"valid":True}
			elif part not in current_level:
				current_level[part] = {}
			current_level = current_level[part]

print d

#print all first maches
for l in d:
	print l,d[l]

from sys import getsizeof
print getsizeof(d)