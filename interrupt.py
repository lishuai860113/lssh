#!/bin/env python
import sys
import commands
import time
import numpy as np
np.set_printoptions(threshold=np.inf)

def get_proc_ouptput(int_name):
    status, output = commands.getstatusoutput("cat /proc/interrupts |grep " + int_name )
    return output

def get_int_list(output):
    int_list = []
    for line in output.split("\n"):
        int_list.append(line.split()[-1])
    return int_list

def get_array(output):
    array_2d = []
    for line in output.split("\n"):
        fields = [int(i) for i in line.split()[1:-2]]
        array_2d.append(fields)
    return array_2d

def main(argv):
    int_name = argv[1]
    output = get_proc_ouptput(int_name)
    int_list = get_int_list(output)
    while True:
        output = get_proc_ouptput(int_name)
        mat1 = np.mat(get_array(output))
        time.sleep(1)
        output = get_proc_ouptput(int_name)
        mat2 = np.mat(get_array(output))
        mat = mat2 - mat1
        for i in range(len(int_list)):
            print int_list[i],
            line = mat[i]
            print line.tolist()


if __name__ == "__main__":
    main(sys.argv)
