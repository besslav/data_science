def data_types():
    all_types = [5, 'str', float(5.55), True, [5], {1: "one"}, ('iterable',), {i ** 2 for i in range(10)}]
    ans = []
    for one_type in all_types:
        ans.append(type(one_type).__name__)

    print("[{}]".format(', '.join(map(str, ans))))


if __name__ == "__main__":
    data_types()



