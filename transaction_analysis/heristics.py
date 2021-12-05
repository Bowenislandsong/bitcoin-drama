import itertools as it


'''
txOutputs takes the tx and output valid outgoing transactions that does not have the address of input
'''
from typing import Tuple


def txOutputs(tx):
    inp,outp = {},{}
    for input in tx["inputs"]:
        inp[input["prev_out"]["addr"]]=True
    for o in tx["out"]:
        if not o["addr"] in inp:
            outp[o["addr"]]=o["value"]
    return outp
