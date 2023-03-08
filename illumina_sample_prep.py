#!/usr/bin/env python

import fire

def calc(reqd_nanoMol, avg_insert_size, cur_ng_per_ul, reqd_vol):
    ## reqd_nanoMol in nMol, generally need 5 nM for Illumina HiSeq and NovoSeq
    reqd_ng_per_ul = (reqd_nanoMol / 1000000) * 660 * avg_insert_size 
    current_mol = (cur_ng_per_ul / (660 * avg_insert_size)) * 1000000 

    v1 = (reqd_vol * reqd_ng_per_ul) / cur_ng_per_ul 
    vdif = reqd_vol - v1 

    print((
        "{mol} nM DNA with an average length of {len} bp is equal to " 
        "{ng} ng/\u03bcL of DNA\n"
        ).format(
            mol=reqd_nanoMol,
            len=avg_insert_size,
            ng=round(reqd_ng_per_ul, 3)))

    print("Sample is currently at {mol} nM\n".format(mol=round(current_mol, 3)))

    if vdif >= 0:
        print((
            "Dilute {v1} \u03bcL of {c1} ng/\u03bcL DNA with {vdif} "
           "\u03bcL of solution to get {v2} \u03bcL of {c2} ng/\u03bcL of DNA"
            ).format(
                v1=round(v1, 3),
                c1=cur_ng_per_ul,
                vdif=round(vdif, 3),
                v2=reqd_vol,
                c2=round(reqd_ng_per_ul, 3)))
    else:
        prop = cur_ng_per_ul / reqd_ng_per_ul
        min_vol = reqd_vol / prop 
        print((
            "Current sample concentration is too low.\n\n"
            "Concentrate sample to a volume less than {prop} "
            "times the current volume and requantify.\n\n"
            "Current volume must be at least {min_vol} \u03bcL or "
            "final volume will be less than {v2} \u03bcL").format(
                prop=round(prop, 3),
                min_vol=round(min_vol, 3),
                v2=reqd_vol))

if __name__ == "__main__":
    fire.Fire(calc)