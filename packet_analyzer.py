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
                  "Node4.txt",
                  "Node5.txt"]

    outputNodes = ["Node1_filtered.txt",
                   "Node2_filtered.txt",
                   "Node3_filtered.txt",
                   "Node4_filtered.txt",
                   "Node5_filtered.txt"]
    headerNodes = []

    computedNodes = []

    for i in range(len(inputNodes)):
        filter(inputNodes[i], 'ICMP', outputNodes[i])
        headerNodes.append(parse(outputNodes[i]))
        computedNodes.append(run(headerNodes[i]))

    with open('MiniProject2Output.csv', 'w', newline='') as file:
        # for each node
        writer = csv.writer(file)
        # writer.writerow(["Node"]) Write node name
        writer.writerow([""])
        writer.writerow(["Echo Requests Sent", "Echo Requests Received", "Echo Replies Sent", "Echo Replies Received"])
        # Metrics go here
        writer.writerow(["Echo Requests Bytes Sent (bytes)", "Echo Requests Data Sent (bytes)"])
        # Metrics go here
        writer.writerow(["Echo Requests Bytes Received (bytes)", "Echo Requests Data Received (bytes)"])
        # Metrics go here
        writer.writerow([""])
        # Last block of metrics commented for now
        # writer.writerow(["Average RTT",  num])
        # writer.writerow(["Echo Request Throughput (kB/sec)",  num])
        # writer.writerow(["Echo Request Goodput (kB/sec)",  num])
        # writer.writerow(["Average Reply Delay (microseconds)",  num])
        # writer.writerow(["Average Echo Request Hop Count",  num])
        writer.writerow([""])


if __name__ == '__main__':
    main()
