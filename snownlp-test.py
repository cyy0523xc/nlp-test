#!/usr/bin/python
# -*- coding: UTF-8 -*-

from snownlp import SnowNLP


filename = 'data/comments.txt'
f = open(filename, "r")
lines = f.readlines()

i = 0
for line in lines:
    line = line.strip()
    s = SnowNLP(line.decode('utf8'))
    print line
    print '====> ', s.sentiments
    i += 1
    if i > 500:
        break

print "\n\nOver!"
