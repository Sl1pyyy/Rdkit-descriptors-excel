from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd

#Creation of an Excel file with SMILES annotations in the first column (SMILES are random for purpose)
smiles_list = [
'[H][C@]12SC(C)(C)[C@@H](N1C(=O)[C@H]2NC(=O)[C@H](N)C1=CC=C(O)C=C1)C(O)=O',
'N[C@]([H])(C)C(=O)O',
'N[C@@]([H])(C)C(=O)O'
]

df = pd.DataFrame({'SMILES': smiles_list})

def descriptors():

    all_descriptors =  []

    for smile in df['SMILES']:
        mol = Chem.MolFromSmiles(smile)

        if mol:
            mol_new = {'SMILES': smile}
            for name,func in Descriptors.descList:
                mol_new[name] = func(mol)
            all_descriptors.append(mol_new)

        else:
            all_descriptors.append({'SMILES': smile})

    return pd.DataFrame(all_descriptors)

if __name__ == '__main__':
    df = descriptors()

    df.to_excel('desc_table.xlsx', index=False)
