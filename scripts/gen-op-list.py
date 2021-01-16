#!/usr/bin/env python3

import os
import git

def genOpcode2Name(file_path):
    with open(file_path, 'r') as f:
        txt = f.read()
        lines = txt.split('\n')
        lines = [line for line in lines if '=' in line]
        types = [line.split('=')[0].strip() for line in lines]
    dict_str = ["BUILTIN_OPCODE2NAME = {\n"]
    for i in range(len(types)):
        dict_str.append("    " + str(i) + ": '" + types[i] + "',\n")
    dict_str.append("}\n")
    return dict_str

def commitChange(repo_dir, the_file):
    with git.Repo(repo_dir) as repo:
        if len(repo.git.diff(the_file)) == 0:
            print("No change, skip commit...")
            exit(0)
        input_str = input("Will commit the utils.py change, continue [Y|N]? ")
        if input_str == 'Y':
            repo.git.add(the_file)
            repo.index.commit('Auto-generate tflite/utils.py to new opcode to name mapping')


def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_fpath = os.path.join(root_dir, 'tflite', 'BuiltinOperator.py')
    dict_str = genOpcode2Name(src_fpath)

    dest_fpath = os.path.join(root_dir, 'tflite', 'utils.py')

    # read the original file
    BEGIN_TAG = "########################## BELOW ARE AUTO-GENERATED ##########################\n"
    END_TAG = "########################## ABOVE ARE AUTO-GENERATED ##########################\n"
    lines = open(dest_fpath, 'r').readlines()
    begin_index = lines.index(BEGIN_TAG)
    end_index = lines.index(END_TAG)

    new_lines = lines[:begin_index+1] + dict_str + lines[end_index:]
    with open(dest_fpath, 'w') as f:
        for line in new_lines:
            f.write(line)

    commitChange(root_dir, dest_fpath)

    print("All done!")


if __name__ == '__main__':
    main()
