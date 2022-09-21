#!python3
import timeit


def appender():
    data = ["john@gmail.com", "james@gmail.com",
            "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    res = []
    for i in data:
        if i.endswith('@gmail.com'):
            res.append(i)
    return res


def comprehensioner():
    data = ["john@gmail.com", "james@gmail.com",
            "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    res = [x for x in data if x.endswith('@gmail.com')]
    return res


def mapper():
    data = ["john@gmail.com", "james@gmail.com",
            "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    res = map(lambda x: x if x.endswith('@gmail.com') else None, data)
    return res


if __name__ == "__main__":
    add_time = timeit.timeit('appender()', setup="from __main__ import appender", number=90000000)
    comp_time = timeit.timeit('comprehensioner()', setup="from __main__ import comprehensioner", number=90000000)
    map_time = timeit.timeit('mapper()', setup="from __main__ import mapper", number=90000000)
    all_in = sorted([add_time, comp_time, map_time])
    if all_in[0] == map_time:
        print("it is better to use a map")
        print("{}".format(' vs '.join(map(str, all_in))))
    elif all_in[0] == comp_time:
        print("it is better to use a list comprehension")
        print("{}".format(' vs '.join(map(str, all_in))))
    else:
        print("it is better to use a loop")
        print("{}".format(' vs '.join(map(str, all_in))))
