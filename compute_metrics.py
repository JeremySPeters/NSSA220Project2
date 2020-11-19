
"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""



def compute(packetList):
	print('called compute function in compute_metrics.py')
	numRequestSent = 0
	numRequestRec = 0
	numReplySent = 0
	numReplyRec = 0
	hostIP = ''
	#How do we determine if the requests/replies are being received or sent
	#Could save IP for comparison
	for packet in packetList:
		if packet[7] == 'unreachable':
			pass
		elif packet[8] == 'request' and packet[2] == hostIP:
			numRequestSent += 1
		elif packet[8] == 'request' and packet[2] != hostIP:
			numRequestRec += 1
		if packet[8] == 'reply' and packet[2] == hostIP:
			numReplyRec += 1
		elif packet[8] == 'reply' and packet[2] != hostIP:
			numReplySent += 1



