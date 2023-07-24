#!/usr/bin/env python3

import os
import git
import argparse

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
    parser = argparse.ArgumentParser(description='gen_op_list')
    parser.add_argument('--no-commit', action='store_true', required=False)
    args, unknown = parser.parse_known_args()

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

    # also patch tflite/OperatorCode.py to incorporate https://github.com/zhenhuaw-me/tflite/commit/b686bf97510b55e809a2d41318d4d40ea65a1852
    op_code_fpath = os.path.join(root_dir, 'tflite', 'OperatorCode.py')
    op_code_file = ''
    with open(op_code_fpath, 'r') as f:
        op_code_lines = f.read().split('\n')
        start_builtin_code = op_code_lines.index('    def BuiltinCode(self):')
        end_builtin_code = op_code_lines.index('def OperatorCodeStart(builder):') - 1

        new_op_code_lines = op_code_lines[0:start_builtin_code]
        new_op_code_lines = new_op_code_lines + [
            """    def BuiltinCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            o = self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)

        from tflite.BuiltinOperator import BuiltinOperator
        if o < BuiltinOperator.PLACEHOLDER_FOR_GREATER_OP_CODES:
            return self.DeprecatedBuiltinCode()
        else:
            return o"""
        ]
        new_op_code_lines = new_op_code_lines + op_code_lines[end_builtin_code:]
        op_code_file = '\n'.join(new_op_code_lines)
    with open(op_code_fpath, 'w') as f:
        f.write(op_code_file)

    if not args.no_commit:
        commitChange(root_dir, dest_fpath)

    print("All done!")


if __name__ == '__main__':
    main()
