import sys


def caesar_enc(line, shift):
    ans = []
    for i in line:
        if ord(i) > 1000:
            raise ValueError
        if i.isupper():
            ans.append(chr(((ord(i) - 65 + shift) % 26) + 65))
        elif i.islower():
            ans.append(chr(((ord(i) - 97 + shift) % 26) + 97))
        else:
            ans.append(i)
    ans = ''.join(str(x) for x in ans)
    print(ans)


def caesar_dec(line, shift):
    ans = []
    for i in line:
        if ord(i) > 1000:
            raise ValueError
        if i.isupper():
            ans.append(chr(((ord(i) - 65 - shift) % 26) + 65))
        elif i.islower():
            ans.append(chr(((ord(i) - 97 - shift) % 26) + 97))
        else:
            ans.append(i)
    ans = ''.join(str(x) for x in ans)
    print(ans)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            try:
                if sys.argv[1] == "encode":
                    caesar_enc(sys.argv[2], int(sys.argv[3]))
                elif sys.argv[1] == "decode":
                    caesar_dec(sys.argv[2], int(sys.argv[3]))
                else:
                    raise NameError
            except ValueError:
                print("bad srt")
            except NameError:
                print("invalid arg 1, use encode or decode")
        else:
            raise ValueError('invalid arguments')
    except ValueError:
        print("invalid arguments")
