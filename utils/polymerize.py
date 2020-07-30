import mbuild
import deepsmiles
from utils import viz
from utils import convert_smiles

def poly_smiles(monomer_string, length=2, ftype = 'mol2', energy_min = False, save = True):
    
    # Find how many branch-brackets are required at polymerization site
    atom_count = 0
    bracket_count = 0
    for string in monomer_string:
        if string.isalpha():
            atom_count += 1    
        if string == ')':
            bracket_count += 1 
    if bracket_count == 0:
        brackets = ')' * atom_count
    elif bracket_count != 0:
        brackets = ')' * (atom_count - bracket_count)
       
    # Find index num of poly site on modified DEEP SMILES string
    monomer_list = list(monomer_string)
    if '*' not in monomer_list:
        return(print('ERROR: Identify the wanted polymerization site using *x*'))
    key_indices = [index for index, string in enumerate(monomer_list) if string == '*']  
    if len(key_indices) != 2:   # Checks for only a single given poly site
        return(print('ERROR: Select only one polymerization site using *x*'))
    if key_indices[1] - key_indices[0] != 2:   # Check that the * are surrounding only a single atom
        return(print('ERROR: Select only one polymerization site using *x*'))
    monomer_list[key_indices[1]] = '{}' + '{}'.format(brackets) # Create poly site+brackets to the right of the atom
    monomer_list.remove('*')
    template = ''.join(monomer_list)  # Monomer string with the {})))) needed for string formating
    monomer_list.remove('{}' + '{}'.format(brackets))
    monomer = ''.join(monomer_list)  # Pure deepsmiles monomer string without {} or *
    # Loop & format to build polymer
    polymer = '{}'
    for i in range(0, length):
        if i == length - 1:
            polymer = polymer.format(monomer) # Format pure smiles monomer string into last {}
            break
        polymer = polymer.format(template) # Format the template into itself length - 1 times

    polymer_smiles = convert_smiles(deep = polymer) # SMILES string of complete polymer
    compound = mb.load(polymer_smiles, smiles = True)
    if energy_min:
        compound.energy_minimize(steps = 30, forcefield='GAFF', algorithm = 'md')
    compound.visualize().show()  
    if save:
        file_name = "comp_{}mer.{}".format(length, ftype)
        compound.save(file_name, overwrite = True)
        return(print("{} saved".format(file_name)))

    return polymer, polymer_smiles
