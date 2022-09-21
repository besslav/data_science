class Research:
    def file_reader(self):
        with open("data.csv") as data:
            return data.read()


if __name__ == "__main__":
    m = Research()
    print(m.file_reader())
