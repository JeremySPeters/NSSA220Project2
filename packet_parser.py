"""
@Authors:
	Jeremy Peters (Jsp7075)
    Randall Weber (rjw9659)

"""


def parse(filename):
    parseList = []
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            line = line.rstrip()
            line = line.split(", ")
            parseList.append(line)
    return parseList


def main():
    parseList = (parse('debug.txt'))
    for packet in parseList:
        print(packet)

if __name__ == '__main__':
    main()

