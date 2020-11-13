"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
"""

def parse(filename):
	"""

	:param filename:
	:return:
	"""
	file = open(filename, 'r')
	raw = file.readlines()
	traffic = []
	bus = []
	for line in raw:
		split = line.split(' ')
		line = []
		for i in range(len(split)):
			if split[i] != '':
				line.append(split[i])
		if line[0] == "No.":
			traffic.append(bus)
			bus = []
		bus.append(line)
	traffic.append(bus)
	traffic.pop(0)
	for bus in traffic:
		bus.append(bus[1][4])
	file.close()
	return traffic

def main():
	parse("Captures/Node1.txt")

if __name__ == '__main__':
    main()