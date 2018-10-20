from __future__ import print_function
from copy import deepcopy as dcp


def Type(x):
    return str(type(x)).split(" ")[1][1:-2]


def Str2Num(Str):
    try:
        return int(Str)
    except:
        try:
            return float(Str)
        except:
            return None