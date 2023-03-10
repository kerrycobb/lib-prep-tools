#! /usr/bin/env python

import fire
import math

def calc(initialConc, finalConc=10, minFinalVolume=10):
    c0 = initialConc
    cf = finalConc
    vf = minFinalVolume
    v0 = math.ceil((vf * cf) / c0)
    vDiff = ((v0 * c0) / cf) - v0
    print("Volume of DNA: ", v0 )
    print("Volume of Water: ", round(vDiff, 2))

if __name__ == "__main__":
    fire.Fire(calc)
