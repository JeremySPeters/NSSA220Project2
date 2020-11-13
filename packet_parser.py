"""
@Authors:
	Jeremy Peters (Jsp7075)
"""

def parse(filename):
	file = open(filename, 'r')
	raw = file.readlines()
	for line in raw:
		split = line.split(' ')
		line = []
		for i in range(len(split)):
			if split[i] != '':
				line.append(split[i])
		print(line)

	file.close()

def main():
	parse("Captures/example.txt")

if __name__ == '__main__':
    main()