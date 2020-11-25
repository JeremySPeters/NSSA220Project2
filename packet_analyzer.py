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
    node = str(sys.argv[(len(sys.argv) - 1)])
    filter()
    parse()
    compute()
if __name__ == '__main__':
    main()
