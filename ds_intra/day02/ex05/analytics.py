from random import randint


class Research:
    def __init__(self, file):
        self.file = file

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
        def __init__(self, list_of_data):
            self.list_of_data = list_of_data

        def counts(self):
            x = [x[0] for x in self.list_of_data]
            y = [y[1] for y in self.list_of_data]
            return [sum(x), sum(y)]

        def fractions(self, counts):
            return [(counts[0] / (counts[0] + counts[1])) * 100,
                    (counts[1] / (counts[0] + counts[1])) * 100]

    class Analytics(Calculations):
        def predict_random(self, count_predicts):
            output = []
            for i in range(count_predicts):
                heads = randint(0, 1)
                tails = 0 if (heads == 1) else 1
                output.append([heads, tails])
            return output

        def predict_last(self):
            return self.list_of_data[-1]

        def save_result(self, data, name_of_file, type_of_file):
            with open(name_of_file + '.' + type_of_file, "w") as file:
                file.write(data)
