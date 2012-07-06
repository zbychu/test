#!/usr/bin/env python
# -*- coding: utf8 -*- 
import codecs, random, os, commands
from subprocess import Popen, PIPE

outf = codecs.open('outfile.txt', 'a', 'utf-8')

p = Popen(['wc', '-l', 'outfile.txt'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
output = p.stdout.read()
print output
lines = int(output.split()[0])

# hundred times add ten lines to the file and then commit
for i in xrange(1,101):
  for j in xrange(lines+1,lines+101):
    lines=lines+1
    outf.write(str(lines) + ' ' + str(random.random())+'\n')
  outf.flush()  
  os.system('git add outfile.txt')
  os.system('git commit -m "append '+str(i)+'"')  

outf.close()
# finally, push the changes to the remote
os.system('git push origin master') # should be git squash
