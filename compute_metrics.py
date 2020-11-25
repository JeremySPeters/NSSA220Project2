"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""
from typing import Text

def run(packetList, hostIP):
	"""
	calls all 
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	1 - number of icmp Request Sent, number of bytes Sent in the icmp Request Frame, number of bytes Sent in the icmp Request ICMP feild, number of icmp Reply Sent, number of bytes Sent in the icmp Reply Frame, number of bytes Sent in the icmp Reply ICMP feild, number of icmp Request Recieved, number of bytes Recieved in the icmp Request Frame, number of bytes Recieved in the icmp Request ICMP feild, number of icmp Reply Recieved, number of bytes Recieved in the icmp Reply Frame, number of bytes Recieved in the icmp Reply ICMP feild
	2 - Round trip time
	3 - Echo request throughput
	4 - Echo request goodput
	5 - average reply delay
	6 - hop average
	"""
	
	return [compute(packetList, hostIP), average_round_trip_time(packetList, hostIP), echo_request_throughput(packetList, hostIP), echo_request_goodput(packetList, hostIP), average_reply_delay(packetList, hostIP), hops_av(packetList)]


def compute(packetList, hostIP):
	"""
	calculates average ping round trip time in milliseconds
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: number of icmp Request Sent, number of bytes Sent in the icmp Request Frame, number of bytes Sent in the icmp Request ICMP feild, number of icmp Reply Sent, number of bytes Sent in the icmp Reply Frame, number of bytes Sent in the icmp Reply ICMP feild, number of icmp Request Recieved, number of bytes Recieved in the icmp Request Frame, number of bytes Recieved in the icmp Request ICMP feild, number of icmp Reply Recieved, number of bytes Recieved in the icmp Reply Frame, number of bytes Recieved in the icmp Reply ICMP feild
	"""
	numRequestSent = 0 #1
	numRequestBytesSentFrame = 0 #2
	numRequestBytesSentICMP = 0 #3

	numRequestRec = 0 #7
	numRequestBytesRecFrame = 0 #8
	numRequestBytesRecICMP = 0 #9

	numReplyRec = 0 #10
	numReplyBytesRecFrame = 0 #11
	numReplyBytesRecICMP = 0 #12

	numReplySent = 0 #4
	numReplyBytesSentFrame = 0 #5 
	numReplyBytesSentICMP = 0 #6
#	try:
	for packet in packetList:
		if packet[7] == 'unreachable':
			pass
		elif packet[8] == 'request' and packet[2] == hostIP:
			numRequestSent += 1
			numRequestBytesSentFrame += int(packet[5])
			pac_panic: int = int(packet[5])
			numRequestBytesSentICMP += pac_panic-24

		elif packet[8] == 'request' and packet[2] != hostIP:
			numRequestRec += 1
			numRequestBytesRecFrame += int(packet[5])
			pac_panic: int = int(packet[5])
			numRequestBytesRecICMP += pac_panic-24

		if packet[8] == 'reply' and packet[2] == hostIP:
			numReplyRec += 1
			numReplyBytesRecFrame += int(packet[5])
			pac_panic: int = int(packet[5])
			numReplyBytesRecICMP += pac_panic-24

		elif packet[8] == 'reply' and packet[2] != hostIP:
			numReplySent += 1
			numReplyBytesSentFrame += int(packet[5])
			pac_panic: int = int(packet[5])
			numReplyBytesSentICMP += pac_panic-24
#	except:
#		print("fatal error in compute")
	return [str(numRequestSent), str(numRequestBytesSentFrame), str(numRequestBytesSentICMP), str(numReplySent), str(numReplyBytesSentFrame), str(numReplyBytesSentICMP), str(numRequestRec), str(numRequestBytesRecFrame), str(numRequestBytesRecICMP), str(numReplyRec), str(numReplyBytesRecFrame), str(numReplyBytesRecICMP)]

def average_round_trip_time(packetList, hostIP):
	"""
	calculates average ping round trip time in milliseconds
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: rtt (round trip time)
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	rtt = 0

	for temp_0 in packetList:
		if(temp_0[7] != 'unreachable'):
			string_temp_2: str = temp_0[9]
			array_temp_1 = string_temp_2.split("=")
			string_temp_3: str = array_temp_1[2]
			final_string = string_temp_3.replace("ttl", "")
			for temp_1 in packetList:
				if(temp_0[2] == hostIP):
					if(temp_0[8] == "request"):
						if(temp_1[7] != 'unreachable'):
							if(temp_0 != temp_1):
								string_temp_1: str = temp_1[9]
								array_temp_0 = string_temp_1.split("=")
								string_temp_2: str = array_temp_0[2]
								final_string1 = string_temp_2.replace("ttl", "")
								if(final_string1 == final_string):
									average_array.append(float(temp_1[1]) - float(temp_0[1]))

	rtt = sum(average_array) / len(average_array)
	return rtt

def echo_request_throughput(packetList, hostIP):
	"""
	calculates echo request throughput in kB/sec
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: ert (echo request throughput) 
	"""
	average_array = []
	ert = 0
	for temp_0 in packetList:
		if(temp_0[7] != 'unreachable'):
			string_temp_2: str = temp_0[9]
			array_temp_1 = string_temp_2.split("=")
			string_temp_3: str = array_temp_1[2]
			final_string = string_temp_3.replace("ttl", "")
			for temp_1 in packetList:
				if(temp_0[2] == hostIP):
					if(temp_0[8] == "request"):
						if(temp_1[7] != 'unreachable'):
							if(temp_0 != temp_1):
								string_temp_1: str = temp_1[9]
								array_temp_0 = string_temp_1.split("=")
								string_temp_2: str = array_temp_0[2]
								final_string1 = string_temp_2.replace("ttl", "")
								if(final_string1 == final_string):
									average_array.append(float(temp_1[1]) - float(temp_0[1]))

	compute_ar = compute(packetList, hostIP)
	temp_int = compute_ar[1]
	ert = float(temp_int)  / sum(average_array)
	return ert

def echo_request_goodput(packetList, hostIP):
	"""
	calculates echo request goodput in kB/sec
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: erg (echo request throughput) 
	"""
	average_array = []
	erg = 0
	for temp_0 in packetList:
		if(temp_0[7] != 'unreachable'):
			string_temp_2: str = temp_0[9]
			array_temp_1 = string_temp_2.split("=")
			string_temp_3: str = array_temp_1[2]
			final_string = string_temp_3.replace("ttl", "")
			for temp_1 in packetList:
				if(temp_0[2] == hostIP):
					if(temp_0[8] == "request"):
						if(temp_1[7] != 'unreachable'):
							if(temp_0 != temp_1):
								string_temp_1: str = temp_1[9]
								array_temp_0 = string_temp_1.split("=")
								string_temp_2: str = array_temp_0[2]
								final_string1 = string_temp_2.replace("ttl", "")
								if(final_string1 == final_string):
									average_array.append(float(temp_1[1]) - float(temp_0[1]))

	compute_ar = compute(packetList, hostIP)
	erg = float(compute_ar[3]) / sum(average_array)
	return erg

def average_reply_delay(packetList, hostIP):
	"""
	calculates average reply delay time in milliseconds
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: ard (average reply delay)
	"""
	average_array = []
	ard = 0

	for temp_0 in packetList:
		if(temp_0[7] != 'unreachable'):
			string_temp_2: str = temp_0[9]
			array_temp_1 = string_temp_2.split("=")
			string_temp_3: str = array_temp_1[2]
			final_string = string_temp_3.replace("ttl", "")
			for temp_1 in packetList:
				if(temp_0[2] != hostIP):
					if(temp_0[8] == "request"):
						if(temp_1[7] != 'unreachable'):
							if(temp_0 != temp_1):
								string_temp_1: str = temp_1[9]
								array_temp_0 = string_temp_1.split("=")
								string_temp_2: str = array_temp_0[2]
								final_string1 = string_temp_2.replace("ttl", "")
								if(final_string1 == final_string):
									average_array.append(float(temp_1[1]) - float(temp_0[1]))

	ard = sum(average_array) / len(average_array)
	return ard

def hops_av(packetList):
	"""
	deterines if a packet has left its local network then averages the number that did and did not
	:param packetList: list of ping data
	:return: average hops per echo request
	"""
	one_hop_this_time = 0
	three_hop_this_time = 0
	for temp_0 in packetList:
		if(temp_0[7] != 'unreachable'):
			string_temp_0: str = temp_0[9]
			array_temp_0 = string_temp_0.split("=")
			string_temp_1: int = array_temp_0[3]
			temp_if_hop = 129 - int(string_temp_1)
			
			if(temp_if_hop == 1):
				one_hop_this_time += 1
			elif(temp_if_hop == 3):
				three_hop_this_time += 1
			else:
				break
	total_hops = one_hop_this_time + three_hop_this_time
	avg_hops = float(three_hop_this_time/total_hops)
	return avg_hops
