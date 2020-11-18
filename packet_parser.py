"""
@Authors:
	Jeremy Peters (Jsp7075)
    Randall Weber (rjw9659)

"""

def parse(filename):
    content = []
    with open(filename) as f:
        content = f.readlines()
        return content

def main():
    parse()


if __name__ == '__main__':
    main()

