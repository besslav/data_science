#!python3
import sys

import psutil


def file_to_list_gener(file):

    with open(file) as f:
        for line in f:
            yield line


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            data = file_to_list_gener(sys.argv[1])
            for i in data:
                pass
            mem = psutil.Process().memory_info().vms / 2 ** 30
            cpu = psutil.Process().cpu_times()
            print(f'Peak Memory Usapmemge = {mem:.3f} Gb')
            print(f'User Time + System Time = {cpu.user + cpu.system:.2f}s')
        except Exception:
            print("error")
    print("bad argv")


