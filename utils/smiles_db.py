import mbuild as mb
import numpy as np


dict_branches = {
        }

dict_groups = {
        }

dict_backbone = {
        "ptb7": "c5cc4cc3sc(c2c1sccc1cs2)cc3cc4s5",
        "benzodithiophene": "c3cc2cc1sccc1cc2s3",
        "thiophene": "c1csc2c1scc2",
        "ptaa": "N(c1ccccc1)(c2ccccc2)c3ccccc3",
        "pbttt": "c2c(c1sccc1)sc4c2sc(c3sccc3)c4",
        "carbozole": "c1ccc3c(c1)c2ccccc2N3",
        "f8t2": "c1cccc2c1sc3c2cccc3c5ccc(c4sccc4)s5",
        "itic": "C6c4cc3c2sc1ccsc1c2Cc3cc4c7sc5ccsc5c67"
        }

dict_compound = {
    "benzene": "c1ccccc1",
    "p3ht": "c1sccc1CCCCCC",
    "p3ht_tail": "CCCCCC",
    "thiophene": "c1sccc1",
    "itic": "CCCCCCc1ccc(cc1)C2(c3ccc(CCCCCC)cc3)c4cc5c6sc7cc(sc7c6C(c8ccc(CCCCCC)cc8)(c9ccc(CCCCCC)cc9)c5cc4c%10sc%11cc(sc%11c2%10)\C=C%12/C(=O)c%13ccccc%13C%12=C(C#N)C#N)\C=C%14/C(=O)c%15ccccc%15C%14=C(C#N)C#N",
    "ptb7": "CCCCC(CC)COC(=O)c1sc2c(scc2c1F)c3sc4c(OCC(CC)CCCC)c5ccsc5c(OCC(CC)CCCC)c4c3",
    "anthracene": "c1ccc2cc3ccccc3cc2c1",
    "naphthalene": "c1ccc2ccccc2c1",
    "test": "c1sccc1cccccc-c1sccc1cccccc",
    }


def compounds(name):
    return dict_compound[name]

def backbone(name):
    return dict_backbone[name]
