import sys


def letter_starter(mail):
    with open("employees.tsv", "r") as data:
        for line in data:
            sep_line = line.split("\t")
            if sep_line[2][-1] == "\n":
                sep_line[2] = sep_line[2][0:-1]
            if sep_line[2] == mail:
                print(f"Dear {sep_line[0]}, welcome to our team. "
                      f"We are sure that it will be a pleasure to work with you. "
                      f"That’s a precondition for the professionals that our company hires.")
                return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter_starter(sys.argv[1])
    else:
        raise Exception('invalid command')
