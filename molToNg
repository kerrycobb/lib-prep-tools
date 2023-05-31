#!/usr/bin/env python

import fire

def calc(requiredMolarity, meanInsertSize):
    """
    requiredMolarity: in nMol, generally need 5 nM for Illumina HiSeq and NovoSeq
    meanInsertSize: mean number base pairs of DNA
    """
    ngPerMicroLiter = (requiredMolarity * meanInsertSize * 656.4) / 1000000
    print(ngPerMicroLiter, "ng/μL")

if __name__ == "__main__":
    fire.Fire(calc)
