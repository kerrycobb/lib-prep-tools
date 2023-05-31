#! /usr/bin/env python

import fire
import math

def calc(initialConc, finalConc=10, minFinalVolume=10):
    """
    Caclulate how much starting material and how much water/buffer
    are needed to acheive a desired concentration and volume
    of DNA.
    
    initialConc: Starting concentration of DNA in ng/uL
    finalConc: Desired final concentration of DNA in ng/uL
    minFinalVolume: Minimum final volume desired
    """
    c0 = initialConc
    cf = finalConc
    vf = minFinalVolume
    v0 = math.ceil((vf * cf) / c0)
    vDiff = ((v0 * c0) / cf) - v0
    print("Volume of DNA: ", v0 )
    print("Volume of Water: ", round(vDiff, 2))

if __name__ == "__main__":
    fire.Fire(calc)
