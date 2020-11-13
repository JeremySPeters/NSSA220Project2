"""
@Authors:
	Jeremy Peters (Jsp7075)
"""

def parse(filename):
	file = open(filename, 'r')
	raw = file.readlines()
	for line in raw:
		split = line.split(' ')
		print(split)
	file.close()

def main():
	parse("Captures/example.txt")

if __name__ == '__main__':
    main()