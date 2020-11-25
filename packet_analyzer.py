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
    nodes = ["Node1.txt" , "Node2.txt", "Node3.txt", "Node4.txt", "Node5.txt"]
    filter()
    parse()
    compute()
if __name__ == '__main__':
    main()
