import os
import sys


class Research:
    def __init__(self, file):
        self.file = file
        self.calculations = self.Calculations()

    def file_reader(self, has_header=True):
        with open(self.file) as data:
            rd = data.read()
            rd = rd.split('\n')
            lol = []
            sp_line = rd[0].split(",")
            if len(sp_line) != 2:
                raise ValueError('bad data(len_head)')
            if sp_line[0] in ['0', '1'] and sp_line[1] in ['0', '1']:
                has_header = False
                if sp_line[0] == sp_line[1]:
                    raise ValueError('bad data(value)')
                else:
                    lol.append([int(sp_line[0]), int(sp_line[1])])

            for line in range(1, len(rd)):
                sp_line = rd[line].split(",")
                if len(sp_line) != 2:
                    raise ValueError('bad data(len)')
                if sp_line[0] not in ['0', '1'] or sp_line[1] not in ['0', '1']:
                    raise ValueError('bad data(value)')
                elif sp_line[0] == sp_line[1]:
                    raise ValueError('bad data(value)')
                else:
                    lol.append([int(sp_line[0]), int(sp_line[1])])
            return lol

    class Calculations:
        def counts(self, data):
            x = [x[0] for x in data]
            y = [y[1] for y in data]
            return [sum(x), sum(y)]

        def fractions(self, counts):
            return [(counts[0] / (counts[0] + counts[1])) * 100,
                    (counts[1] / (counts[0] + counts[1])) * 100]


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            m = Research(sys.argv[1])
            list_data = m.file_reader()
            print(list_data)
            counted = m.calculations.counts(list_data)
            print(counted)
            print(m.calculations.fractions(counted))
        else:
            raise SyntaxError('bad argv')
    except SyntaxError as se:
        print(se)
    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnfe:
        print(fnfe)
