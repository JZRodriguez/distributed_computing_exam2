#!/usr/bin/env python3

import subprocess
import re
import sys


def create_document(size_in_MB) :
    data = "."*(1024*1024)
    with open('exam', 'w') as f :
        for i in range(0, size_in_MB) :
            f.write(data)
        f.close()


def get_time(ip, Megabytes, verbose = False) :
    create_document(Megabytes)
    run = subprocess.run(f'time scp exam {ip}', shell = True, check = True, capture_output = True)
    out = run.stderr.decode('ASCII')
    temp = re.match(".*system.([\d:\.]+)", out.strip()).group(1)
    time_list = temp.replace(".", ":").split(":")
    actual_time = int(time_list[0]) * 60 + int(time_list[1]) + int(time_list[2]) * 0.1
    subprocess.run(f'rm exam', shell = True, check = True)
    if verbose :
        print(actual_time, "s")
    return actual_time
