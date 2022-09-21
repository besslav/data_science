#!python3

import os


def main():
    os.system("echo Your current virtual env is $VIRTUAL_ENV")
    if os.environ['VIRTUAL_ENV'].split('/')[-1] != 'pskip02':
        raise Exception
    os.system('pip3 install -r requirements.txt')
    os.system("pip3 freeze > requirements.txt")


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("env wrong")
