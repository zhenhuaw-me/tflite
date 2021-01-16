#!/usr/bin/env python

import os
import git
"""Auto-generate the submodule importing from `tflite/tflite`"""

here = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(here, '..'))
submodule_dir = os.path.join(repo_dir, 'tflite')
the_file = os.path.join(repo_dir, 'tflite/__init__.py')

BEGIN_TAG = "########################## BELOW ARE AUTO-GENERATED ##########################\n"
END_TAG = "########################## ABOVE ARE AUTO-GENERATED ##########################\n"

# the generated import lines
pys = [ f[:-3] for f in sorted(os.listdir(submodule_dir)) \
        if os.path.isfile(os.path.join(submodule_dir, f)) and \
        f.endswith('.py') and f != '__init__.py']
imports = [ "from tflite.%s import *\n" % py for py in pys ]

# read the original file
lines = open(the_file, 'r').readlines()
begin_index = lines.index(BEGIN_TAG)
end_index = lines.index(END_TAG)

# write the new file
new_lines = lines[:begin_index+1] + imports + lines[end_index:]
with open(the_file, 'w') as f:
    for line in new_lines:
        f.write(line)

# commit change?
with git.Repo(repo_dir) as repo:
    if len(repo.git.diff(the_file)) == 0:
        print("No change, skip commit...")
        exit(0)
    input_str = input("Will commit the __init__.py change, continue [Y|N]? ")
    if input_str == 'Y':
        repo.git.add(the_file)
        repo.index.commit('Auto-generate tflite/__init__.py to new schema.fbs')

