from filter_packets import *
from packet_parser import *
from compute_metrics import *

"""
@Authors:
	Jeremy Peters (Jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""


def main():
    inputNodes = ["Node1.txt" , "Node2.txt", "Node3.txt", "Node4.txt", "Node5.txt"]
    outputNodes = ["Node1_filtered.txt" , "Node2_filtered.txt", "Node3_filtered.txt", "Node4_filtered.txt", "Node5_filtered.txt"]
    for i in range(len(inputNodes)):
        filter(inputNodes[i], 'ICMP', outputNodes[i])
    parse()
    compute()
if __name__ == '__main__':
    main()
