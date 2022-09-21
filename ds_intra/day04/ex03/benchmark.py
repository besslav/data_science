#!python3
import timeit
import sys
from functools import reduce


def looper():
    n = int(sys.argv[3])
    i = 0
    step = 1 if n >= 0 else -1
    for j in range(1, n+1, step):
        i += j**2
    return i


def reduser():
    n = int(sys.argv[3])
    if n == 0:
        return 0
    step = 1 if n > 0 else -1
    return reduce(lambda x, y: x + y**2, range(1, n+1, step))


def main():
    if int(sys.argv[2]) <= 0:
        raise ValueError
    if sys.argv[1] == 'reduce':
        print(timeit.timeit('reduser()', setup="from __main__ import reduser", number=int(sys.argv[2])))
        # print(reduser())
    elif sys.argv[1] == 'loop':
        print(timeit.timeit('looper()', setup="from __main__ import looper", number=int(sys.argv[2])))
        # print(looper())
    else:
        raise ValueError


if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            main()
        except ValueError:
            print("bad arg")
    else:
        print("bad num of args")
