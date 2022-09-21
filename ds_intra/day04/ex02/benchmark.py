#!python3
import timeit
import sys


def appender():
    data = ["john@gmail.com", "james@gmail.com",
            "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    res = []
    for i in data:
        if i.endswith('@gmail.com'):
            res.append(i)
        else:
            res.append(None)
    return res


def comprehensioner():
    data = ["john@gmail.com", "james@gmail.com",
            "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    res = [x if x.endswith('@gmail.com') else None for x in data]
    return res


def mapper():
    data = ["john@gmail.com", "james@gmail.com",
            "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    res = map(lambda x: x if x.endswith('@gmail.com') else None, data)
    return res


def filterer():
    data = ["john@gmail.com", "james@gmail.com",
            "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    res = filter(lambda x: x if x.endswith('@gmail.com') else None, data)
    return res


def main():
    if int(sys.argv[2]) <= 0:
        raise ValueError
    if sys.argv[1] == 'loop':
        print(timeit.timeit('appender()', setup="from __main__ import appender", number=int(sys.argv[2])))
    elif sys.argv[1] == 'list_comprehension':
        print(timeit.timeit('comprehensioner()', setup="from __main__ import comprehensioner",
                            number=int(sys.argv[2])))
    elif sys.argv[1] == 'map':
        print(timeit.timeit('mapper()', setup="from __main__ import mapper", number=int(sys.argv[2])))
    elif sys.argv[1] == 'filter':
        print(timeit.timeit('filterer()', setup="from __main__ import filterer", number=int(sys.argv[2])))
    else:
        raise ValueError


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            main()
        except ValueError:
            print("bad input")
