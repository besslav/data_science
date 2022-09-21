import sys


def extractor(file):
    with open(file, "r") as mails:
        with open("employees.tsv", "w") as data:
            data.write("Name\tSurname\tmail\n")
            for line in mails:
                sep_line = line.replace("@", ".").split(".", 2)
                sep_line[2] = line
                sep_line[0] = sep_line[0].capitalize()
                sep_line[1] = sep_line[1].capitalize()
                data.write("\t".join(sep_line))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        extractor(sys.argv[1])
    else:
        raise Exception('invalid command')
