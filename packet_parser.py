"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
"""

def parse(filename):
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
			print("====================================================================================================")
			traffic.append(bus)
			bus = []
		bus.append(line)
		print(line)
	traffic.pop(0)
	print(traffic[0][1][4])
	file.close()

def main():
	parse("Captures/example.txt")

if __name__ == '__main__':
    main()