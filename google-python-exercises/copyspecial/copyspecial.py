#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def copy_special(tocopy, tozip, path):
# print 'tocopy = ', tocopy
# print 'tozip = ', tozip
# print 'Path = ', path
 if (tocopy):
   if not os.path.exists(tocopy):
     os.mkdir(tocopy)
 elif (tozip):
#   zippath = os.path.dirname(tozip)
#   print 'Zippath =', zippath
 
   if not os.path.exists(tozip):
     os.mkdir(tozip)
#      os.mkdir(zippath)
#     tozip = os.path.abspath(tozip)
#     print 'tozip =', tozip

 for dirs in path:
   print 'dirs = ', dirs
   special_files = os.listdir(dirs)
   print 'Special Files = =', special_files

   for file in special_files:
     print 'File = ', file
     if (re.match(r'[\w]+__[\w]+__[\w.]+', file)):
         print 'Match =', file
         if (tocopy):
           if (shutil.copy(file, tocopy)):
             print 'Error Copying file'
           else:
             print 'copied:', file,' to ', tocopy
         elif (tozip):
           file = os.path.abspath(file)
           print 'File to zip =', file
           cmd = 'zip -j %s %s' % (tozip, file)
           (status, msg) = commands.getstatusoutput(cmd)
           print 'Zip: ', msg
         else:
           print 'Error Zipping file'

    
    



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  copy_special(todir, tozip,args)
  
if __name__ == "__main__":
  main()
