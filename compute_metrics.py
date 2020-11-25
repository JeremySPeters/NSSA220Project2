"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""
from typing import Text

def run(packetList, hostIP):
	return [compute(packetList, hostIP), average_round_trip_time(packetList, hostIP), echo_request_throughput(packetList, hostIP), echo_request_goodput(packetList, hostIP), average_reply_delay(packetList, hostIP), hops_av(packetList)]


def compute(packetList, hostIP):
	"""
	calculates average ping round trip time in milliseconds
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: number of icmp Request Sent, number of bytes Sent in the icmp Request Frame, number of bytes Sent in the icmp Request ICMP feild, number of icmp Reply Sent, number of bytes Sent in the icmp Reply Frame, number of bytes Sent in the icmp Reply ICMP feild, number of icmp Request Recieved, number of bytes Recieved in the icmp Request Frame, number of bytes Recieved in the icmp Request ICMP feild, number of icmp Reply Recieved, number of bytes Recieved in the icmp Reply Frame, number of bytes Recieved in the icmp Reply ICMP feild
	"""
	print('called compute function in compute_metrics.py')
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
	:return: RTT (round trip time)
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	RTT = 0

	while temp_0 <= len(packetList):
		if packetList[temp_0][9] == "unreachable)":
			pass
		elif(packetList[temp_0][2] == hostIP):
			if(packetList[temp_0][8] == "request"):
				string_temp_0: str = packetList[temp_0][9]
				array_temp_0 = string_temp_0.split("=")
				string_temp_1: str = array_temp_0[2]
				string_temp_1.replace("ttl", "")

				string_temp_2: str = packetList[temp_1][9]
				array_temp_1 = string_temp_2.split("=")
				string_temp_3: str = str(array_temp_1[2])
				string_temp_3.replace("ttl", "")

				while temp_1 <= len(packetList):
					if(temp_0 != temp_1):
						if(packetList[temp_0][9] == string_temp_3):
							average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
				temp_1 += 1
			temp_1 = 0
			RTT = sum(average_array) / len(average_array)
		temp_0 += 1
	return RTT

def echo_request_throughput(packetList, hostIP):
	"""
	calculates echo request throughput in kB/sec
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: ERT (echo request throughput) 
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	ERT = 0

	while temp_0 <= len(packetList):
		if(packetList[7] == "unreachable"):
				pass
		if(packetList[temp_0][2] == hostIP and packetList[temp_0][8] == "request"):
			string_temp_0: str = packetList[temp_0][9]
			array_temp_0 = string_temp_0.split("=")
			string_temp_1: str = array_temp_0[2]
			string_temp_1.replace("ttl", "")
			string_temp_2: str = packetList[temp_1][9]
			array_temp_1 = string_temp_2.split("=")
			string_temp_3: str = array_temp_1[2]
			string_temp_3.replace("ttl", "")

			while temp_1 <= len(packetList):
				if(temp_0 != temp_1):
					if(packetList[temp_0][9] == string_temp_3):
						average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
			temp_1 += 1
		temp_0 += 1
		temp_1 = 0
	ERT = compute.numRequestBytesSentFrame / sum(average_array)
	return ERT

def echo_request_goodput(packetList, hostIP):
	"""
	calculates echo request goodput in kB/sec
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: ERT (echo request throughput) 
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	ERG = 0

	hostIP = '192.168.100.1'
	while temp_0 <= len(packetList):
		if(packetList[temp_0][2] == hostIP and packetList[temp_0][8] == "request"):
			string_temp_0: str = packetList[temp_0][9]
			array_temp_0 = string_temp_0.split("=")
			string_temp_1: str = array_temp_0[2]
			string_temp_1.replace("ttl", "")
			
			string_temp_2: str = packetList[temp_1][9]
			array_temp_1 = string_temp_2.split("=")
			string_temp_3: str = array_temp_1[2]
			string_temp_3.replace("ttl", "")

			while temp_1 <= len(packetList):
				if(temp_0 != temp_1):
					if(packetList[temp_0][9] == string_temp_3):
						average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
			temp_1 += 1
		temp_0 += 1
		temp_1 = 0
	ERG = compute.numRequestBytesSentICMP / sum(average_array)
	return ERG

def average_reply_delay(packetList, hostIP):
	"""
	calculates average reply delay time in milliseconds
	:param packetList: list of ping data
	:param hostIP: ip of the host pc 
	:return: ARD (average reply delay)
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	ARD = 0

	hostIP = '192.168.100.1'
	while temp_0 <= len(packetList):
		if(packetList[temp_0][2] != hostIP and packetList[temp_0][8] == "request"):
			while temp_1 <= len(packetList[temp_0]): # just a hunch but posible issue fix
				string_temp_0: str = packetList[temp_0][9]
				array_temp_0 = string_temp_0.split("=")
				string_temp_1: str = array_temp_0[2]
				string_temp_1.replace("ttl", "")

				string_temp_2: str = packetList[temp_1][9]
				array_temp_1 = string_temp_2.split("=")
				string_temp_3: str = array_temp_1[2]
				string_temp_3.replace("ttl", "")

				if(temp_0 != temp_1):
					if(packetList[temp_0][9] == string_temp_3):
						average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
			temp_1 += 1
		temp_0 += 1
		temp_1 = 0
	ARD = sum(average_array) / len(average_array)
	return ARD

def hops_av(packetList):
	"""
	deterines if a packet has left its local network then averages the number that did and did not
	:param packetList: list of ping data
	:return: average hops per echo request
	"""
	temp_0 = 0
	temp_1 = 0
	one_hop_this_time = 0
	three_hop_this_time = 0
	while temp_0 <= len(packetList):
		while temp_1 <= len(packetList[temp_0]):
			string_temp_0: str = packetList[temp_0][9]
			array_temp_0 = string_temp_0.split("=")
			string_temp_1: int = array_temp_0[3]
			temp_if_hop = 129 - string_temp_1
			
			if(temp_if_hop == 1):
				one_hop_this_time += 1
			elif(temp_if_hop == 3):
				three_hop_this_time += 1
			else:
				break
			temp_1 += 1
		temp_0 += 1
	total_hops = one_hop_this_time + three_hop_this_time
	avg_hops = float(three_hop_this_time/total_hops)
	return avg_hops