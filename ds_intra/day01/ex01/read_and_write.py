def read_and_write():
    with open("ds.csv", "r") as data:
        info = data.read().replace('\",\"', '\"\t\"')\
                            .replace(',true', '\ttrue')\
                            .replace(',false', '\tfalse')\
                            .replace('true,', 'true\t') \
                            .replace('false,', 'false\t')
    with open("ds.tsv", 'w') as tsv:
        tsv.write(info)


if __name__ == "__main__":
    read_and_write()
