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


if __name__ == "__main__":
    add_time = timeit.timeit('appender()', setup="from __main__ import appender", number=90000000)
    comp_time = timeit.timeit('comprehensioner()', setup="from __main__ import comprehensioner", number=90000000)
    if add_time >= comp_time:
        print("it is better to use a list comprehension")
        print(f"{comp_time} vs {add_time}")
    else:
        print("it is better to use a loop")
        print(f"{add_time} vs {comp_time}")
