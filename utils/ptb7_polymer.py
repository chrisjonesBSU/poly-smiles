import deepsmiles
import mbuild as mb
import sys

def convert_smiles(smiles=False, deep=False):
    '''
    smiles and deep must be str format
    Converts from SMILES to DeepSMILES and vice versa.
    Which ever has a string provided, will convert to the other.
    If strings are proivded for both, then nothing happens
    '''
    converter = deepsmiles.Converter(rings=True, branches=True)
    if smiles and deep:
        print('Only provide a string for one of smiles or deep')
        return()
    if smiles: # Convert from SMILES to DeepSMILES
        deep_string = converter.encode(smiles)
        return deep_string
    if deep: # Convert from DeepSMILES to SMILES
        smiles_string = converter.decode(deep)
        return smiles_string

def polymerize(length = 2, extension = 'mol2', energy_min = True):
    monomer = 'ccccOCCCC))CCCC)))))))cscccscCOCCCCCC))))CC)))))=O))cF)c5cs8))))))))cc5cOCCCC))CCCC)))))))c9s%12'
    template = 'ccccOCCCC))CCCC)))))))cscccscCOCCCCCC))))CC)))))=O))cF)c5c{}))))))))))))s8))))))))cc5cOCCCC))CCCC)))))))c9s%12'
    polymer = '{}'
    for i in range(0, length):
        if i == length - 1:
            polymer = polymer.format(monomer)
            break
        polymer = polymer.format(template)
    polymer_smiles = convert_smiles(deep = polymer)
    print("Building the mbuild compound....")
    compound = mb.load(polymer_smiles, smiles = True)
    if energy_min:
        print("Performing the energy minimization")
        compound.energy_minimize(steps=50, algorithm="md")
    file_name = "PTB7_{}mer.{}".format(length, extension)
    compound.save(file_name, overwrite = True)
    print("Finished!")

chain_length = int(sys.argv[1])

polymerize(length = chain_length)
