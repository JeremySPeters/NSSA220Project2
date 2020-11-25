"""
@Authors:
	Jeremy Peters (jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""

from filter_packets import *
from packet_parser import *
from compute_metrics import *

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

    for i in range(len(inputNodes)):
        filter(inputNodes[i], 'ICMP', outputNodes[i])
        headerNodes.append(parse(outputNodes[i]))
    compute()
if __name__ == '__main__':
    main()
