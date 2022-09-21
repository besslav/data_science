import os
import sys


class Research:
    def __init__(self, file):
        self.file = file

    def file_reader(self):
        with open(self.file) as data:
            rd = data.read()
            check = rd.split("\n")
            if len(check[0].split(",")) != 2:
                raise ValueError('bad header')
            for i in range(1, len(check)):
                if ((check[i][0] not in ['0', '1'])
                        or check[i][-1] not in ['0', '1']
                        or check[i][0] == check[i][-1]
                        or len(check[i]) != 3):
                    raise ValueError('bad data')

            return rd


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            m = Research(sys.argv[1])
            print(m.file_reader())
        else:
            raise SyntaxError('bad argv')
    except SyntaxError as se:
        print(se)
    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnfe:
        print(fnfe)
