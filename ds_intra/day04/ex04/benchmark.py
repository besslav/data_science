#!python3
import timeit
import random
from collections import Counter


def count_func(data):
    return dict(Counter(data))


def top_count(data):
    return dict(Counter(data).most_common(10))


def my_function(data):
    dict_data = {}
    for i in data:
        if i in dict_data.keys():
            dict_data[i] += 1
        else:
            dict_data[i] = 1
    return dict_data


def my_top(data):
    dict_data = {}
    for i in data:
        if i in dict_data.keys():
            dict_data[i] += 1
        else:
            dict_data[i] = 1
    return dict(sorted(dict_data.items(), key=lambda item: -item[1])[:10])


if __name__ == "__main__":
    my_list = [random.randint(0, 100) for i in range(1000)]
    print("my_function:", timeit.timeit(f'my_function({my_list})',
                                        number=10000, setup='from __main__ import my_function'))
    print("count_func:", timeit.timeit(f'count_func({my_list})',
                                       number=10000, setup='from __main__ import count_func'))
    print("my_top:", timeit.timeit(f'my_top({my_list})',
                                   number=10000, setup='from __main__ import my_top'))
    print("top_count:", timeit.timeit(f'top_count({my_list})',
                                      number=10000, setup='from __main__ import top_count'))
    print(my_top(my_list))
    print(top_count(my_list))
