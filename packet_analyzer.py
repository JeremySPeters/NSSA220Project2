"""
@Authors:
	Jeremy Peters (jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""

from filter_packets import *
from packet_parser import *
from compute_metrics import *
import csv

def main():
    inputNodes = ["Node1.txt",
                  "Node2.txt",
                  "Node3.txt",
                  "Node4.txt"]

    outputNodes = ["Node1_filtered.txt",
                   "Node2_filtered.txt",
                   "Node3_filtered.txt",
                   "Node4_filtered.txt"]

    ipNodes = ["192.168.100.1",
               "192.168.100.2",
               "192.168.200.1",
               "192.168.200.2"]

    headerNodes = []

    computedNodes = []

    for i in range(len(inputNodes)):
        filter(inputNodes[i], 'ICMP', outputNodes[i])
    for temp in outputNodes:
        headerNodes.append(parse(temp))
    for i in range(len(headerNodes)):
        computedNodes.append(run(headerNodes[i], ipNodes[i]))

    reformattedResults = []
    for temp_1 in computedNodes:
        temp_2 = []
        for temp_3 in temp_1:
            if type([]) == type(temp_3):
                for temp_4 in temp_3:
                    temp_2.append(temp_4)
            else:
                temp_2.append(temp_3)
        reformattedResults.append(temp_2)

    #[
    # 1str(numRequestSent),
    # 2str(numRequestBytesSentFrame),
    # 3str(numRequestBytesSentICMP),
    # 4str(numReplySent),
    # 5str(numReplyBytesSentFrame),
    # 6str(numReplyBytesSentICMP),
    # 7str(numRequestRec),
    # 8str(numRequestBytesRecFrame),
    # 9str(numRequestBytesRecICMP),
    # 10str(numReplyRec),
    # 11str(numReplyBytesRecFrame),
    # 12str(numReplyBytesRecICMP)]

    # 13average_round_trip_time(packetList, hostIP),
    # 14echo_request_throughput(packetList, hostIP),
    # 15echo_request_goodput(packetList, hostIP),
    # 16average_reply_delay(packetList, hostIP),
    # 17hops_av(packetList)]













    # Reference for CSV Write
    #  [0][str(numRequestSent), str(numRequestBytesSentFrame), str(numRequestBytesSentICMP),
    #  [3]str(numReplySent), str(numReplyBytesSentFrame), str(numReplyBytesSentICMP), str(numRequestRec),
    #  [7]str(numRequestBytesRecFrame), str(numRequestBytesRecICMP), str(numReplyRec), str(numReplyBytesRecFrame),
    #  [11]str(numReplyBytesRecICMP)]
    metricResults = []

    with open('MiniProject2Output.csv', 'w', newline='') as file:
        # for each node
        writer = csv.writer(file)
        # writer.writerow(["Node"]) Write node name
        writer.writerow([""])
        # Emtpy Line

        writer.writerow(["Echo Requests Sent", "Echo Requests Received", "Echo Replies Sent", "Echo Replies Received"])
        writer.writerow([metricResults[0], metricResults[6], metricResults[3], metricResults[9]])
        writer.writerow(["Echo Requests Bytes Sent (bytes)", "Echo Requests Data Sent (bytes)"])
        writer.writerow([metricResults[1], metricResults[2]])
        writer.writerow(["Echo Requests Bytes Received (bytes)", "Echo Requests Data Received (bytes)"])
        writer.writerow(metricResults[[7], metricResults[8]])
        writer.writerow([""])
        # Emtpy Line

        # Last block of metrics commented for now
        # writer.writerow(["Average RTT",  num])
        # writer.writerow(["Echo Request Throughput (kB/sec)",  num])
        # writer.writerow(["Echo Request Goodput (kB/sec)",  num])
        # writer.writerow(["Average Reply Delay (microseconds)",  num])
        # writer.writerow(["Average Echo Request Hop Count",  num])
        # writer.writerow([""])
        # Emtpy Line


if __name__ == '__main__':
    main()
