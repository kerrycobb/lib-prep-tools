#! /usr/bin/env python

import fire
import math

def calc(reqMolarity, meanInsertSize):
    ## reqMolarity in nMol, generally need 5 nM for Illumina HiSeq and NovoSeq
    ## meanInsertSize in base pairs
    ngPerMicroLiter = (reqMolarity * meanInsertSize * 656.4) / 1000000
    print(ngPerMicroLiter, "ng/μL")

if __name__ == "__main__":
    fire.Fire(calc)
