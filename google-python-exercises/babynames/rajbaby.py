#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename,"rU")
  file_txt = f.read()
  year_line = re.search(r'(Popularity\sin\s)([\d\d\d\d]+)',file_txt)
  year = year_line.group(2)
  print 'Year =', year
  f.close()
  f = open(filename,"rU")
  rank_male = {}
  rank_female = {}
  for line in f:
    extract = re.search('<td>([0-9]+)</td><td>([A-z]+)</td><td>([A-z]+)</td>', line)
    if extract:
      rank = extract.group(1)
      rank_male[rank] = extract.group(2)
      rank_female[rank] = extract.group(3)
    
  print combine_dict(rank_male, rank_female)

def combine_dict(dict1, dict2):
  combined_dict = {}
  for key in dict1.keys():
    if (dict2[key]):
      combined_dict[key] = (dict1[key], dict2[key])
  return combined_dict

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for file in args:
    name_list = extract_names(file)
  


  
if __name__ == '__main__':
  main()
