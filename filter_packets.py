"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""

import sys

def filter(inputFilename, protocol, outputFilename):
	"""
	Reads the file and filters by protocl
	:param filename: Name of file to read from
	:param protocol: Protocol To filter
	:return:
	"""
	traffic = read_in(inputFilename)
	if protocol == '':
		return traffic
	ret = []
	for bus in traffic:
		if bus[1][4] == protocol:
			ret.append(bus)
	file = open(outputFilename, 'w')
	for bus in ret:
		bus = str(bus[1]).replace('\'','').replace(']','').replace('[','').replace(',,', '').replace(' ','')
		file.write(bus + '\n')
	file.close()
	return ret



def read_in(filename):
	"""
	Reads in a text file containing network traffic
	:param filename: Name of file to read from
	:return: An array of sub arrays that comprise a packet. Format as follows:
	traffic = [ [[Labels], [Header], [Packet Payload]...], [[Labels], [Header], [Packet Payload]...], etc.]
	Protocol type will always be located at traffic[index][1][4]
	"""
	file = open(filename, 'r')
	raw = file.readlines()
	traffic = []
	bus = []
	"""
	Gets data from file, but is very ugly and has a lot of excess formatting
	"""
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
	"""
	Add the last packet and remove empty sub array from start of traffic
	"""
	traffic.append(bus)
	traffic.pop(0)
	"""
	removes excess newline characters using and subsequent empty sub arrays
	"""
	for bus in traffic:
		for passanger in bus:
			for i in range(len(passanger)):
				passanger[i] = passanger[i].rstrip("\n")
	for i in range(len(traffic)):
		traffic[i] = recursive_remove(traffic[i])
	file.close()
	return traffic

def recursive_remove(bus):
	"""
	Recursively removes empty sub arrays from an array
	:param bus: array to remove empty sub arrays from
	:return: array with no empty sub arrays
	"""
	r = False
	for i in range(len(bus)):
		if bus[i] == ['']:
			bus.pop(i)
			r = True
			break
	if r:
		bus = recursive_remove(bus)
	return bus

def main():
	traffic = filter('Captures/Node1.txt', 'ICMP', 'debug.txt')
	#traffic = filter(str(sys.argv[(len(sys.argv) - 1)]), 'ICMP', 'debug.txt')
	for bus in traffic:
		sep = 0
		print(bus[1])
		for passanger in bus:
			if len(passanger) > sep:
				sep = len(passanger)
		for i in range(sep):
			print("-----------", end="")
		print()
if __name__ == '__main__':
    main()
