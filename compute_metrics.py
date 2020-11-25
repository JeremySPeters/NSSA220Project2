"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""
import sys
import threading
from typing import Text


def compute(packetList):
	print('called compute function in compute_metrics.py')
	numRequestSent = 0
	numRequestBytesSentFrame = 0
	numRequestBytesSentICMP = 0

	numRequestRec = 0
	numRequestBytesRecFrame = 0
	numRequestBytesRecICMP = 0

	numReplyRec = 0
	numReplyBytesRecFrame = 0
	numReplyBytesRecICMP = 0

	numReplySent = 0
	numReplyBytesSentFrame = 0
	numReplyBytesSentICMP = 0
	hostIP = '192.168.100.1'

	#How do we determine if the requests/replies are being received or sent
	#Could save IP for comparison
	for packet in packetList:
		if packet[7] == 'unreachable':
			pass
		elif packet[8] == 'request' and packet[2] == hostIP:
			numRequestSent += 1
			numRequestBytesSentFrame += packet[5]
			numRequestBytesSentICMP += (packet[5]-24)

		elif packet[8] == 'request' and packet[2] != hostIP:
			numRequestRec += 1
			numRequestBytesRecFrame += packet[5]
			numRequestBytesRecICMP += (packet[5]-24)

		if packet[8] == 'reply' and packet[2] == hostIP:
			numReplyRec += 1
			numReplyBytesRecFrame += packet[5]
			numReplyBytesRecICMP += (packet[5]-24)

		elif packet[8] == 'reply' and packet[2] != hostIP:
			numReplySent += 1
			numReplyBytesSentFrame += packet[5]
			numReplyBytesSentICMP += (packet[5]-24)

def average_round_trip_time(packetList):
	"""
	calculates average ping round trip time in milliseconds
	:param packetList: list of ping data
	:return: RTT (round trip time)
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	RTT = 0

	hostIP = '192.168.100.1'
	while temp_0 <= len(packetList):
		if(packetList[temp_0][2] == hostIP and packetList[temp_0][8] == "request"):
			while temp_1 <= len(packetList):
				if(temp_0 != temp_1):
					if(packetList[temp_0][9] == packetList[temp_1][9]): #debug.txt is incorrectly formated for comparison requires more devisions to correctly compare!!!!!!
						average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
			temp_1 += 1
		temp_0 += 1
		temp_1 = 0
	RTT = sum(average_array) / len(average_array)
	return RTT

def echo_request_throughput(packetList):
	"""
	calculates echo request throughput in kB/sec
	:param packetList: list of ping data
	:return: ERT (echo request throughput) 
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	ERT = 0

	hostIP = '192.168.100.1'
	while temp_0 <= len(packetList):
		if(packetList[temp_0][2] == hostIP and packetList[temp_0][8] == "request"):
			while temp_1 <= len(packetList):
				if(temp_0 != temp_1):
					if(packetList[temp_0][9] == packetList[temp_1][9]): #debug.txt is incorrectly formated for comparison requires more devisions to correctly compare!!!!!!
						average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
			temp_1 += 1
		temp_0 += 1
		temp_1 = 0
	ERT = compute.numRequestBytesSentFrame / sum(average_array)
	return ERT

def echo_request_goodput(packetList):
	"""
	calculates echo request goodput in kB/sec
	:param packetList: list of ping data
	:return: ERT (echo request throughput) 
	"""
	temp_0 = 0
	temp_1 = 0
	average_array = []
	ERG = 0

	hostIP = '192.168.100.1'
	while temp_0 <= len(packetList):
		if(packetList[temp_0][2] == hostIP and packetList[temp_0][8] == "request"):
			while temp_1 <= len(packetList):
				if(temp_0 != temp_1):
					if(packetList[temp_0][9] == packetList[temp_1][9]): #debug.txt is incorrectly formated for comparison requires more devisions to correctly compare!!!!!!
						average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
			temp_1 += 1
		temp_0 += 1
		temp_1 = 0
	ERG = compute.numRequestBytesSentICMP / sum(average_array)
	return ERG

def average_reply_delay(packetList):
	"""
	calculates average reply delay time in millisecondsx
	:param packetList: list of ping data
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
				if(temp_0 != temp_1):
					if(packetList[temp_0][9] == packetList[temp_1][9]): #debug.txt is incorrectly formated for comparison requires more devisions to correctly compare!!!!!!
						average_array.apend(packetList[temp_1][1]-packetList[temp_0][1])
			temp_1 += 1
		temp_0 += 1
		temp_1 = 0
	ARD = sum(average_array) / len(average_array)
	return ARD

def total_hops(packetList):
	"""
	docstring
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
	return




#string_temp_0: str = packetList[temp_0][9]
#			array_temp_0 = string_temp_0.split("=")
#			string_temp_1: str = array_temp_0[2]
#			string_temp_1.replace("ttl", "")